from openai import AzureOpenAI
        
client = AzureOpenAI(
    api_key="", # insert the provided api key here
    api_version="2024-02-01",
    azure_endpoint = "" # insert the provided endpoint here
)

deployment_id = "whisper"
audio_test_file = "audio.wav"

result = client.audio.transcriptions.create(
    file=open(audio_test_file, "rb"),            
    model=deployment_id
)

print(result)