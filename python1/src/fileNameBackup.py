import os

def get_all_file_names(folder_paths):
    file_names = []

    for folder_path in folder_paths:
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                # 记录文件所在文件夹的名称，用于后续按文件夹名排序
                file_names.append((os.path.basename(root), file_name))

    # 先按文件夹名排序，再按文件名排序
    file_names.sort(key=lambda item: (item[0], item[1]))

    return file_names

if __name__ == '__main__':
    # 调用函数并传入多个文件夹路径
    folder_paths = [
        r'G:\0',
        r'F:\0-F',
        # 在此添加更多目录，例如 r'G:\1'
    ]
    file_names = get_all_file_names(folder_paths)

    # 指定保存文件的路径
    output_file = r'E:\图片、文档、下载_副本\图片\old2017\bak.txt'

    # 将文件名保存到文本文件中（w 模式会直接覆盖原有内容）
    with open(output_file, 'w', encoding='utf-8') as file:
        for _, file_name in file_names:
            file.write(file_name + '\n')
