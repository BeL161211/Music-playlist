from tools import dowload_image, dowload_lyrics
import requests
import os
from dotenv import load_dotenv
import argparse


def get_song_by_author_id(api_key,id):
    url = f'https://api.genius.com/artists/{id}/songs'


    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    geniuses = response.json()["response"]["songs"]

    for genius in geniuses:
        title = genius["title"]
        artist_name = genius["artist_names"]
        text_url = genius["url"]
        image_url = genius["header_image_url"]
        release_date = genius["release_date_for_display"]

        dowload_image(artist_name,image_url)
        dowload_lyrics(artist_name,text_url)

        print(f"\nНазвание: {title}\nМузыкант: {artist_name}\nСсылка на текст: {text_url}\nСсылка на изображения: {image_url}\nДата выхода: {release_date}")

def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    parser = argparse.ArgumentParser(description="Находит и скачивает все картинки и тексты по общему id авторов")

    parser.add_argument("-d", "--id", help="2152955",type=int,required=True)
    args = parser.parse_args()

    get_song_by_author_id(api_key,args.id)


if __name__ == "__main__":
    main()