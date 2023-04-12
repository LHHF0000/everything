import os
from pprint import pprint

path = r'E:\0tmp'

if __name__ == '__main__':
    fileList = os.listdir(path)
    print(fileList)
    n = 0
    list = []
    for i in fileList:
        row = [fileList[n], fileList[n]]
        list.append(row)
        n += 1
    pprint(list)