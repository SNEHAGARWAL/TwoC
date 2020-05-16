cost = int(input("Enter cost Price "))
sell = int(input("Enter selling Price "))

Profit = sell-cost
profit_per = (Profit/cost)*100

inc_profit_per = ((5*profit_per)/100) + profit_per

new_sp = cost + (inc_profit_per/100)*cost

print(new_sp)