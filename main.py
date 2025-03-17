from modules import reading_csv
import pandas
pe = reading_csv.print_excel()

#This is main.
data = pandas.read_excel(open("Personal Finance Project.xlsx", 'rb'))
print(data)