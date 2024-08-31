import os
import re

def remove_special_characters(text):
    # Define a regular expression to match non-alphanumeric and non-underscore characters,
    # replacing them with an empty string
    return re.sub(r'[^\w\s]', '', text)

def rename_videos(folder_path):
    # Get all filenames in the specified folder
    files = os.listdir(folder_path)

    for filename in files:
        # Check if the file is a video file; you can extend this to support more formats as needed
        if filename.endswith(('.mp4', '.mov')):
            old_filepath = os.path.join(folder_path, filename)
            # Remove special characters from the filename
            parts = filename.split(".mp4")
            if len(parts) > 1:
                new_filename = remove_special_characters(parts[0]) + ".mp4"
            else:
                new_filename = remove_special_characters(filename)

            new_filepath = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed file: {filename} -> {new_filename}")

# Specify the path of the folder where the files need to be renamed
folder_path = 'abcnews'

# Call the function to rename files
rename_videos(folder_path)
