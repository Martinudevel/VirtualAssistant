import requests

# Endpoint și API Key
endpoint = "" # insert the provided endpoint here
api_key = "" # insert the provided api key here
import requests

# Define headers and parameters
headers = {
    "api-key": api_key
}

# Load the audio file and send as form-data
audio_file_path = 'audio.wav'
with open(audio_file_path, 'rb') as audio_file:
    files = {
        "file": ("audio.wav", audio_file, "audio/wav")
    }
    response = requests.post(url=endpoint, headers=headers, files=files)

# Analyze the response
if response.status_code == 200:
    transcription = response.json()
    print("Transcription:", transcription)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)