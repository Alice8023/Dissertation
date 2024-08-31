import os
import shutil
import csv

def copy_csv(input_file, output_file):
    # 复制源文件为目标文件
    shutil.copyfile(input_file, output_file)

def check_news_files(input_csv, news_folder):
    # 创建一个临时列表来保存更新后的行数据
    updated_rows = []

    with open(input_csv, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            filename = row[1].split(".mp4")[0]  # 提取文件名
            found = False
            for news_file in os.listdir(news_folder):
                if filename in news_file:
                    row.append("yes")
                    found = True
                    break
            if not found:
                row.append("error")
            updated_rows.append(row)

    # 将更新后的行写入新的CSV文件
    with open(input_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(updated_rows)

# 指定源CSV文件和目标CSV文件
input_csv = "youtube_cooking_info.csv"
output_csv = "youtube_cooking_name.csv"

# 复制源CSV文件
copy_csv(input_csv, output_csv)

# 指定News文件夹路径
news_folder = "cooking"

# 检查News文件中的文件是否与CSV文件中的第二列匹配，并更新CSV文件中的第五列
check_news_files(output_csv, news_folder)
