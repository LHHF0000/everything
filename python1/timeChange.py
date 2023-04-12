import os
import re

class bcolors:
    HEADER = '\033[95m'       # pink
    OKBLUE = '\033[94m'       # blue
    OKGREEN = '\033[92m'      # green
    WARNING = '\033[93m'      # yellow
    FAIL = '\033[91m'         # red
    ENDC = '\033[0m'          # black
    BOLD = '\033[1m'          # black+bold
    UNDERLINE = '\033[4m'     # black+underline

if __name__ == '__main__':
    path=r'E:\0tmp'
    fileList = os.listdir(path)
    n = 0
    for i in fileList:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + os.sep + fileList[n]  # os.sep添加系统分隔符
        # 判断当前是否是文件
        if os.path.isfile(oldname):

            oldname1 = fileList[n].split(".")
            # oldnameList = oldname1[0].rsplit("-", 1)
            result = re.findall(r'(\d{8})', oldname1[0])
            if len(result) < 1:
                n += 1
                continue
            res = ""
            for i in range(0, len(result[0])):
                if i == 2 or i == 3 or i == 4 or i == 5:
                    res = res + result[0][i]
            oldname1[0] = oldname1[0].replace(result[0], res)
            newname = oldname1[0] + '.' + oldname1[1]
            print(n)
            print(fileList[n])
            print(bcolors.OKBLUE + newname)
            finalCheck = input("检查文件名: 回车继续，1修改，2跳过")
            if finalCheck == '1':
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
