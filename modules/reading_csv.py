import pandas

def print_excel():
    data = pandas.read_excel(open("Personal Finance Project.xlsx", 'rb'))
    print(data)