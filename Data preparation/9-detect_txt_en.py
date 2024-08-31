import os
from langdetect import detect

def check_language(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            lang = detect(text)
            return lang == 'en'
    except Exception as e:
        print(f"An error occurred with file {file_path}: {e}")
        return False

def check_directory(directory_path):
    non_english_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                if not check_language(file_path):
                    non_english_files.append(file)
    return non_english_files


directory_path = 'TED_video_from_official_ASR'
non_english_files = check_directory(directory_path)

if non_english_files:
    print("The following files are not in English:")
    for file in non_english_files:
        print(file)
else:
    print("All files are in English.")
