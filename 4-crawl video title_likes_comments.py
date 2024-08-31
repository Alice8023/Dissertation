import csv
import requests
from pytube import YouTube
import re

# API key
API_KEY = "AIzaSyAQ49KZDgOq9YUdCs8mmiwSxfe_oFogPFI"
API_URL = "https://www.googleapis.com/youtube/v3/videos"

input_file = "youtube_cooking_urls.csv"
output_file = "youtube_cooking_info2.csv"

with open(input_file, 'r', newline='', encoding='utf-8') as csv_in, \
     open(output_file, 'w', newline='', encoding='utf-8') as csv_out:

    reader = csv.reader(csv_in)
    writer = csv.writer(csv_out)

    next(reader)


    writer.writerow(["Video URL", "Title", "Likes Count", "Comment Count"])


    for row in reader:
        video_url = row[0]

        video_id = video_url.split('=')[-1]


        try:
            yt = YouTube(video_url)
            title = yt.title

            title = re.sub(r'[^\w\s]', '', title)
        except Exception as e:
            title = "Error: " + str(e)


        params = {
            'part': 'statistics',
            'id': video_id,
            'key': API_KEY
        }
        response = requests.get(API_URL, params=params)
        data = response.json()


        if 'items' in data and data['items']:
            likes_count = data['items'][0]['statistics'].get('likeCount', 'N/A')
            comment_count = data['items'][0]['statistics'].get('commentCount', 'N/A')
        else:
            likes_count = 'N/A'
            comment_count = 'N/A'


        writer.writerow([video_url, title, likes_count, comment_count])

print("title, like counts and comment counts already save to", output_file)
