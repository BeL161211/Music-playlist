import requests
import os
from tools import dowload_image, dowload_lyrics
from dotenv import load_dotenv
import argparse


def get_song_by_song_id(api_key,id):
    url = f'https://api.genius.com/songs/{id}'

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    song_info = response.json()["response"]["song"]

    title = song_info["title"]
    artist_names = song_info["artist_names"]
    song_lyric = song_info["url"]
    song_image = song_info["song_art_image_url"]
    release_date = song_info["release_date_for_display"]

    dowload_image(artist_names,song_image)
    dowload_lyrics(artist_names,song_lyric)

    print(f"Название: {title}\nМузыкант: {artist_names}\nСсылка на текст: {song_lyric}\nСсылка на изображение: {song_image}\nДата выхода: {release_date}")


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    parser = argparse.ArgumentParser(description="Находит информацию на сайте genius по id и скачивает картинки с текстами")

    parser.add_argument("-d", "--id", help="13135540",type=int,required=True)
    args = parser.parse_args()
    get_song_by_song_id(api_key,args.id)


if __name__ == "__main__":
    main()