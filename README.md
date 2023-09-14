# Market Insight
CLI tool to obtain some basic information for cryptocurrency and stock market activities.

## Requirements
Basic data analysis libraries (i.e. `pandas`, `numpy`, `matplotlib`) are assumed to be installed.

Other libraries are in `requirements.txt` (i.e. `pip install -r`)

## Arguments
### `mkisctl`
```
usage: mkisctl [-h] [-v] [-e] {yf,cm,cd,ew,nd} ...

positional arguments:
  {yf,cm,cd,ew,nd}  Different source selection
    yf              Yahoo Finance
    cm              CoinMarketCap
    cd              CoinDesk
    ew              Earnings Whispers
    nd              NASDAQ

options:
  -h, --help        show this help message and exit
  -v, --verbose     Verbose output
  -e, --export      Export output to downloads folder
```

### Yahoo Finance (`mkisctl yf`)
```
usage: mkisctl yf [-h] [--ticker TICKER] [--range RANGE]

options:
  -h, --help       show this help message and exit
  --ticker TICKER  Ticker (default: BTC-USD)
  --range RANGE    Time Range (default: 24h)
```

### CoinMarketCap (`mkisctl cm`)
```
usage: mkisctl cm [-h] [--slug SLUG] [--limit LIMIT]

options:
  -h, --help     show this help message and exit
  --slug SLUG    Slug (default: bitcoin)
  --limit LIMIT  Limit (default: 10)
```

### CoinDesk (`mkisctl cd`)
```
usage: mkisctl cd [-h] [--symbol SYMBOL]

options:
  -h, --help       show this help message and exit
  --symbol SYMBOL  Symbol (default: BTC)
```

### Earnings Whispers (`mkisctl ew`)
```
usage: mkisctl ew [-h] [--start START] [--end END]

options:
  -h, --help     show this help message and exit
  --start START  From (default: 20230913)
  --end END      To (default: 20230920)
```

### NASDAQ (`mkisctl nd`)
```
usage: mkisctl nd [-h] [--ticker TICKER] [--limit LIMIT]

options:
  -h, --help       show this help message and exit
  --ticker TICKER  Ticker (default: nvda)
  --limit LIMIT    Limit (default: 30)
```

## Examples
Note: all examples below assume user is running the commands from the `market-insight` directory.

Remark: Optionally, user may consider adding the directory to the PATH environment variable to omit the `./`.

1) Graph multiple tickers against JPY:
    
`for ticker in BTC DOGE; do ./mkisctl yf --ticker $ticker-JPY; done`

*_opens multiple tabs of graphs on default browser_

2) Display multple OHLC prices with symbol:

`for ticker in BTC DOGE; do ./mkisctl cd --symbol $ticker; done`

```
BTC: {'o': 25904.4255622, 'h': 26535, 'l': 25842.8, 'c': 26273}
DOGE: {'o': 0.0611061372, 'h': 0.0621485196, 'l': 0.0607435794, 'c': 0.0615675025}
```

3) Print out earnings information for one day: (output has been omiited)

`./mkisctl -v ew --start 20230913 --end 20230913`

```
   ticker                                 company  total          nextEPSDate  releaseTime  ...   qSales   eps  surprise  revenue direction
```

4) Export and print out insider trades: (output has been omiited)

`./mkisctl -ev nd`

```
                insider  relation    lastDate                transactionType   ownType sharesTraded lastPrice sharesHeld
```

5) Check the IFC table for abbreviations:

`python -i mkisctl`

```
>>> from lib.crypto import table
>>> table[table['name'].apply(lambda x: x in ['Bitcoin', 'Dogecoin'])]
        name ticker symbol      slug
8    Bitcoin    BTC   ฿, ₿   bitcoin
12  Dogecoin   DOGE   D, Ɖ  dogecoin
```