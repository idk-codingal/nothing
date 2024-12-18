actual_cost = float(input("Please enter the product correct price: "))
sell_amount = float(input("Please enter the product sell amount: "))
if(sell_amount > actual_cost):
    amount = sell_amount-actual_cost
    print("Total profit = {0}".format(amount))
else:
    print("No profit")