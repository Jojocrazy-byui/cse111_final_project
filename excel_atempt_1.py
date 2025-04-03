import pandas as pd 

file = pd.read_excel("Personal Finance Project (1).xlsx", sheet_name="Personal Finance Project (1)")

print(file)



# Group by Name and Income/Expense type, summing MoneyChange
grouped = file.groupby(["Name:", "Income/Expense"])["MoneyChange"].sum().unstack(fill_value=0)

# Add a Net Total column
grouped["Net Total"] = grouped.get("Income", 0) + grouped.get("Expense", 0)  # Expenses are already negative

# Display totals
# print(grouped)

just_expenses=file[file["Income/Expense"]=="Expense"]


just_expenses_sorted=just_expenses.groupby("Name:")["MoneyChange"].sum()
just_expenses_sorted=just_expenses.groupby(["Name:","Category"])["MoneyChange"].sum()


print(just_expenses_sorted)



