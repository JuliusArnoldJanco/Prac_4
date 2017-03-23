"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    incomes = []
    month_num = int(input("How many months? "))

    for month_num in range(1, month_num + 1):
        income = float(input("Enter income for month  {:0.0f}: ".format(month_num)))
        incomes.append(income)

    Output_print(incomes, month_num)


def Output_print(incomes, month_num):
    print("\nIncome Report\n-------------")
    total = 0
    for month_num in range(1, month_num + 1):
        income = incomes[month_num - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month_num, income, total))


main()