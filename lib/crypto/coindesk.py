import json, requests
from bs4 import BeautifulSoup

def get_price(symbol='BTC', url='https://www.coindesk.com'):
	res = requests.get(f"{url}/price/BTC/")
	if res.ok:
		html = BeautifulSoup(res.content, features="lxml")
		data = html.select(f"#fusion-metadata")[0].text
	stop_term = 'Fusion.globalContent'
	vals = eval(str(list(filter(lambda x: x.startswith(stop_term), data.split(';')))))
	try:
		dump = json.loads(vals[0].split(f"{stop_term}=")[-1])
	except:
		try:
			dump = json.loads(vals[0].split(f"{stop_term}=")[-1]+'"}]}}')
		except:
			raise
		pass
	return (dump['prices'][symbol]['iso'], dump['prices'][symbol]['ohlc'])