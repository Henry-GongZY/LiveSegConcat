import os
import time
import re
import subprocess

def remove_chinese_characters(filename):
    # 使用正则表达式匹配中文字符
    pattern = re.compile(r'[^\x00-\x7F]+')
    # 使用sub函数替换中文字符为空字符串
    new_filename = pattern.sub('', filename)
    return new_filename

# 遍历当前目录下的所有文件
for _, _, filenames in os.walk('./'):
    for filename in filenames:
        new_filename = remove_chinese_characters(filename)
        # 如果文件名有变化，重命名文件
        if new_filename != filename:
            os.rename(filename, new_filename)

format = ['flv', 'mp4']

date = input("请输入日期：")

for _, _, filenames in os.walk('./'):
    for filename in filenames:
        if filename.split('.')[-1] in format and date in filename:
            with open(f'mylist_{date}.txt', 'a', encoding='utf-8') as f:
                f.write(f"file '{filename}'\n")

time.sleep(1)

# ffmpeg -f concat -i mylist_20240423.txt -c copy output_0422.flv
subprocess.run(['ffmpeg', '-f', 'concat', '-i', f'mylist_{date}.txt', '-c', 'copy', f'{date}.flv'])

print(date)