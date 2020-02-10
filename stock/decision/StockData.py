master_url = 'https://finviz.com/quote.ashx?t='

stocks = ['cmg']
import requests
from bs4 import BeautifulSoup
import pandas as pd
stock_dict = {}
columns = ["stock", "Index", "P/E", "EPS (ttm)", "Insider Own", "Shs Outstand", "Perf Week", "Market Cap",
           "Forward P/E", "EPS next Y", "Insider Trans", "Shs Float", "Perf Month", "Income", "PEG", "EPS next Q",
           "Inst Own", "Short Float", "Perf Quarter", "Sales", "P/S", "EPS this Y", "Inst Trans", "Short Ratio",
           "Perf Half Y", "Book/sh", "P/B", "EPS next Y", "ROA", "Target Price", "Perf Year", "Cash/sh", "P/C",
           "EPS next 5Y", "ROE", "52W Range", "Perf YTD", "Dividend", "P/FCF", "EPS past 5Y", "ROI", "52W High", "Beta",
           "Dividend %", "Quick Ratio", "Sales past 5Y", "Gross Margin", "52W Low", "ATR", "Employees", "Current Ratio",
           "Sales Q/Q", "Oper. Margin", "RSI (14)", "Volatility", "Optionable", "Debt/Eq", "EPS Q/Q", "Profit Margin",
           "Rel Volume", "Prev Close", "Shortable", "LT Debt/Eq", "Earnings", "Payout", "Avg Volume", "Price", "Recom",
           "SMA20", "SMA50", "SMA200", "Volume", "Change"]
lili=[]
for stock in stocks:
    li=[]
    li.append(stock)
    page = requests.get(master_url + stock)
    # print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    x = soup.find_all(class_='snapshot-table2')[0]
    # soup1 = BeautifulSoup(str(x), 'html.parser')
    rows = x.find_all(class_='table-dark-row')
    for row in rows:
        # print("*"*20)
        cols = row.find_all('td')
        x = 1
        for col in cols:
            if x % 2 == 0:
                li.append(str(col.text))
            x += 1

    lili.append(li)
    # print (lili)
    df = pd.DataFrame(lili, columns=columns)
df.to_csv('out.csv')          # print(col)
    # for row in soup1.find_all(class_='table-dark-row'):
    #     # cols=BeautifulSoup(soup1.find_all('td'))
    #     print(row)
