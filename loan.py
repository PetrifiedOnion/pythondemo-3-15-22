# Get the loan details
money_owed = float(input("How much money do you own in dollars?\n"))
apr = float(input("What is your annual percentage rate?\n"))
payment = float(input("what will your monthly payment be, in dollars?\n"))
months = int(input("How many months do you want to see results for?\n"))

monthly_rate = apr/100/12
for i in range(months):


    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest end=' '")
    print("Now I owe", money_owed)
