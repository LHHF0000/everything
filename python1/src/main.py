import os
from pprint import pprint

path = r'E:\0\0tmp'
# path = r'F:\tmp'
# path = r'D:\迅雷下载'

if __name__ == '__main__':
    fileList = os.listdir(path)
    n = 0
    list = []
    for i in fileList:
        row = [fileList[n], fileList[n]]
        list.append(row)
        n += 1
    pprint(list)