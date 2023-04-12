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
    print(bcolors.HEADER + "提示:此时文字颜色为pink")
    print(bcolors.OKBLUE + "提示:此时文字颜色为blue")
    print(bcolors.OKGREEN + "提示:此时文字颜色为green")
    print(bcolors.WARNING + "提示:此时文字颜色为yellow")
    print(bcolors.FAIL + "提示:此时文字颜色为red")
    print(bcolors.ENDC + "提示:此时文字颜色为black")
    print(bcolors.UNDERLINE + "提示:此时文字颜色为black+underline")
    print(bcolors.BOLD + "提示:此时文字颜色为black+bold")

# pip install numpy -i https://mirrors.aliyun.com/pypi/simple/
