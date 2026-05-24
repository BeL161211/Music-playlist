from tools import dowload_image, dowload_lyrics
import requests
import os
from dotenv import load_dotenv
import argparse


def get_song_by_author_name(api_key,authorname):
    url = 'https://api.genius.com/search'

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    params ={
        "q": f"{authorname}"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    song_info = response.json()["response"]["hits"]

    for song in song_info:
        title = song["result"]["title"]
        artist_names = song["result"]["artist_names"]
        song_lyric = song["result"]["url"]
        song_image = song["result"]["song_art_image_url"]
        release_date = song["result"]["release_date_for_display"]

        dowload_image(artist_names,song_image)
        dowload_lyrics(artist_names,song_lyric)

        print(f"\nНазвание: {title}\nМузыкант: {artist_names}\nСсылка на текст: {song_lyric}\nСсылка на изображение: {song_image}\nДата выхода: {release_date}")


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    parser = argparse.ArgumentParser(description="Находит информацию на сайте genius по имени и скачивает тексты и картинки песен")

    parser.add_argument("-n", "--authorname", help="Gazan",type=str,required=True)
    args = parser.parse_args()

    get_song_by_author_name(api_key,args.authorname)


if __name__ == "__main__":
    main()