# Crypto Scripts

CLI tool to obtain some basic information for cryptocurrency prices.

## Requirements
Basic data analysis libraries (i.e. `pandas`, `numpy`, `matplotlib`) are assumed to be installed.

Other libraries are in `requirements.txt` (i.e. `pip install -r`)

## bitcheck
### Arguments
```
usage: bitcheck [-h] [--verbose] [--slug SLUG] {cmc,cd,yf} ...

positional arguments:
  {cmc,cd,yf}  Different source selection
    cmc        CoinMarketCap
    cd         CoinDesk
    yf         YahooFinance

options:
  -h, --help   show this help message and exit
  --verbose    Verbose output
  --slug SLUG  Slug (default: bitcoin)
```

### CoinDesk
```
usage: bitcheck cd [-h] [--tag TAG]

options:
  -h, --help  show this help message and exit
  --tag TAG   Tag (default: fusion-metadata)
```

### CoinMarketCap
```
usage: bitcheck cmc [-h] [--limit LIMIT]

options:
  -h, --help     show this help message and exit
  --limit LIMIT  Limit (default: 10)
```

### Yahoo Finance
```
usage: bitcheck yf [-h] [--tick TICK]

options:
  -h, --help   show this help message and exit
  --tick TICK  Slug (overwrite: BTC-USD)
```

## earnings
```
usage: earnings [-h] [--verbose] [--start START] [--end END]

options:
  -h, --help     show this help message and exit
  --verbose      Verbose output
  --start START  From (default: 20230911)
  --end END      To (default: 20230918)
```

## Examples
### bitcheck
Graph multiple tickers against JPY:
    
`for ticker in BTC DOGE; do crypto-scripts/bitcheck yf --tick $ticker-JPY; done`

Export multple OHLC prices with slug:

`for ticker in bitcoin dogecoin; do crypto-scripts/bitcheck --slug $ticker cd; done`

Check the IFC table for abbreviations:

`python -i crypto-scripts/bitcheck cmc`

```
BTC: 25896.67140263601
>>> table[table['name'].apply(lambda x: x in ['Bitcoin', 'Dogecoin'])]
        name ticker symbol      slug
8    Bitcoin    BTC   ฿, ₿   bitcoin
12  Dogecoin   DOGE   D, Ɖ  dogecoin
```
### earnings
Save the exported data as CSV:
```
% python -i earnings --start 20230901 --end 20230930
>>> cdf.to_csv(f"{args.start}-{args.end}.csv")
```