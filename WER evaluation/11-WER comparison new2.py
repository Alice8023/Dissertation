
# Remove parentheses content
# Remove square brackets content
# Remove names
# Remove dashes
# Remove ordinary punctuation
# Remove extra spaces


import pandas as pd
import re
import os
import string
#import html

def wer(reference, hypothesis):
    r = reference
    h = hypothesis
    d = [[0] * (len(h) + 1) for _ in range(len(r) + 1)]
    for i in range(len(r) + 1):
        for j in range(len(h) + 1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            else:
                substitution_cost = 0 if r[i - 1] == h[j - 1] else 1
                d[i][j] = min(d[i - 1][j] + 1,  # deletion
                              d[i][j - 1] + 1,  # insertion
                              d[i - 1][j - 1] + substitution_cost)  # substitution
    return float(d[len(r)][len(h)]) / len(r)


def remove_bracketed_content(transcript):

    transcript = re.sub(r'\([^)]*\)', '', transcript)  # Remove parentheses content
    transcript = re.sub(r'\[[^\]]*\]', '', transcript)  # Remove square brackets content
    transcript = re.sub(r'^[A-Za-z\s]+:', '', transcript, flags=re.MULTILINE)  # Remove names
    transcript = re.sub(r'--', '', transcript)  # Remove dashes
    transcript = transcript.translate(str.maketrans('', '', string.punctuation)) # Remove ordinary punctuation
    transcript = ' '.join(transcript.split())  # Remove extra spaces
    return transcript


def read_transcript_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Remove unwanted content
        content = remove_bracketed_content(content)
        # Split content into words
        words = content.split()
        return words


# Path to the CSV file
csv_path = "/Users/alicezhang/Downloads/pythonProject5/Download_and_ASR/TED_video_from_official_ASR_name.csv"
df = pd.read_csv(csv_path, header=None)  # Read CSV without header

# List to store results
results = []

# Iterate over each row in the CSV file
for index, row in df.iterrows():
    file_name = row[0]  # Directly extract from the first column

    # Construct file paths for reference and hypothesis
    reference_file_path = f"/Users/alicezhang/Downloads/pythonProject5/Download_and_ASR/TED_transcript_from_official/{file_name}.txt"
    hypothesis_file_path = f"/Users/alicezhang/Downloads/pythonProject5/Download_and_ASR/TED_video_from_official_ASR/{file_name}.txt"

    try:
        # Read reference and hypothesis file contents
        reference = read_transcript_file(reference_file_path)
        hypothesis = read_transcript_file(hypothesis_file_path)

        # Calculate WER
        wer_score = wer(reference, hypothesis)
        results.append({"file name": file_name, "WER": wer_score})
    except FileNotFoundError as e:
        # Handle file not found case
        results.append({"file name": file_name, "WER": "File not found"})
    except Exception as e:
        # Handle other errors
        results.append({"file name": file_name, "WER": f"Error: {str(e)}"})

# Create a DataFrame from results
results_df = pd.DataFrame(results)

# Save results to CSV file
output_csv_path = "WER08062.csv"
results_df.to_csv(output_csv_path, index=False)
print(f"Results saved to {output_csv_path}")
