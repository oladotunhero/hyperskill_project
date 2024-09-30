# Write your code here
prices= """Prices:
Bubblegum: $2
Toffee: $0.2
Ice cream: $5
Milk chocolate: $4
Doughnut: $2.5
Pancake: $3.2
"""
print(prices)

earned= """
Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80
"""
print(earned)

#remove value from the string dictionary and sum it out
lines = earned.strip().split('\n')
income = []
for line in lines:
    if "$" in line:
        amount = line.split('$')[-1].strip()
        income.append(float(amount))
total_earning = sum(income)

print(f"Income: {total_earning}")

#calculate the net income based on business expenses
staff_expenses = int(input("Staff expenses: \n"))
other_expenses = int(input("Other expenses: \n"))
net_income = total_earning - staff_expenses - other_expenses
print(f"Net income: ${net_income}")