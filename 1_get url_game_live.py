# Download first 200 url in the "Fox News-Tucker Carlson Tonight" channel playlist
# video length around 3-5 minutes
import csv
from pytube import Playlist

# Define the URL of the playlist
#playlist_url = 'https://www.youtube.com/playlist?list=PLlTLHnxSVuIzrARlmz9oCfQEF08UV-v-E'
#playlist_url = 'https://www.youtube.com/playlist?list=PLQOa26lW-uI8ZFnCrPVv25OUPMmPyhdi7'

#Sniper Roulette 198
#playlist_url = 'https://www.youtube.com/playlist?list=PL5E111114D40C5AD2'
#Swiftor Says
playlist_url = 'https://www.youtube.com/playlist?list=PL5r-ii6ChwOiWe4j9bTt70-KiymKuAU1l'
# Create a Playlist object
p = Playlist(playlist_url)

# Open a CSV file in write mode
with open('youtube_game_live3_urls.csv', 'w', newline='', encoding='utf-8') as csvfile:
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
        if count >= 220:
            break

print("CSV file with the first 220 YouTube URLs has been created.")

