
import pandas as pd
import requests
import os

# Read the CSV file
file_path = '/Users/alicezhang/Downloads/pythonProject5/Download_and_ASR/ted_downloaded_link_add2.csv'
df = pd.read_csv(file_path)

# Set the target folder for downloading files
download_folder = os.path.expanduser('/Users/alicezhang/Downloads/pythonProject5/Download_and_ASR/TED_video_from_official22')

for index, row in df.iterrows():
    # Get the download link and talk ID from each row
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
