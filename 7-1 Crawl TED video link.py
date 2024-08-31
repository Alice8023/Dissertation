import requests
from bs4 import BeautifulSoup
import csv
import time  # 导入time模块

# 设置URL模板
url_template = "https://www.ted.com/talks/quick-list?page={}"

# 创建CSV文件并写入标题行
with open('../ted_crawl_official_list2.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Partial Link', 'Title', 'Event', 'Published', 'Download Link (Low)',
                  'Download Link (Medium)', 'Download Link (1080p)', 'Modified_Link_transcript']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # 循环遍历页面
    for page_number in range(1, 175):
        url = url_template.format(page_number)
        response = requests.get(url)

        if response.status_code == 200:
            # 创建BeautifulSoup对象
            soup = BeautifulSoup(response.text, 'html.parser')

            # 提取所有演讲信息块
            talk_blocks = soup.find_all('div', class_='col xs-12 quick-list__container-row')

            # 遍历每个演讲块并提取信息
            for talk_block in talk_blocks:
                partial_link = talk_block.select_one('.col-xs-6.title a')['href']
                title1 = talk_block.select_one('.col-xs-6.title a').text
                event = talk_block.select_one('.col-xs-2.event a').text
                # 提取Published信息
                published_span = talk_block.select_one('.col-xs-1 span.meta')
                if published_span:
                    published = published_span.get_text(strip=True)

                # 在标题中添加下载地址标识
                download_links = talk_block.select('.quick-list__download a')
                download_dict = {link.text: link['href'] for link in download_links}

                # 构建Modified_Link_transcript
                modified_link_transcript = f"https://www.ted.com{partial_link}/transcript"

                # 写入CSV文件
                writer.writerow({
                    'Partial Link': partial_link,
                    'Title': title1,
                    'Event': event,
                    'Published': published if 'published' in locals() else '',
                    'Download Link (Low)': download_dict.get('Low', ''),
                    'Download Link (Medium)': download_dict.get('Medium', ''),
                    'Download Link (1080p)': download_dict.get('1080p', ''),
                    'Modified_Link_transcript': modified_link_transcript
                })

            # 休息2秒
            time.sleep(2)

        else:
            print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")
