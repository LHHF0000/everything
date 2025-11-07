import os

path1 = r'D:\迅雷下载\1'
path2 = r'F:\FC2\2503'
path3 = r'G:\0\T4：tmp'


def getC(name):
    return path1 + os.sep + name


def getD(name):
    return path2 + os.sep + name


def getE(name):
    return path3 + os.sep + name


if __name__ == '__main__':
    # 桃乃木香奈-ipx-813-C-2202-女仆-cut
    list = [

]


    n = 0
    for i in list:
        print(list[n])
        check = input()
        if '' == check:
            if os.path.exists(getC(list[n][0])):
                os.rename(getC(list[n][0]), getC(list[n][1]))
                n += 1
            elif os.path.exists(getD(list[n][0])):
                os.rename(getD(list[n][0]), getD(list[n][1]))
                n += 1
            elif os.path.exists(getE(list[n][0])):
                os.rename(getE(list[n][0]), getE(list[n][1]))
                n += 1
            else:
                n += 1
                continue
        else:
            n += 1
            continue