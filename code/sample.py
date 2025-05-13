import math
import sys
import yfinance as yf
import stock_module


def main():
  STOCK_download = yf.download(tickers="AAPL", period="max")
  print(STOCK_download)
  
  sm = stock_module.StockTool()
  sm.getPrice(111)
  return

if __name__ == "__main__":
  main()
