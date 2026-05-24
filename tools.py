import os
from pathlib import Path
from sanitize_filename import sanitize
from bs4 import BeautifulSoup
import requests


def dowload_image(artist_name,image_url):
    folder_path = f"songs/{artist_name}/images"
    os.makedirs(folder_path,exist_ok=True)  
    extention = Path(image_url).suffix
    file_name = sanitize(f"{artist_name}{extention}")
    file_path = os.path.join(folder_path, file_name)

    response = requests.get(image_url)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def dowload_lyrics(artist_name,text_url):
    folder_path = f"songs/{artist_name}/lyrics"
    os.makedirs(folder_path,exist_ok=True)
    file_name = sanitize(f"{artist_name}.txt")
    file_path = os.path.join(folder_path, file_name)

    response = requests.get(text_url)
    bs = BeautifulSoup(response.text,"lxml")

    lyrics = bs.find('div', 'Lyrics__Container-sc-c1895f55-1')
    lyrics.find("div", "LyricsHeader__Container-sc-347d044d-1").decompose()
    lyrics = lyrics.get_text(separator="\n")

    with open(file_path, 'w', encoding="UTF-8") as file:
        file.write(lyrics)