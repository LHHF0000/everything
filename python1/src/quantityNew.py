import os
import re

class bcolors:
    HEADER = '\033[95m'       # pink
    ENDC = '\033[0m'  # black


path = r'E:\\'

def deal(name, fileSize):
    pattern = r'^[a-zA-Z]{3,4}$'
    if "Fc2" in name or name.isdigit() or re.match(pattern, name):
        return
    if name in dict:
        dict[name][0] += 1
        dict[name][1] += fileSize
    else:
        xx = {name: [1, fileSize]}
        dict.update(xx)


if __name__ == '__main__':
    pathList = os.listdir(path)
    n = 1
    dict = {}
    while n <= 17:
        filePath = path + pathList[n]
        fileList = os.listdir(filePath)
        for i in fileList:
            fullPathName = filePath + '\\' + i
            fileSize = round(os.path.getsize(fullPathName)/1024/1024/1024, 3)
            fullFileName = i.rsplit(".", 1)
            if fullFileName[1] == "srt":
                continue
            actorName = fullFileName[0].split("-", 1)[0]
            if "、" in actorName:
                actorNameList = actorName.split("、")
                for j in actorNameList:
                    deal(j, fileSize)
            else:
                deal(actorName, fileSize)
        n += 1
    dictSortByNumber = sorted(dict.items(), key=lambda x: x[1][0], reverse=True)
    dictSortBySize = sorted(dict.items(), key=lambda x: x[1][1], reverse=True)
    dictSortByName = sorted(dict.items(), key=lambda x: x[0])
    numList = tuple(dict.values())
    num = 0
    for i in range(len(dictSortBySize)):
        print('%-2s\t%-8s\t%-1s\t%-6s\t' % (i + 1, dictSortByNumber[i][0],
                bcolors.HEADER + str(dictSortByNumber[i][1][0]) + bcolors.ENDC, round(dictSortByNumber[i][1][1], 2)))
        # print(f'{i+1:<5}{dictSortByNumber[i][0]:<10}{repr(dictSortByNumber[i][1][0]):<4}{repr(round(dictSortByNumber[i][1][1], 2)):>6}')
    for i in range(len(numList)):
        num += numList[i][0]
    print(num)
    # for i in range(len(dictSortByName)):
    #     print(dictSortByName[i], '\n', end="")
