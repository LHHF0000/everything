import os
import re
import requests
import hashlib  # 用来计算MD5码
import win32clipboard as wcb
import win32con as wc

class bcolors:
    HEADER = '\033[95m'       # pink
    OKBLUE = '\033[94m'       # blue
    OKGREEN = '\033[92m'      # green
    WARNING = '\033[93m'      # yellow
    FAIL = '\033[91m'         # red
    ENDC = '\033[0m'          # black
    BOLD = '\033[1m'          # black+bold
    UNDERLINE = '\033[4m'     # black+underline

def ctrlc(fan):
    wcb.OpenClipboard()
    wcb.EmptyClipboard()
    wcb.SetClipboardData(wc.CF_TEXT, fan.encode("gbk"))
    wcb.CloseClipboard()

def ctrlv():
    wcb.OpenClipboard()
    data = wcb.GetClipboardData(wc.CF_TEXT)
    wcb.CloseClipboard()
    return data.decode("gbk")

def gettitle(fan, flag):
    url = "https://javdb001.com/search?q=ipx-666&f=all"
    url=url.replace("ipx-666", fan)
    payload = {}
    headers = {
        'authority': 'javdb001.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://javdb001.com/',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'list_mode=h; theme=auto; locale=zh; __cf_bm=uxsSLZ1zmhC04Stm3QhrndC0S4ETbT6FxZj9rFCp79A-1662045225-0-AV2RpSmIrqk+qt2NsjZFwJj9MZXPSMmuPqDAHjtF9LMvDtoQIxe/q3hgIoZjeeUAFtIbsllXNZ0rh2jOH8d7anf3ysIk1yahDMmtS3Laousli16lvDGha+fFozL/DIxCCg==; over18=1; _jdb_session=fQ6bBCLO0KYoNA72QDeSmMqKVJAaryD%2BAsMoKVtKhMArrVD7K1bxRni0aSEeZ5SaGuYAbi1x%2B2w7WEBeCAjD8axSOfvMW1tl6MxJ5fL4StM%2Bn7rDdLgDdj2fhonc0PjNSM4M5plzeUCLnVmhvmTNUPampe0xj25OaeqBrfakAD68qd0WLzNawyUd8fKT6BZPIVapFoo8i%2ByJCoIvvqN5e3R4NyYkfgU0UPHK96f5VbGVEQtVyIk%2BNgAwoclgcKksseOFNQYTrccvtpDupFCo54BXgkstJ7SPNX%2BpAhVRo3o08mMBV7EzlerG--MxF28WxJKt7IZgde--AMOISqvON28%2FY6v%2BJUuhKA%3D%3D; _jdb_session=frjwFbbuHwn0xpS9ZDI1i7%2FQfOeT1QfBPW0HtYLicmrbPEc6NII8jN8hHadxdfiUpOaytgz%2BSA%2FvBWMubO1e4lA2H8vh%2Bc3cY%2B96gnfX6595WrHMuXRgVy%2Bn%2F%2Flua1YLJ7RRGKBn0zPrUl%2FBbG7fy%2FHJCfxm%2F7o5LT35pdB7hDrTAt4KQ%2FNurq5lNfzc83c2ns97%2Bsqixw%2FHeG%2F1gzWFqvJoLGAsyrWLJeEZICJIfjaOJK%2FkBakywn7erCuqPLnpQrNE5ws3ylKROW1iFtLEs7dqmDmnantUWwyXiH1HlGK3GSJsJVqP8VmN--NqGyIyugBzPWvQVg--4FJFMbHUtrJBs3i6xLy8vw%3D%3D; locale=zh'
    }
    proxies = {"http": None, "https": None}
    response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=proxies)
    txt = response.text
    txt = txt.replace("\r", "")
    txt = txt.replace("\n", "")
    tag0 = r"<strong>" + fan.upper() + "</strong>(.+?)</div>"
    match = re.search(r'\d{4}-\d{2}-\d{2}', txt)
    time = match[0].replace('-', '')

    # print(txt)
    res = re.findall(tag0, txt)
    if len(res) < 1:
        return "没有找到"
    else:
        print(time)
        print(fanyi(res[0]))
        if flag == 2:
            return "-"+time+"-"+fanyi(res[0])
        else:
            return "-"+time+"-"

def fanyi(shuru):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    appid, salt, key = "20220307001115013", "666", "xj4Yz1A2jRpmGcJbnkNG"
    q = shuru
    sign = appid + q + salt + key
    md5 = hashlib.md5()
    md5.update(sign.encode('utf-8'))  # 生成签名计算MD5码
    data = {
        "q": q,
        "from": "auto",
        "to": "zh",
        "appid": appid,
        "salt": salt,
        "sign": md5.hexdigest()
    }
    proxies = {"http": None, "https": None}
    response = requests.post('https://fanyi-api.baidu.com/api/trans/vip/translate', headers=header, data=data, verify=False, proxies=proxies)  # 发送post请求
    text = response.json()  # 返回的为json格式用json接收数据
    # print(text)
    shuchu = text['trans_result'][0]['dst']
    return shuchu

if __name__ == '__main__':
    path=r'E:\tmp'
    fileList = os.listdir(path)
    n = 0
    for i in fileList:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + os.sep + fileList[n]  # os.sep添加系统分隔符
        # 判断当前是否是文件
        if os.path.isfile(oldname):
            print(fileList[n])
            no=input("回车继续,跳过输入0")
            if no == '0':
                n += 1
                print("\n")
                continue
            oldname1 = fileList[n].rsplit(".", 1)
            oldnameList = oldname1[0].rsplit("-", 1)
            result = re.findall(r'(\w{3,})-(\d{3,})', oldnameList[0])
            if len(result) < 1:
                fan = input("请输入番号：")
            else:
                fan = result[0][0] + "-" + result[0][1]
                print(bcolors.OKBLUE + fan)
                # check = input("检查番号(回车继续1修改）：")
                # if check == '1':
                #     fan = input("请重新输入番号：")
            ctrlc(fan)

            back = input("请输入返回结果：")
            if back == '':
                back = ctrlv()
            res = back.split('/')
            if len(res) == 2:
                newname = oldname1[0] + '-' + res[0].replace('-', '') + '-' + fanyi(res[1]) + '.' + oldname1[1]
            else:
                newname = oldnameList[0] + '-' + res[0].replace('-', '') + '-' + oldnameList[1] + '.' + oldname1[1]
            print(bcolors.OKGREEN + fileList[n])
            print(bcolors.OKBLUE + newname)
            finalCheck = input("检查文件名: 回车继续，1修改，2跳过")
            if finalCheck == '1':
                ctrlc(newname)
                newname = input("重新输入名称")
                fullNewname = path + os.sep + newname
                os.rename(oldname, fullNewname)
            elif finalCheck == '':
                fullNewname = path + os.sep + newname
                os.rename(oldname, fullNewname)  # 用os模块中的rename方法对文件改名
            else:
                n += 1
                print("\n")
                continue
            print(bcolors.OKGREEN + oldname, '======>', newname)
            print("\n")
            n += 1
