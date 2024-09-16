import os
import shutil

# 当前工作目录
# current_directory = os.getcwd()
script_path = os.path.abspath(__file__)
current_directory = os.path.join(script_path, "..", "images")

# 遍历当前目录及其所有子目录
for root, dirs, files in os.walk(current_directory):
    # 遍历所有文件
    for file in files:
        # 检查文件扩展名是否为.png
        if file.endswith('.png'):
            # 构建原始文件路径
            old_file_path = os.path.join(root, file)
            # 获取相对于当前目录的路径，不包括文件名
            relative_path = os.path.relpath(root, current_directory)
            # 将路径中的分隔符替换为下划线
            prefix = relative_path.replace(os.sep, '_') if relative_path != '.' else ''
            # 如果路径是当前目录，则prefix为空字符串
            if prefix:
                prefix += '_'
            # 构建新的文件名
            new_file_name = f"{prefix}{file}"
            # 构建新的文件路径
            new_file_path = os.path.join(current_directory, new_file_name)
            # 移动并重命名文件
            shutil.move(old_file_path, new_file_path)
            print(f"Moved and renamed: {old_file_path} to {new_file_path}")

print("All .png files have been moved and renamed.")