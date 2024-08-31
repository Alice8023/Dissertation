import requests

# Set the URL for the first page
# url = "https://www.ted.com/talks/quick-list?page=1"
# url = "https://www.ted.com/talks/isaac_saul_3_ideas_for_communicating_across_the_political_divide/transcript"
url = "https://www.ted.com/talks/bilal_bomani_plant_fuels_that_could_power_a_jet/transcript"

# Send a request and retrieve the page content
response = requests.get(url)

if response.status_code == 200:
    # Print the entire HTML content of the page
    print(response.text)
else:
    print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")
