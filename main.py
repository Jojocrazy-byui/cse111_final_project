from modules import reading_csv
p_e = reading_csv.print_excel()

def cycle():
    print("----CSE 111: Final Project----")
    print("Personal Finance application")
    print("1)N.A.\t2)N.A.\t3)N.A.\t0)Exit")
    return input('->')
#This is main.


choice = cycle()
while choice != '0':
    print('Made it!')
    choice = cycle()