import imdb_id
import show_api, movie_api
import argparse
import urllib

my_arg = argparse.ArgumentParser(description = 'CLI for searching torrent links for Movies, Shows, Anime Series', epilog = 'To view all the Episodes of a season give just the season number.To get detailed view of the episode give the season number and episode number.')

my_arg.add_argument('-m', '--media_type', required = True, help = 'Type of Media you are looking for valid values are (movie, series, show)')
my_arg.add_argument('-n', '--name', required= True, help = 'Name of the movie/show/series')
my_arg.add_argument('-s', '--season_num',type = int, required = False, help = 'Season number of the show.')
my_arg.add_argument('-e', '--episode_num', type = int, required = False, help = 'Episode number of the season of the show')

args = vars(my_arg.parse_args())
#title = 'tt4154796'
try:
    title = imdb_id.get_title(args['name'])

    if args['media_type'] == 'movie':
        movie = movie_api.Movie(title)
        movie.display_details()

    elif args['media_type'] == 'show':
        show = show_api.Show(title)
        show.display_show_details()
        if args['season_num'] > 0 and args['episode_num'] != None:
            show.display_episode_details(args['season_num'], args['episode_num'])

        elif args['season_num'] > 0 and args['episode_num'] == None:
            show.display_season_details(args['season_num'])

        else:
            print("Enter valid Season number and episode number")
            
    elif args['media_type'] == 'series':
        print("series coming soon")

    else:
        print("Invalid")

except Exception as e:
    if type(e) == urllib.error.URLError or type(e) == show_api.req.exceptions.ConnectionError:
        print("\nNo Connection")
    if type(e) == movie_api.MovieNotFound:
        print("\nMovie not found")
    if type(e) == show_api.ShowNotFound:
        print("\nShow not Found")
    if type(e) == show_api.InvalidEpisode:
        print("\nEpisode not found")
    if type(e) == show_api.InvalidSeason:
        print("\nSeason not found")


    