from ib_async import *

util.startLoop()  # Required for notebooks using asyncio event loop

# Initialize IB API connection
ib = IB()
ib.connect('127.0.0.1', 4004, clientId=400)  # Make sure port & clientId are aligned with Gateway config

# Set market data type to delayed/free data
ib.reqMarketDataType(4)

# Request historical data for EUR/USD forex pair
contract = Forex('EURUSD')
bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# Convert historical bars to pandas DataFrame and print
df = util.df(bars)
print(df)

# Sample contract qualification and market data request for TSLA stock
tsla_contract = Stock(symbol='TSLA', exchange='SMART', currency='USD')
ib.qualifyContracts(tsla_contract)
tsla_ticker = ib.reqMktData(tsla_contract, "", False, False)
tsla_ticker.marketPrice()  # Print current market price

# Retrieve and display recent fills (if any)
util.df(ib.fills())

# Alternate way to define a contract
contract = Contract(symbol='TSLA', secType='STK', exchange='SMART', currency='USD')
ib.qualifyContracts(contract)

# Another test with TSLA using Stock shortcut
stock = Stock(symbol='TSLA', exchange='SMART', currency='USD')
ib.qualifyContracts(stock)

# Request contract details for AMD
amd = Stock(symbol="AMD")
cds = ib.reqContractDetails(amd)
df_amd_contract_details = util.df(cds)
df_amd_contract_details  # View all matching AMD contracts

# Request and view contract details for EURUSD forex pair
eurusd = Forex(pair='EURUSD')
util.df(ib.reqContractDetails(eurusd))
