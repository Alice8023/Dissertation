# import requests
# from bs4 import BeautifulSoup
#
# # 设置第一页的URL
# url = "https://www.ted.com/talks/quick-list?page=1"
#
# # 发送请求并获取页面内容
# response = requests.get(url)
#
# if response.status_code == 200:
#     # 创建BeautifulSoup对象
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # 提取所有演讲信息块
#     talk_blocks = soup.find_all('div', class_='col xs-12 quick-list__container-row')
#
#     # 遍历每个演讲块并提取信息
#     for talk_block in talk_blocks:
#         partial_link = talk_block.select_one('.col-xs-6.title a')['href']
#         title = talk_block.select_one('.col-xs-6.title a').text.strip()
#         event = talk_block.select_one('.col-xs-2.event a').text.strip()
#
#         # 提取Published信息
#         published_span = talk_block.select_one('.col-xs-1 span.meta')
#         published = published_span.get_text(strip=True) if published_span else 'N/A'
#
#         # 提取下载链接信息
#         download_links = talk_block.select('.quick-list__download a')
#         download_dict = {link.text.strip(): link['href'] for link in download_links}
#
#         # 构建Modified_Link_transcript
#         modified_link_transcript = f"https://www.ted.com{partial_link}/transcript"
#
#         # 打印提取到的信息
#         print(f"Title: {title}")
#         print(f"Partial Link: {partial_link}")
#         print(f"Event: {event}")
#         print(f"Published: {published}")
#         print(f"Download Link (Low): {download_dict.get('Low', 'N/A')}")
#         print(f"Download Link (Medium): {download_dict.get('Medium', 'N/A')}")
#         print(f"Download Link (1080p): {download_dict.get('1080p', 'N/A')}")
#         print(f"Modified_Link_transcript: {modified_link_transcript}")
#         print('-' * 40)  # 分隔线
#
# else:
#     print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")



import requests

# 设置第一页的URL
# url = "https://www.ted.com/talks/quick-list?page=1"
#url = "https://www.ted.com/talks/isaac_saul_3_ideas_for_communicating_across_the_political_divide/transcript"
url = "https://www.ted.com/talks/bilal_bomani_plant_fuels_that_could_power_a_jet/transcript"
# 发送请求并获取页面内容
response = requests.get(url)

if response.status_code == 200:
    # 打印整个HTML页面内容
    print(response.text)
else:
    print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")
