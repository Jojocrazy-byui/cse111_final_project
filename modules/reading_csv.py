import pandas as pd

def print_excel():
    data = pd.read_excel(open("Personal Finance Project.xlsx", 'rb'))
    print(data)