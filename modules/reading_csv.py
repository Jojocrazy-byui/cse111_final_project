# Jacob Henrie will be working on this one.
import pandas as pd

def print_excel():
    data = pd.read_excel("Personal Finance Project.xlsx",'AccountBalance')
    print(data.iloc())