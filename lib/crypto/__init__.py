from . import coindesk, coinmarketcap
import requests, slugify
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def _get_abbreviations(url='https://www.ifcmarkets.com/en/cryptocurrency-abbreviations'):
	res = requests.get(url)
	html = BeautifulSoup(res.content, features="lxml")
	tdata = html.find(id='equities_table').select('tbody')[0].select('td')
	table = pd.DataFrame(np.array(list(map(lambda x:x.text.strip(), tdata))).reshape(49,3), columns=['name', 'ticker', 'symbol'])
	table['slug'] = table['name'].apply(slugify.slugify)
	return table

table = _get_abbreviations()
slug_to_ticker = lambda slug:table[table['slug']==slug].ticker.values[0]
ticker_to_slug = lambda ticker:table[table['ticker']==ticker].slug.values[0]