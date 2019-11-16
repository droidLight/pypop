from googlesearch import search

def __parse(imdb_url):

    id = None
    success = False
    for i in range(len(imdb_url) - 2, 0, -1):
        if imdb_url[i] == '/':
            id = imdb_url[i + 1:len(imdb_url) -1]
            success = True
            break
    if success:
        return id
    else:
        return None

def get_title(film_name):
    title = None
    film_name = 'IMDB ' + film_name
    for results in search(query = film_name, tld = 'com', num = 1, stop = 1, pause = 1):
        title = __parse(results)
        
    return title

