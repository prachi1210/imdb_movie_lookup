import urllib
from urllib2 import Request, urlopen, URLError
import json
import pandas as pd
import os
import requests
from lxml import html

movie_names = []
genre = []
plot = []
ratings = []

def get_imdb_id(input):
    """Function to get imdb id from input file name"""
    query = urllib.quote_plus(input)
    url = "http://www.imdb.com/find?ref_=nv_sr_fn&q="+query+"&s=all"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    if"No results" in (tree.xpath('//h1[@class="findHeader"]/text()')[0]):
        imdb_id = "tt00000"
    else:
        imdb_id=(tree.xpath('//td[@class="result_text"]//a')[0].get('href'))
        imdb_id = imdb_id.replace('/title/','')
        imdb_id = imdb_id.replace('/?ref_=fn_al_tt_1','')
    return (imdb_id)

def get_info(id):  
    """Function to get genre, plot and ratings from imdb id"""
    omdb_request = Request('http://www.omdbapi.com/?i='+id+'&y=&plot=short&r=json')
    response = urlopen(omdb_request)
    data = response.read()
    d=json.loads(data)
    if 'False' in data:
        message = "No results found"
        genre.append(message)
        plot.append(message)
        ratings.append(message)
           
    else:
        genre.append(d['Genre'])
        plot.append(d['Plot'])
        ratings.append(d['imdbRating'])

for file in os.listdir("H:\DS LAB\Movies - aloo"):
    print(file)   
    get_info(get_imdb_id(file))
    movie_names.append(file)
    
df = pd.DataFrame({'Genre': genre, 'Plot': plot, 'Ratings': ratings})
df.to_excel('movies.xls', sheet_name='sheet1', index=False)
    


