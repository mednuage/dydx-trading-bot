
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import constract_market_prices

if __name__=="__main__":
    #print("Hello bot!")

    # Connect to Client
    try:
       print ("Connection to client...")
       client =  connect_dydx()
    except Exception as e:
        print ("Error connectig to client", e)
        exit(1)

# Abort all open positions
if ABORT_ALL_POSITIONS:
    try:
        print ("Closing all positions ...")
        close_orders = abort_all_positions(client)
    except Exception as e:
            print ("Error closing all positions", e)
            exit(1)

# Find cointegrated Pairs
if FIND_COINTEGRATED:

    # Constractu Market Prices : A faire peu fréquement (exemple, une fois par jour)
    try:
        print ("Fetching market prices, please allow 3 minutes ...")
        df_market_prices = constract_market_prices(client) 
    except Exception as e:
            print ("Error constructing market prices !", e)
            exit(1)