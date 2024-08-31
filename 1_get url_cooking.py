# Download first 200 url in the "David Seymour-buzzfeeds test" channel playlist, he taught people how to cook
# video length around 5 minutes
import csv
from pytube import Playlist

# Define the URL of the playlist
playlist_url = 'https://www.youtube.com/playlist?list=PLuocqDUAmsKVm5RasiR_-KCJePSGmDP9Y'

# Create a Playlist object
p = Playlist(playlist_url)

# Open a CSV file in write mode
with open('youtube_cooking_urls.csv', 'w', newline='', encoding='utf-8') as csvfile:
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
        if count >= 205:
            break

print("CSV file with the first 200 YouTube URLs has been created.")

