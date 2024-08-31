# import requests
# import os
#
# # 设置下载文件的 URL
# url = 'https://download.ted.com/products/100045.mp4?apikey=TEDDOWNLOAD'
#
# # 设定目标文件夹（通常是用户的下载文件夹）
# download_folder = os.path.expanduser('~/Downloads')  # 根据操作系统的不同可能需要调整
# file_name = '100045.mp4'
# file_path = os.path.join(download_folder, file_name)
#
# # 发送 HTTP GET 请求下载文件
# response = requests.get(url, stream=True)
#
# # 检查请求是否成功
# if response.status_code == 200:
#     # 将下载内容写入文件
#     with open(file_path, 'wb') as file:
#         for chunk in response.iter_content(chunk_size=8192):
#             file.write(chunk)
#     print(f'文件已成功下载到 {file_path}')
# else:
#     print(f'下载失败，状态码: {response.status_code}')
import pandas as pd
import requests
import os

# Read CSV file
file_path = '/Users/alicezhang/Downloads/pythonProject5/Download_and_ASR/ted_downloaded_link_add2.csv'
df = pd.read_csv(file_path)

# Set the target folder for downloading files
download_folder = os.path.expanduser('/Users/alicezhang/Downloads/pythonProject5/Download_and_ASR/TED_video_from_official22')

for index, row in df.iterrows():
    # Get download_link and talk_id from each row
    url = row['download_link']
    talk_id = row['talk_id']
    file_name = f'{talk_id}.mp4'
    full_path = os.path.join(download_folder, file_name)

    # Download the file
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(full_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f'File successfully downloaded to {full_path}')
        else:
            print(f'Failed to download {file_name}, status code: {response.status_code}')
    except Exception as e:
        print(f'Error occurred while downloading {file_name}: {e}')
