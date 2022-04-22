from pickle import GET
import ccxt

ftx = ccxt.ftx()


def get_quote(request):
    markets = ftx.load_markets()

    return{
        "symbols": list(markets.keys())
    }
