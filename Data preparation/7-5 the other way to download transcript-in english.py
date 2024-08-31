
import requests
import re
import html

# URL of the TED talk transcript
#url = 'https://www.ted.com/talks/stephen_burt_why_people_need_poetry/transcript'
url = 'https://www.ted.com/talks/larry_irvin_a_program_to_empower_black_teachers_in_the_us/transcript?subtitle=en'
# Sending the HTTP GET request
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Getting the text content of the response
    transcript_text = response.text

    # Using regular expression to match the transcript field
    match = re.search(r'"transcript":"([^"]+)"', transcript_text)
    if match:
        # Unescaping HTML entities to convert them into characters
        transcript_content = html.unescape(match.group(1))
        print(transcript_content)
    else:
        print("Transcript not found in the page.")
else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")
