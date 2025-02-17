import urllib.request 
from PIL import Image 
import html
import os
import json
import re

output_folder = "app_data"

# Create the folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

with open('output.json', 'r') as file:
    json_data = json.load(file)

def clean_text(text):
    text = text.encode("utf-8", "ignore").decode("utf-8")
    text = re.sub(r'[^\x20-\x7E\n]', '', text)
    return text

count = 0

for item in json_data:
    if count > 10000:
        break
    img_path = os.path.join(output_folder, f"app{count}.png")
    text_path = os.path.join(output_folder, f"app{count}.txt")
    try:
        urllib.request.urlretrieve(item.get('icon'), img_path) 
        title = clean_text(item.get("title"))
        # Save formatted text file
        with open(text_path, "w") as file:
            file.write(title)
        print(title)
    except:
        print("didn't add!")
    count += 1
print(count)