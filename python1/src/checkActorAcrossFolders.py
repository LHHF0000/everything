import os

# 检查同一演员是否分布在多个文件夹中，并打印出相关信息
# 根目录：里面是各个文件夹，文件夹里是"演员-影片名"命名的文件
path = r'G:\0\\'

# 需要排除的文件夹
exclude_folders = [
    "T4.0：SF DP",
    "T4.2：无码流出",
   ]


def parse_actors(filename):
    """从文件名中解析演员名字，支持“、”分隔的多个演员"""
    name = filename.rsplit(".", 1)[0]           # 去掉扩展名
    actor_part = name.split("-", 1)[0]          # 取“-”前的演员部分
    actors = actor_part.split("、")             # 多个演员用“、”分隔
    return [a.strip() for a in actors if a.strip()]


def main():
    # actor -> {folder -> [文件列表]}
    actor_map = {}

    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)
        if not os.path.isdir(folder_path):
            continue
        if folder in exclude_folders:
            continue

        for f in os.listdir(folder_path):
            full_path = os.path.join(folder_path, f)
            if not os.path.isfile(full_path):
                continue
            # 跳过字幕、图片等非视频文件
            if f.lower().endswith((".srt", ".txt", ".jpg", ".jpeg", ".png", ".gif", ".nfo")):
                continue

            actors = parse_actors(f)
            for actor in actors:
                actor_map.setdefault(actor, {}).setdefault(folder, []).append(f)

    # 打印分布在多个文件夹的演员
    found = False
    for actor, folders in sorted(actor_map.items()):
        if len(folders) > 1:
            found = True
            print(f"演员: {actor}  (出现在 {len(folders)} 个文件夹)")
            for folder, files in sorted(folders.items()):
                print(f"  [{folder}]  {len(files)} 个文件")
                for f in sorted(files):
                    print(f"      - {f}")
            print()

    if not found:
        print("未发现同一演员分布在多个文件夹的情况")


if __name__ == '__main__':
    main()
