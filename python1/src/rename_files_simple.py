import os

def rename_files_simple(directory=r"E:\video workspace\output1 VR"):
    """简单版本：直接替换当前目录下文件名中的cp为cq"""
    for filename in os.listdir(directory):
        if "cp" in filename:
            new_name = filename.replace("cp", "cq")
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"重命名: {filename} -> {new_name}")

if __name__ == "__main__":
    rename_files_simple()