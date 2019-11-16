import requests as rq
import json


class Movie:
    BASE_URL = "https://tv-v2.api-fetch.website/"
    title, imdb_id, synopsis, year, torrents = None, None, None, None, None

    def __init__(self, IMDB_ID):
        if IMDB_ID != None:
            
                URL = self.BASE_URL + "movie/" + IMDB_ID
                response = rq.get(url = URL)
                try:
                    json_data = response.json()
                except:
                    raise MovieNotFound
                
                self.title = json_data['title']
                self.imdb_id = json_data['imdb_id']
                self.synopsis = json_data['synopsis']
                self.year = json_data['year']
                self.torrents = json_data['torrents']

    def __display_torrent(self):
        for key in self.torrents.keys():
            print("Language: "+str(key))
            lang = self.torrents[key]

            for lang_key in lang.keys():
                print("\n\n"+str(lang_key))
                quality = lang[lang_key]

                print("\nurl: "+quality['url'])
                print("\nFile size: "+quality['filesize'])
                print("\nprovider: "+quality['provider'])


    def display_details(self):
        print(f"\nTitle: {self.title}\nIMDB_ID: {self.imdb_id}")
        print(f"Year: {self.year}")
        print(f"Synopsis:\n{self.synopsis}\n")
        self.__display_torrent()


class MovieNotFound(Exception):
    pass