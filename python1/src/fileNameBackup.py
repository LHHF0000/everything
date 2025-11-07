import os

def get_all_file_names(folder_path):
    file_names = []

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_names.append(file_name)

    return file_names

if __name__ == '__main__':
    # 调用函数并传入文件夹路径
    folder_path = r'G:\0'
    file_names = get_all_file_names(folder_path)

    # 指定保存文件的路径
    output_file = r'D:\图片\old2017\bak.txt'

    # 删除已存在的文件内容
    with open(output_file, 'w', encoding='utf-8') as file:
        file.truncate(0)

    # 将文件名保存到文本文件中
    with open(output_file, 'a', encoding='utf-8') as file:
        for file_name in file_names:
            file.write(file_name + '\n')
