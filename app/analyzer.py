import requests

# API_URL = ""
headers = {
    "Authorization": "Bearer {your_secret_key}}",
    "Content-Type": "image/jpeg"
}

def analyze_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()

    response = requests.post(API_URL, headers=headers, data=data)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code != 200:
        raise Exception("Failed to analyze image.")

    return response.json()  # This will return a list like: [{'label': '...', 'score': ...}]
