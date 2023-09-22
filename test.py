import requests
import json

# GitHub raw JSON file URL
github_json_url = "https://raw.githubusercontent.com/your_username/your_repository/master/your_file.json"

# Send a request to download the JSON file
response = requests.get(github_json_url)

# Check if the request was successful
if response.status_code == 200:
  # Parse the JSON data
  json_data = json.loads(response.text)

  # Access the data in the JSON file
  # For example, if the JSON structure is a dictionary:
  # Access a specific key in the JSON data
  print("Value of key 'example_key':", json_data.get("example_key"))
else:
  print("Failed to retrieve the JSON file. Status code:", response.status_code)
  input()
  exit()
