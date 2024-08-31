import whisper
import os

# Convert video to text
# Load the model
model = whisper.load_model("base")

# Path to the video files directory
videos_directory = "abcnews"

# Check if the video directory exists
if not os.path.exists(videos_directory):
    print(f"Error: Videos directory '{videos_directory}' not found.")
    exit()

# Loop through each video file in the directory
for video_file in os.listdir(videos_directory):
    # Construct the full path to the video file
    video_file_path = os.path.join(videos_directory, video_file)

    # Use the transcribe method to get the result
    result = model.transcribe(video_file_path)

    # Extract the transcription text
    transcription_text = result["text"]

    # Get the base name of the video file (without path and extension)
    video_base_name = os.path.splitext(os.path.basename(video_file_path))[0]

    # Dynamically generate the txt filename
    output_filename = f"{video_base_name}.txt"

    # Specify the directory to save the txt file
    output_directory = "abcnews_ASR"

    # Ensure the directory exists; create it if it doesn't
    os.makedirs(output_directory, exist_ok=True)

    # Full path to the txt file
    output_file_path = os.path.join(output_directory, output_filename)

    # Write the transcription text to the txt file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(transcription_text)

    # Print a success message
    print(f"Transcription for {video_file} saved to {output_file_path}")
