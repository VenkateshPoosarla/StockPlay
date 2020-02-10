
import pandas as pd
df=pd.read_csv("../out.csv")
# Warren Buffet Formula
def calculate_Warren_Buffet_Formula():
    print(df[['stock','P/B','Dividend']])

calculate_Warren_Buffet_Formula()