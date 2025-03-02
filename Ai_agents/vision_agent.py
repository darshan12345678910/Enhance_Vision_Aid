

import requests
image_path = "testing_images\im1.jpg"  
api_key = "bTBwdDMwZ3FuaW5maTZ3Y2E2bmRwOmZOR2k2Wmc2NDd2YWhadzA2VjNyNVh3Z2FHZTR6bUpT"        # Provide your API key
prompt_text =  "Detect objects such as road, obstacles, vehicles, people, and raffic signs."


url = "https://api.landing.ai/v1/tools/agentic-object-detection"

# Open the image file
with open(image_path, "rb") as image_file:
    files = {"image": image_file}
    data = {
        "prompts": prompt_text,
        "model": "agentic"
    }
    headers = {
        "Authorization": f"Basic {api_key}"
    }

    # Send the request
    response = requests.post(url, files=files, data=data, headers=headers)

# Print the response
print(response.json())
