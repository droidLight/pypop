# pypop
ONLY FOR LEARNING PURPOSE
CLI client for acessing torrents of movies and tv shows.Uses popcorntime API.
Install the dependencies by (for python3) pip3 install -r requirements.txt (for python2) pip install -r requirements.txt

python3 pypop.py -h 

usage: pypop.py [-h] -m MEDIA_TYPE -n NAME [-s SEASON_NUM] [-e EPISODE_NUM]

CLI for searching torrent links for Movies, Shows, Anime Series

optional arguments:
-h, --help\n            
show this help message and exit\n

-m MEDIA_TYPE, --media_type MEDIA_TYPE\n    
Type of Media you are looking for valid values are(movie, series, show)\n
                                     
-n NAME, --name NAME\n  
Name of the movie/show/series\n
  
-s SEASON_NUM, --season_num SEASON_NUM\n    
Season number of the show.\n
                        
                        
-e EPISODE_NUM, --episode_num EPISODE_NUM\n   
Episode number of the season of the show\n
                        

To view all the Episodes of a season give just the season number.To get
detailed view of the episode give the season number and episode number.

