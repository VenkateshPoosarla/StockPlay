master_url = 'https://finviz.com/quote.ashx?t='

import requests
from bs4 import BeautifulSoup
import pandas as pd

stocks = [[x[1].lower(), x[2]] for x in
          pd.read_csv("../Stock_Symbols.csv")[['Symbol', 'Company name']].to_records().tolist()]
# stocks = ['cmg']
print(stocks)
stock_dict = {}
columns = ["stock", "stockName", "Index(Major index membership)", "P/E(Price-to-Earnings (ttm))",
           "EPS (ttm)(Diluted EPS (ttm))", "Insider Own(Insider ownership)", "Shs Outstand(Shares outstanding)",
           "Perf Week(Performance (Week))", "Market Cap(Market capitalization)",
           "Forward P/E(Forward Price-to-Earnings (next fiscal year))",
           "EPS next Y(EPS estimate for next year)",
           "Insider Trans(Insider transactions (6-Month change in Insider Ownership))", "Shs Float(Shares float)",
           "Perf Month(Performance (Month))", "Income(Income (ttm))", "PEG(Price-to-Earnings-to-Growth)",
           "EPS next Q(EPS estimate for next quarter)", "Inst Own(Institutional ownership)",
           "Short Float(Short interest share)", "Perf Quarter(Performance (Quarter))", "Sales(Revenue (ttm))",
           "P/S(Price-to-Sales (ttm))", "EPS this Y(EPS growth this year)",
           "Inst Trans(Institutional transactions (3-Month change in Institutional Ownership))",
           "Short Ratio(Short interest ratio)", "Perf Half Y(Performance (Half Year))",
           "Book/sh(Book value per share (mrq))", "P/B(Price-to-Book (mrq))", "EPS next Y(EPS growth next year)",
           "ROA(Return on Assets (ttm))", "Target Price(Analysts' mean target price)", "Perf Year(Performance (Year))",
           "Cash/sh(Cash per share (mrq))", "P/C(Price to cash per share (mrq))",
           "EPS next 5Y(Long term annual growth estimate (5 years))", "ROE(Return on Equity (ttm))",
           "52W Range(52-Week trading range)", "Perf YTD(Performance (Year To Date))", "Dividend(Dividend (annual))",
           "P/FCF(Price to Free Cash Flow (ttm))", "EPS past 5Y(Annual EPS growth past 5 years)",
           "ROI(Return on Investment (ttm))", "52W High(Distance from 52-Week High)",
           "Beta(Beta)", "Dividend %(Dividend yield (annual))", "Quick Ratio(Quick Ratio (mrq))",
           "Sales past 5Y(Annual sales growth past 5 years)", "Gross Margin(Gross Margin (ttm))",
           "52W Low(Distance from 52-Week Low)", "ATR(Average True Range (14))", "Employees(Full time employees)",
           "Current Ratio(Current Ratio (mrq))", "Sales Q/Q(Quarterly revenue growth (yoy))",
           "Oper. Margin(Operating Margin (ttm))", "RSI (14)(Relative Strength Index)",
           "Volatility(Volatility (Week, Month))", "Optionable(Stock has options trading on a market exchange)",
           "Debt/Eq(Total Debt to Equity (mrq))", "EPS Q/Q(Quarterly earnings growth (yoy))",
           "Profit Margin(Net Profit Margin (ttm))", "Rel Volume(Relative volume)", "Prev Close(Previous close)",
           "Shortable(Stock available to sell short)", "LT Debt/Eq(Long Term Debt to Equity (mrq))",
           "Earnings(Earnings date<br><br>BMO = Before Market Open<br>AMC = After Market Close)",
           "Payout(Dividend Payout Ratio (ttm))", "Avg Volume(Average volume (3 month))", "Price(Current stock price)",
           "Recom(Analysts' mean recommendation (1=Buy 5=Sell))", "SMA20(Distance from 20-Day Simple Moving Average)",
           "SMA50(Distance from 50-Day Simple Moving Average)", "SMA200(Distance from 200-Day Simple Moving Average)",
           "Volume(Volume)", "Change(Performance (today))"]
lili = []
for stock in stocks:
    li = []
    li.append(stock[0])
    li.append(stock[1])
    page = requests.get(master_url + stock[0])
    soup = BeautifulSoup(page.content, 'html.parser')
    x = soup.find_all(class_='snapshot-table2')[0]
    rows = x.find_all(class_='table-dark-row')
    for row in rows:
        cols = row.find_all('td')
        x = 1
        for col in cols:
            if x % 2 == 0:
                li.append(str(col.text))
            x += 1

    lili.append(li)
    df = pd.DataFrame(lili, columns=columns)
df.to_csv('../out.csv')
