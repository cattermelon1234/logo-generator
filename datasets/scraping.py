from google_play_scraper import app, search, Sort, reviews_all
from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import json, os, uuid
import kagglehub
import re

# Download latest version
path = kagglehub.dataset_download("lava18/google-play-store-apps")
print(os.listdir(path))
csv_file = os.path.join(path, "googleplaystore.csv")
app_df = pd.read_csv(csv_file)
overall_json = []
app_names = app_df["App"]
app_name_list = [x for x in app_names if x != None]
categories = [
    "Business",
    "Communication",
    "Education",
    "Entertainment",
    "Finance",
    "Health & Fitness",
    "Lifestyle",
    "Maps & Navigation",
    "Medical",
    "Music & Audio",
    "News & Magazines",
    "Personalization",
    "Photography",
    "Productivity",
    "Shopping",
    "Social",
    "Sports",
    "Tools",
    "Travel & Local",
    "Weather",
    "Auto & Vehicles",
    "Beauty",
    "Books & Reference",
    "Comics",
    "Dating",
    "Events",
    "Food & Drink",
    "House & Home",
    "Libraries & Demo",
    "Parenting",
    "Video Players & Editors"
]

def get_apps_by_category(name, num_results=1):
    try:
        results = search(
            name,
            lang="en",  # Language
            country="us",  # Country
        )
        return results
    except:
        return -1

for name in app_name_list:
    print(name)
    cur = get_apps_by_category(name, num_results=1)
    if cur != -1:
        for app in cur:
            entry = {
                "title": app['title'],
                'icon': app['icon']
            }
            overall_json.append(entry)

with open("output.json", "w") as f:
    json.dump(overall_json, f, indent=4)