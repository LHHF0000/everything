import os

path = r'E:\\'

def deal(name):
    if "Fc2" in name:
        return
    if name.isdigit():
        return
    if name in dict:
        dict[name] += 1
    else:
        xx = {name: 1}
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
            fileSize = os.path.getsize(fullPathName)/1024/1024/1024
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
    dictSortByNumber = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    dictSortByName = sorted(dict.items(), key=lambda x: x[0])
    numList = tuple(dict.values())
    num = 0
    for i in range(len(dictSortByNumber)):
        print(i+1, dictSortByNumber[i])
    for i in range(len(numList)):
        num += numList[i]
    print(num)
    # for i in range(len(dictSortByName)):
    #     print(dictSortByName[i], '\n', end="")
