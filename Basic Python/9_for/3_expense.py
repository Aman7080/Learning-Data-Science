""" 3. Your monthly expense list (from Jan to May) looks like this,
```
expense_list = [2340, 2500, 2100, 3100, 2980]
```
Write a program that asks you to enter an expense amount and program
should tell you in which month that expense occurred. If expense is not
found then it should print that as well. """

expense_list = [2340, 2500, 2100, 3100, 2980]
month = ["January","February","March","April","May"]
expense = int(input("Enter Your Expense : "))

count = False
for i in range(len(expense_list)):
    if expense == expense_list[i]:
        count = i

if count:
    print(f"you spent {expense} in {month[count]}")
else:
    print(f"You didn't spent {expense} in any month")