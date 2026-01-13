import os
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import time

def modifyFileTime(filePath, createTime, modifyTime, accessTime, offset):
    """
    修改文件时间属性
    :param filePath: 文件路径名
    :param createTime: 创建时间
    :param modifyTime: 修改时间
    :param accessTime: 访问时间
    :param offset: 时间偏移的秒数,tuple格式
    """
    try:
        format = "%Y-%m-%d %H:%M:%S" # 时间格式
        cTime_t = timeOffsetAndStruct(createTime, format, offset[0])
        mTime_t = timeOffsetAndStruct(modifyTime, format, offset[1])
        aTime_t = timeOffsetAndStruct(accessTime, format, offset[2])

        fh = CreateFile(filePath, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
        createTimes, accessTimes, modifyTimes = GetFileTime(fh)

        createTimes = Time(time.mktime(cTime_t))
        accessTimes = Time(time.mktime(aTime_t))
        modifyTimes = Time(time.mktime(mTime_t))
        SetFileTime(fh, createTimes, accessTimes, modifyTimes)
        CloseHandle(fh)
        return 0
    except Exception as e:
        print(f"修改文件时间失败: {e}")
        return 1

def timeOffsetAndStruct(times, format, offset):
    return time.localtime(time.mktime(time.strptime(times, format)) + offset)

def getFileTime(filePath):
    """
    获取文件的时间属性
    :param filePath: 文件路径
    :return: (创建时间, 修改时间, 访问时间) 的字符串格式
    """
    try:
        fh = CreateFile(filePath, GENERIC_READ, 0, None, OPEN_EXISTING, 0, 0)
        createTime, accessTime, modifyTime = GetFileTime(fh)
        CloseHandle(fh)
        
        # 转换时间为可读格式
        def timeToStr(t):
            return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t.timestamp()))
        
        return (timeToStr(createTime), timeToStr(modifyTime), timeToStr(accessTime))
    except Exception as e:
        print(f"获取文件时间失败: {e}")
        return None

def sync_file_times(path1, path2):
    """
    同步两个路径下文件的时间
    :param path1: 源文件路径
    :param path2: 目标文件路径（需要修改时间的文件路径）
    """
    # 获取路径1下的所有文件
    path1_files = {}
    for filename in os.listdir(path1):
        if os.path.isfile(os.path.join(path1, filename)):
            name, ext = os.path.splitext(filename)
            path1_files[name] = filename
    
    # 获取路径2下的所有文件
    path2_files = {}
    for filename in os.listdir(path2):
        if os.path.isfile(os.path.join(path2, filename)):
            # 移除文件名中的"-h265cq27"来匹配路径1的文件
            name, ext = os.path.splitext(filename)
            original_name = name.replace("-cq29", "")
            path2_files[original_name] = filename
    
    # 同步时间
    success_count = 0
    fail_count = 0
    
    for file_key in path1_files:
        if file_key in path2_files:
            path1_file = os.path.join(path1, path1_files[file_key])
            path2_file = os.path.join(path2, path2_files[file_key])
            
            print(f"处理文件: {path1_files[file_key]} -> {path2_files[file_key]}")
            
            # 获取路径1文件的时间
            times = getFileTime(path1_file)
            if times:
                createTime, modifyTime, accessTime = times
                
                # 修改路径2文件的时间
                offset = (0, 0, 0)  # 不需要时间偏移
                result = modifyFileTime(path2_file, createTime, modifyTime, accessTime, offset)
                
                if result == 0:
                    print(f"✓ 成功同步时间: {path2_files[file_key]}")
                    success_count += 1
                else:
                    print(f"✗ 同步失败: {path2_files[file_key]}")
                    fail_count += 1
            else:
                print(f"✗ 无法获取源文件时间: {path1_files[file_key]}")
                fail_count += 1
        else:
            print(f"⚠ 路径2中未找到对应文件: {file_key}")
    
    print(f"\n同步完成！成功: {success_count}, 失败: {fail_count}")

if __name__ == '__main__':
    # 配置路径
    path1 = r"D:\video workspace\input T3"  # 替换为实际的路径1
    path2 = r"D:\video workspace\output T3"  # 替换为实际的路径2
    
    # 检查路径是否存在
    if not os.path.exists(path1):
        print(f"错误: 路径1不存在 - {path1}")
    elif not os.path.exists(path2):
        print(f"错误: 路径2不存在 - {path2}")
    else:
        sync_file_times(path1, path2)