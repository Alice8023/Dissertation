# Download first 200 url in the "Warner Bros. Entertainment" channel playlist
# video length around 1-10 minutes
import csv
from pytube import Playlist

# Define the URL of the playlist
playlist_url = 'https://www.youtube.com/playlist?list=UULFgKkNPU2Ib7_TcyAl8M2S-w'

# Create a Playlist object
p = Playlist(playlist_url)

# Open a CSV file in write mode
with open('youtube_movieclips_urls.csv', 'w', newline='', encoding='utf-8') as csvfile:
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
        if count >= 210:
            break

print("CSV file with the first 200 YouTube URLs has been created.")

