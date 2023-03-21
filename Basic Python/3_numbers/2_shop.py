""" 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back? """

chips_bought = 9
packet_cost = 1.49

total_chip_cost = chips_bought*packet_cost
money_gave = 20

return_money = money_gave - total_chip_cost

print(f"dollar returned by shopkeeper = {return_money}")