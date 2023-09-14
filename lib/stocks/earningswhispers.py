import os, json, requests
from datetime import datetime
import pandas as pd

def get_caldata(date, url='https://www.earningswhispers.com'):
	try:
		datetime.strptime(date, '%Y%m%d')
	except:
		print('Date format is incorrect')
		os._exit(1)
	cookieString='.AspNetCore.Antiforgery.gLLQ8_-gK9o=IAMAI; hidenonconfirmed=0; .AspNet.Consent=yes'
	res = requests.get(f"{url}/api/caldata/{date}", headers={'cookie':cookieString, 'referer':url, 'User-Agent':'IAMAI'})
	if not res.ok:
		print('API response is invalid')
		os._exit(2)
	return json.loads(res.content)

def get_caldata_range(start, end):
	raw_dates = pd.date_range(start, end, freq='D').to_series()
	df = pd.DataFrame(raw_dates, columns=['dates'])
	df['dow'] = raw_dates.dt.dayofweek
	dates = list(map(lambda d: d.astype(str).split('T')[0].replace('-',''), df[df['dow']<5].dates.values))
	return pd.concat(list(map(pd.DataFrame, map(get_caldata, dates)))).reset_index(drop=True)