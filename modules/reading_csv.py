# Jacob Henrie will be working on this one.
import pandas as pd

def print_excel(account_name):
    data = pd.read_excel("Personal Finance Project (1).xlsx",'AccountBalance')
    index_list = []
    row, col = data.shape
    for i in range(int(row)):
        index_list.append(data.at[i, 'Account'])
    data.index = index_list
    print(data.at[account_name, 'Balance'])

def print_name():
    data = pd.read_excel("Personal Finance Project (1).xlsx")
    index_list = []
    row, col = data.shape
    for i in range(int(row)):
        index_list.append(data.at[i, 'Name:'])
    data.index = index_list
    print(data.at['Name:'])