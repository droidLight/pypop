import requests as req
import json


class Show:
    BASE_URL = "https://tv-v2.api-fetch.website/"
    title, imdb_id, synopsis, year, seasons = None, None, None, None, {}
    num_episodes, num_seasons = None, None

    def sort_episodes(self, episode_list, num_seasons):
        for i in range(0, num_seasons):
            self.seasons['season' + str(i + 1)] = list()
        
        for episode in episode_list:
            enum = str(episode['season'])
            self.seasons['season' + enum].append(episode)
            sorted(self.seasons['season' + enum], key = lambda i : int(i['episode']))


    def __init__(self, IMDB_ID):
        if IMDB_ID == None:
            print('IMDB ID NULL')
        URL = self.BASE_URL + "show/" + IMDB_ID

        try:
            response = req.get(url = URL)
            json_data = response.json()
            
            self.title = json_data['title']
            self.imdb_id = json_data['imdb_id']
            self.synopsis = json_data['synopsis']
            self.year = json_data['year']
            self.sort_episodes(json_data['episodes'], json_data['num_seasons'])
        except Exception as e:
            print("Error calling the API \n",e)

    
    def display_episode_details(self, season_num, episode_num):
        try:
            episode_list = self.seasons['season'+str(season_num)]
        except:
            raise InvalidSeason
        try:
            episode = episode_list[episode_num - 1]
        except:
            raise InvalidEpisode
        print(f"\nSeason: {season_num} Episode: {episode_num}")
        print(f"\nTitle: {episode['title']}")
        print(f"Overview: {episode['overview']}")
        print("Torrents: ")
        torrents = episode['torrents']
        for key in torrents.keys():
            print("\n"+str(key))
            print(f"Magnet url:{torrents[str(key)]['url']}")


    def display_season_details(self, season_num):
        try:
            episode_list = self.seasons['season'+str(season_num)]
            for episode in episode_list:
                print("\nEpisode "+str(episode['episode']))
                print("Title: "+str(episode['title']))
        except:
            raise InvalidSeason


    def display_show_details(self):
        print(f"\nTitle: {self.title}\nIMDB_ID: {self.imdb_id}")
        print(f"Year: {self.year}")
        print(f"Synopsis:\n{self.synopsis}\n")
        print("Available Seasons:")
        for i in range(len(self.seasons.keys())):
            print("Season"+str(i+1))
            print("Episodes: "+str(len(self.seasons["season"+str(i+1)])))

class ShowNotFound(Exception):
    pass
class InvalidSeason(Exception):
    pass
class InvalidEpisode(Exception):
    pass