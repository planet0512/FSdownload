#define the functions to download financial statement from Sina
#using tushare


import tushare as ts
import time

tickers = ts.get_stock_basics()
tickers = sorted(tickers.index.values)
tickers.to_csv("your_path"+"/tickers.csv")
#getting all the tickers to download the stock data


def get_profit_statement():
    i=0
    while i<len(tickers):
        try:
            profit_statement = ts.get_profit_statement(tickers[i])
            profit_statement.to_csv("your_path"+"/profit_statement_"+tickers[i]+'.csv', encoding="gbk")
            # remember to change it to your designated path
            print(i)
            i=i+1
            time.sleep(10)
        except:
            print(i+'failed')
            time.sleep(60)


def get_balance_sheet():
    i = 0
    while i < len(tickers):
        try:
            balance_sheet = ts.get_balance_sheet(tickers[i])
            balance_sheet.to_csv("your_path"+"/balance_sheet_" + tickers[i] + '.csv', encoding="gbk")
            # remember to change it to your designated path
            print(i)
            i = i + 1
            time.sleep(10)
        except:
            print(i + 'failed')
            time.sleep(60)



def get_cash_flow():
    i = 0
    while i < len(tickers):
        try:
            cash_flow = ts.get_cash_flow(tickers[i])
            cash_flow.to_csv("your_path"+"/cash_flow_" + tickers[i] + '.csv', encoding="gbk")
            # remember to change it to your designated path
            print(i)
            i = i + 1
            time.sleep(10)
        except:
            print(i + 'failed')
            time.sleep(60)

