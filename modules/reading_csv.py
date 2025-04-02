# Jacob Henrie will be working on this one.
import pandas as pd

def print_excel(account_name):
    data = pd.read_excel("Personal Finance Project (1).xlsx",'AccountBalance')
    index_list = []
    for i in range(int(data.size/2)):
        index_list.append(data.at[i, 'Account'])
    data.index = index_list
    print(data.at[account_name, 'Balance'])