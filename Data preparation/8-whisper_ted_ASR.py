
#from 6-whisper-ASR_ordered.py code

import whisper
import os

# Load the Whisper model
model = whisper.load_model("base")

# Path to the directory containing video files
videos_directory = "/Users/alicezhang/Downloads/pythonProject5/Download_and_ASR/TED_video_from_official22"

# Check if the video directory exists
if not os.path.exists(videos_directory):
    print(f"Error: Videos directory '{videos_directory}' not found.")
    exit()

# Directory to save the transcribed text files
output_directory = "/Users/alicezhang/Downloads/pythonProject5/Download_and_ASR/TED_video_from_official22_ASR"

# Ensure the output directory exists, create it if it doesn't
os.makedirs(output_directory, exist_ok=True)

# Supported video file extensions
video_extensions = {'.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv'}

# Loop through each file in the directory
for video_file in os.listdir(videos_directory):
    # Construct the full path to the file
    video_file_path = os.path.join(videos_directory, video_file)

    # Get the file extension
    file_extension = os.path.splitext(video_file_path)[1].lower()

    # Skip files that are not video files
    if file_extension not in video_extensions:
        print(f"Skipping non-video file: {video_file}")
        continue

    # Get the base name of the video file (without path and extension)
    video_base_name = os.path.splitext(os.path.basename(video_file_path))[0]

    # Dynamically generate the name for the output text file
    output_filename = f"{video_base_name}.txt"

    # Full path to the output text file
    output_file_path = os.path.join(output_directory, output_filename)

    try:
        # Transcribe the video file using the Whisper model
        result = model.transcribe(video_file_path)

        # Extract the transcribed text and detected language
        transcription_text = result["text"]
        detected_language = result["language"]

        # Print the detected language to the terminal
        print(f"Detected language for {video_file}: {detected_language}")

        # Write the transcribed text to the output file
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(transcription_text)

        # Print a message indicating the transcription was saved successfully
        print(f"Transcription for {video_file} saved to {output_file_path}")

    except Exception as e:
        print(f"Error transcribing {video_file}: {e}")
