import os

def remove_string_from_filenames(directory, string_to_remove):
    """
    批量删除文件名中的指定字符串
    
    参数:
    directory: 文件夹路径
    string_to_remove: 要从文件名中删除的字符串
    """
    # 检查目录是否存在
    if not os.path.exists(directory):
        print(f"错误：目录 '{directory}' 不存在")
        return
    
    # 获取目录中的所有文件和文件夹
    items = os.listdir(directory)
    
    # 计数器，记录重命名的文件数量
    rename_count = 0
    
    for filename in items:
        # 构建完整的文件路径
        old_filepath = os.path.join(directory, filename)
        
        # 只处理文件，忽略子目录（如需处理子目录，可移除这个判断）
        if os.path.isfile(old_filepath):
            # 检查文件名中是否包含要删除的字符串
            if string_to_remove in filename:
                # 删除文件名中的指定字符串
                new_filename = filename.replace(string_to_remove, "")
                new_filepath = os.path.join(directory, new_filename)
                
                # 避免文件名冲突
                if not os.path.exists(new_filepath):
                    # 重命名文件
                    os.rename(old_filepath, new_filepath)
                    print(f"重命名: '{filename}' -> '{new_filename}'")
                    rename_count += 1
                else:
                    print(f"警告: 文件 '{new_filename}' 已存在，跳过重命名")
    
    print(f"操作完成！共重命名 {rename_count} 个文件")

# 使用示例
if __name__ == "__main__":
    # 设置要处理的目录路径
    path = input("请输入要处理的目录路径: ").strip()
    
    # 设置要删除的字符串
    string_to_remove = "h265"
    
    # 调用函数
    remove_string_from_filenames(path, string_to_remove)