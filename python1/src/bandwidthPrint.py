import subprocess
import re
import time
from statistics import mean

class bcolors:
    HEADER = '\033[95m'       # pink
    OKBLUE = '\033[94m'       # blue
    OKGREEN = '\033[92m'      # green
    WARNING = '\033[93m'      # yellow
    FAIL = '\033[91m'         # red
    ENDC = '\033[0m'          # black
    BOLD = '\033[1m'          # black+bold
    UNDERLINE = '\033[4m'     # black+underline

def get_connection_speed():
    output = subprocess.check_output("netsh wlan show interfaces", shell=True)
    output = output.decode("gbk")

    # 使用正则表达式从输出中提取连接速度
    pattern1 = r"接收速率\(Mbps\)\s*:\s*(\d+)\s*"
    pattern2 = r"传输速率 \(Mbps\)\s*:\s*(\d+)\s*"
    match1 = re.search(pattern1, output)
    match2 = re.search(pattern2, output)
    if match1 and match2:
        receive_speed = int(match1.group(1))
        transmit_speed = int(match2.group(1))
        return receive_speed, transmit_speed

    return None


if __name__ == '__main__':
    receive_speed_list = []
    transmit_speed_list = []
    start_time = time.time()

    while True:
        speed = get_connection_speed()
        if speed:
            receive_speed, transmit_speed = speed
            receive_speed_list.append(receive_speed)
            transmit_speed_list.append(transmit_speed)
            print(bcolors.ENDC + str(receive_speed), ' | ', str(transmit_speed))

        elapsed_time = time.time() - start_time
        if elapsed_time >= 120:
            avg_receive_speed = int(mean(receive_speed_list))
            avg_transmit_speed = int(mean(transmit_speed_list))
            print(bcolors.OKGREEN + str(avg_receive_speed), ' | ', str(avg_transmit_speed))
            receive_speed_list = []
            transmit_speed_list = []
            start_time = time.time()

        time.sleep(2)
