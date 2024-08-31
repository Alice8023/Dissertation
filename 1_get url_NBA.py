# Still using pytube, get youtube video url from youtube playlist
# Here is the related example:"https://pytube.io/en/latest/user/playlist.html"

# from pytube import Playlist
# p = Playlist('https://www.youtube.com/playlist?list=PLXlvFN0gKJA4jp9_3mEbUTf-SOmr9YJZK')
#  for url in p.video_urls:# Download all video URLs from playlist
#     print(url)
# for url in p.video_urls[:2]:# Download 2 video URLs from playlist
#     print(url)

# Download first 200 url in the "Hopper highlights" channel playlist
import csv
from pytube import Playlist

# Define the URL of the playlist
playlist_url = 'https://www.youtube.com/playlist?list=PLXlvFN0gKJA4jp9_3mEbUTf-SOmr9YJZK'

# Create a Playlist object
p = Playlist(playlist_url)

# Open a CSV file in write mode
with open('youtube_NBA_urls.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the header
    writer.writerow(['Video URL'])

    # Initialize a counter
    count = 0

    # Iterate through each video URL in the playlist
    for url in p.video_urls:
        # Write the URL to the CSV file
        writer.writerow([url])

        # Increment the counter
        count += 1

        # Check if we have written 200 URLs
        if count >= 200:
            break

print("CSV file with the first 200 YouTube URLs has been created.")

