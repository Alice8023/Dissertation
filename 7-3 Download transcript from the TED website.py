#7-Download transcript from the TED website and save the download link 2
# Get 'Modified_Link_transcript' transcript url link from "ted_crawl_official_list.csv"
# Download the transcript first
# If the video has transcript, then check whether it has [low quality download link].
# If it has the [low quality download link], then save the talk_id(partial link) and [low quality download link] to csv file
import pandas as pd
import requests
import re
import html
from langdetect import detect, DetectorFactory
import os
import random
from urllib.parse import urlparse
import time

# Set seed to ensure repeatable results
DetectorFactory.seed = 0

# Load URLs and related columns from CSV file
def load_urls_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df[['Modified_Link_transcript', 'Download Link (Low)']]

# Check if the URL exists
def check_url_exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking URL: {e}")
        return False

# Fetch webpage content
def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        response.raise_for_status()

# Detect the language of the text
def detect_language_of_text(text):
    return detect(text)

# Extract transcript text from the HTML content using regex
def extract_transcript_from_html(html_content):
    # Using regex to match the transcript field
    match = re.search(r'"transcript":"([^"]+)"', html_content)
    if match:
        # Unescaping HTML entities to convert them into characters
        return html.unescape(match.group(1))
    return None

# Save text to a file
def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Extract talk_id from URL
def get_talk_id(url):
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.split('/')
    for segment in path_segments:
        if segment == 'talks':
            talk_id_index = path_segments.index('talks') + 1
            return path_segments[talk_id_index]
    return None

# Process a single URL
def process_webpage(url, save_dir, talk_id, download_link, downloaded_links):
    if check_url_exists(url):
        try:
            html_content = fetch_webpage(url)
            transcript_content = extract_transcript_from_html(html_content)
            if transcript_content:
                language = detect_language_of_text(transcript_content)
                if language == 'en':
                    if talk_id:
                        file_path = os.path.join(save_dir, f"{talk_id}.txt")
                        save_text_to_file(transcript_content, file_path)
                        # Add to downloaded links list
                        downloaded_links.append({'talk_id': talk_id, 'download_link': download_link})
                        return True
        except Exception as e:
            print(f"An error occurred: {e}")
    return False

# Main function
def main():
    csv_file = '/Users/alicezhang/Downloads/Wget/ted-talks-download-master/src/video_name/ted_crawl_official_list.csv'
    save_dir = 'TED_transcript_from_official'
    output_file = 'ted_downloaded_link_add2.csv'

    # Create directory to save files (if it doesn't exist)
    os.makedirs(save_dir, exist_ok=True)

    # Read data
    df = load_urls_from_csv(csv_file)
    urls = df['Modified_Link_transcript'].tolist()
    download_links = df['Download Link (Low)'].tolist()

    # Create a list to save results
    downloaded_links = []

    # Shuffle URL list randomly
    combined = list(zip(urls, download_links))
    random.shuffle(combined)
    urls, download_links = zip(*combined)

    valid_count = 0

    for url, download_link in zip(urls, download_links):
        if valid_count >= 20:
            break
        if pd.notna(download_link):  # Ensure "Download Link (Low)" is not empty
            talk_id = get_talk_id(url)  # Extract talk_id
            if process_webpage(url, save_dir, talk_id, download_link, downloaded_links):
                valid_count += 1
                print(f"Processed {valid_count} URLs successfully")
            time.sleep(2)  # Rest for 2 seconds after each process

    # Write results to CSV file
    pd.DataFrame(downloaded_links).to_csv(output_file, index=False)
    print("Completed processing 200 URLs and saved results to ted_downloaded_link.csv.")

if __name__ == "__main__":
    main()
