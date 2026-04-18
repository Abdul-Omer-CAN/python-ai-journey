import yfinance as yf

### fetch live stock data ###
stock = yf.Ticker("AAPL")  # .Ticker as you know highlights that stock then info does the rest. Also T needs to be capital because it is a type of class.
info = stock.info  # .info pulls the info of that stock


print(f"Company: {info['longName']}")      # '[]' this then pulls the individual values via .info aka info["key"]
print(f"Current Price: ${info['currentPrice']:.2f}")
print(f"Market Cap: ${info['marketCap']:,.0f}")  # in the project we used .get("",0) it will import it safely without crashed because of 0.
print(f"52 Week High: ${info['fiftyTwoWeekHigh']:.2f}")
print(f"52 Week Low: ${info['fiftyTwoWeekLow']:.2f}")
