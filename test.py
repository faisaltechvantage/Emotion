import requests

API_URL = "https://api-inference.huggingface.co/models/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"
headers = {"Authorization": "Bearer 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"}
# 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

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("03-01-01-01-01-01-01.wav")

print(output)