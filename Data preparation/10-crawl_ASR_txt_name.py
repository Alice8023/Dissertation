import os
import csv

def get_txt_filenames(folder_path):

    filenames = []
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            filenames.append(os.path.splitext(file)[0])
    return filenames

def write_to_csv(filenames, csv_path):

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for filename in filenames:
            writer.writerow([filename])

# Usage example
folder_path = 'TED_video_from_official_ASR'  # Replace with your folder path
csv_path = 'TED_video_from_official_ASR_name.csv'  # Replace with your desired CSV file path

# Get the list of txt filenames
filenames = get_txt_filenames(folder_path)

# Write the filenames to the CSV file
write_to_csv(filenames, csv_path)

print(f"{len(filenames)} filenames have been written to {csv_path}")
