# Market Insight
CLI tool to obtain some basic information for cryptocurrency and stock market activities.

## Requirements
Basic data analysis libraries (i.e. `pandas`, `numpy`, `matplotlib`) are assumed to be installed.

Other libraries are in `requirements.txt` (i.e. `pip install -r`)

## Arguments
### `mkisctl`
```
usage: mkisctl [-h] [-v] [-e] {cc,uw,yf,cm,cd,ew,nd,qq} ...

positional arguments:
  {cc,uw,yf,cm,cd,ew,nd,qq}
                        Different source selection
    cc                  CoinCodex (Source: coincodex.com)
    uw                  Unusual Whales (Source: unusualwhales.com)
    yf                  Yahoo Finance (Source: finance.yahoo.com)
    cm                  CoinMarketCap (Source: coinmarketcap.com)
    cd                  CoinDesk (Source: coindesk.com)
    ew                  Earnings Whispers (Source: earningswhispers.com)
    nd                  NASDAQ (Source: nasdaq.com)
    qq                  Quiver Quantitative (Source: quiverquant.com)

options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose output
  -e, --export          Export output to downloads folder
```

### CoinCodex (`mkisctl cc`)
```
usage: mkisctl cc [-h] (-s STOCK | -c CRYPTO)

options:
  -h, --help            show this help message and exit
  -s STOCK, --stock STOCK
                        Requires specifying stock (example: NVDA)
  -c CRYPTO, --crypto CRYPTO
                        Requires specifying crypto (example: bitcoin)
```

### Unusual Whales (`mkisctl uw`)
```
usage: mkisctl uw [-h] [-o] [-m] [-c] [-t TICKER]

options:
  -h, --help            show this help message and exit
  -o, --option          Option information (default: False)
  -m, --market          Market information (default: False)
  -c, --crypto          Crypto information (default: False)
  -t TICKER, --ticker TICKER
                        Company/Ticker information
```

### Yahoo Finance (`mkisctl yf`)
```
usage: mkisctl yf [-h] [-t TICKER] [-r RANGE]

options:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker (default: BTC-USD)
  -r RANGE, --range RANGE
                        Time Range (default: 24h)
```

### CoinMarketCap (`mkisctl cm`)
```
usage: mkisctl cm [-h] [-s SLUG] [-l LIMIT]

options:
  -h, --help            show this help message and exit
  -s SLUG, --slug SLUG  Slug (default: bitcoin)
  -l LIMIT, --limit LIMIT
                        Limit (default: 10)
```

### CoinDesk (`mkisctl cd`)
```
usage: mkisctl cd [-h] [-s SYMBOL]

options:
  -h, --help            show this help message and exit
  -s SYMBOL, --symbol SYMBOL
                        Symbol (default: BTC)
```

### Earnings Whispers (`mkisctl ew`)
```
usage: mkisctl ew [-h] [-s START] [-e END]

options:
  -h, --help            show this help message and exit
  -s START, --start START
                        From (default: 20230915)
  -e END, --end END     To (default: 20230922)
```

### NASDAQ (`mkisctl nd`)
```
usage: mkisctl nd [-h] [-t TICKER] [-l LIMIT]

options:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker (default: nvda)
  -l LIMIT, --limit LIMIT
                        Limit (default: 30)
```

### Quiver Quant (`mkisctl qq`)
```
usage: mkisctl qq [-h] (-c | -s | -r | -e | -d | -g | -l | -q | -i | -z)

options:
  -h, --help         show this help message and exit
  -c, --congress     US Congress trading
  -s, --senate       US Senate trading
  -r, --house        US House of Representatives trading
  -e, --election     Election contributions
  -d, --dcinsider    DC Insider scores
  -g, --govcontract  US Government contracts
  -l, --lobbying     Lobbying
  -q, --inflation    Inflation
  -i, --insiders     Insiders
  -z, --stocksplits  Stock splits
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

5) Verbose output of congress trading

`./mkisctl -v qq -c`

```
# recent_trades
                                                 Stock                    Transaction                  Politician  ...         Traded Description        
```

6) Check the IFC table for abbreviations:

`python -i mkisctl`

```
>>> from lib.crypto import table
>>> table[table['name'].apply(lambda x: x in ['Bitcoin', 'Dogecoin'])]
        name ticker symbol      slug
8    Bitcoin    BTC   ฿, ₿   bitcoin
12  Dogecoin   DOGE   D, Ɖ  dogecoin
```