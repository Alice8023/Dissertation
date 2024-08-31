
import os
import csv
import yt_dlp

def download_video(video_url, output_dir):
    # Create an instance of yt-dlp with options
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Save in output_dir with video title as filename
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        video_title = info_dict.get('title', None)  # Get video title from info dictionary

    print(f"Video downloaded successfully: {video_title}")

def main():
    csv_file = 'youtube_irish_news_urls.csv'
    output_dir = 'Irish_news'

    # Check if output directory exists, create if not
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Directory '{output_dir}' created.")

    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if exists
        for row in csv_reader:
            url = row[0].strip()  # Assuming URL is in the first column; strip whitespace
            download_video(url, output_dir)

if __name__ == "__main__":
    main()
