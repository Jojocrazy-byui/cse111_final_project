from modules import reading_csv
from modules import account

def cycle(): # Works by checking if the inputs are in fact the inputs we are looking for.
    choice = '-1'
    while choice not in ['1', '2', '3', '0', '0x']:
        print("----CSE 111: Final Project----")
        print("Written by Jacob Henrie, Spencer Olson, Carson Payne")
        print("Personal Finance application")
        print("1)N.A.\t2)N.A.\t3)N.A.\t0)Exit")
        choice = input('->')
    return choice
# 1) Account details
#   a) Balance
#   b) Transation list
#   c) ...
# 2)
# 3) Budget

#This is main.
choice = cycle()
while choice != '0':
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '0x':
        account_name = input('Account Name\t->')
        reading_csv.print_excel(account_name)
    choice = cycle()
