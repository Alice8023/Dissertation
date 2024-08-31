import csv
import os
import pytube

def download_video(url):
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.first()
        if stream:
            # Create NBA directory if it doesn't exist
            if not os.path.exists('Vlog'):
                os.makedirs('Vlog')
            # Download video to NBA directory
            stream.download(output_path='Vlog')
            print('Downloaded:', yt.title)
        else:
            print('No streams available for this video:', url)
    except pytube.exceptions.RegexMatchError:
        print('Invalid YouTube URL:', url)
    except pytube.exceptions.VideoUnavailable:
        print('This video is unavailable:', url)
    except Exception as e:
        print('An error occurred while downloading', url, ':', e)

# CSV file containing YouTube URLs
csv_file = 'youtube_Vlog_urls.csv'

# Download each video from URLs in the CSV file
with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row if exists
    for row in csv_reader:
        url = row[0]  # Assuming URL is in the first column
        download_video(url)
