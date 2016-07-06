import urllib
from urllib2 import Request, urlopen, URLError
import json
import pandas as pd

genre = []
plot = []
ratings = []
def get_ratings(title):
    omdb_request = Request('http://www.omdbapi.com/?t='+urllib.quote_plus(title)+'&y=&plot=short&r=json')
    response = urlopen(omdb_request)
    data = response.read()
    d=json.loads(data)
    if 'False' in data:
        message = "No such movie"
        genre.append(message)
        plot.append(message)
        ratings.append(message)
           
    else:
        genre.append(d['Genre'])
        plot.append(d['Plot'])
        ratings.append(d['imdbRating'])
    
get_ratings('toy story')
get_ratings('titanic')
get_ratings('prachi')

df = pd.DataFrame({'Genre': genre, 'Plot': plot, 'Ratings': ratings})

df.to_excel('movies.xls', sheet_name='sheet1', index=False)
    


