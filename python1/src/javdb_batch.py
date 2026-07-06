# -*- coding: utf-8 -*-
import re
import time
import random
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ================== 配置 ==================
INPUT_FILE = r"D:\Projects\python1\src\numbers.txt"          # 输入文件，每行一个原始文件名
OUTPUT_JSON = r"D:\Projects\python1\src\results.json"          # 输出的 JSON 文件
BASE_URL = "https://javdb573.com"
WAIT_TIMEOUT = 8  # 显式等待超时（秒）

# ---------- 元素定位器 ----------
SEARCH_BOX = (By.ID, "video-search")
SEARCH_BUTTON = (By.ID, "search-submit")
FIRST_RESULT_LINK = (By.CSS_SELECTOR, ".movie-list .item a")
TITLE_SELECTOR = (By.CSS_SELECTOR, "strong.current-title")
DATE_SELECTOR = (By.XPATH, "//strong[text()='日期:']/following-sibling::span[@class='value']")
ACTOR_LIST_SELECTOR = (By.CSS_SELECTOR, ".panel-block .value a")
# ==================================================

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    # 核心修正：设置页面加载策略为 eager（不等待图片等资源）
    options.set_capability("pageLoadStrategy", "eager")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def random_sleep(min_sec=2, max_sec=5):
    time.sleep(random.uniform(min_sec, max_sec))

def extract_number_from_filename(filename):
    base = os.path.splitext(filename)[0]
    match = re.search(r'([a-zA-Z]+-\d+)', base)
    return match.group(1) if match else base

def get_first_female_actor(driver):
    try:
        actor_links = driver.find_elements(*ACTOR_LIST_SELECTOR)
        for link in actor_links:
            try:
                sibling = link.find_element(By.XPATH, "./following-sibling::strong[contains(@class,'symbol')]")
                if "female" in sibling.get_attribute("class"):
                    return link.text.strip()
            except:
                continue
        if actor_links:
            return actor_links[0].text.strip()
        return ""
    except:
        return ""

def search_and_click_first(driver, number):
    """在当前页面执行搜索并点击第一个结果"""
    try:
        # 等待搜索框可见且可交互
        search_box = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(SEARCH_BOX)
        )
        search_box.clear()
        search_box.send_keys(number)
        time.sleep(random.uniform(0.3, 0.6))

        # 点击检索按钮
        search_btn = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(SEARCH_BUTTON)
        )
        search_btn.click()

        # 等待第一个结果链接出现（可点击）
        first_link = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(FIRST_RESULT_LINK)
        )
        first_link.click()

        # 等待详情页的标题加载（确保页面切换完成）
        WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(TITLE_SELECTOR)
        )
        return True
    except TimeoutException:
        print(f"   ⏱️ 超时：未找到搜索结果或详情页")
        return False
    except Exception as e:
        print(f"   ❌ 搜索/点击异常: {e}")
        return False

def extract_details(driver, original_filename, number):
    try:
        title_elem = driver.find_element(*TITLE_SELECTOR)
        title = title_elem.text.strip()
    except:
        title = ""

    try:
        date_elem = driver.find_element(*DATE_SELECTOR)
        date_str = date_elem.text.strip()
        parts = date_str.split('-')
        yymm = parts[0][2:] + parts[1] if len(parts) == 3 else ""
    except:
        yymm = ""

    actress = get_first_female_actor(driver)

    base_name = os.path.splitext(original_filename)[0]
    if actress and yymm and title:
        clean_title = re.sub(r'[\\/*?:"<>|]', '', title)
        new_filename = f"{actress}-{base_name}-{yymm}-{clean_title}.mp4"
    else:
        new_filename = original_filename

    return {
        "original": original_filename,
        "number": number,
        "actress": actress,
        "yymm": yymm,
        "title": title,
        "new_filename": new_filename
    }

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ 找不到 {INPUT_FILE}，请创建并每行写入一个文件名。")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        filenames = [line.strip() for line in f if line.strip()]

    if not filenames:
        print("❌ 输入文件为空。")
        return

    print(f"📋 共 {len(filenames)} 个文件待处理。")
    driver = setup_driver()

    # 首次打开首页
    driver.get(BASE_URL)
    try:
        WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(SEARCH_BOX)
        )
    except:
        print("⚠️ 首页加载超时，但继续尝试...")

    results = []

    try:
        for idx, filename in enumerate(filenames, 1):
            print(f"\n🔍 [{idx}/{len(filenames)}] 处理: {filename}")
            number = extract_number_from_filename(filename)
            print(f"   番号: {number}")

            if not search_and_click_first(driver, number):
                results.append({
                    "original": filename,
                    "number": number,
                    "actress": "",
                    "yymm": "",
                    "title": "",
                    "new_filename": filename
                })
                random_sleep(1, 2)
                continue

            info = extract_details(driver, filename, number)
            results.append(info)
            print(f"   ✅ 女优: {info['actress']}, 日期: {info['yymm']}, 标题: {info['title'][:20]}...")

            random_sleep(2, 5)

    except KeyboardInterrupt:
        print("\n🛑 用户中断，保存已处理数据...")
    finally:
        driver.quit()

    output_data = [[r["original"], r["new_filename"]] for r in results]

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 完成！结果保存至 {OUTPUT_JSON}")
    print("示例输出：")
    for i, pair in enumerate(output_data[:3]):
        print(f"  {i+1}. {pair[0]} -> {pair[1]}")
    if len(output_data) > 3:
        print(f"  ... 共 {len(output_data)} 项")

if __name__ == "__main__":
    main()