import os
from pprint import pprint

path = r'G:\0\T4：tmp'
# path = r'F:\tmp'
# path = r'D:\迅雷下载\1'

if __name__ == '__main__':
    fileList = os.listdir(path)
    n = 0
    list = []
    for i in fileList:
        row = [fileList[n], fileList[n]]
        list.append(row)
        n += 1
    pprint(list)