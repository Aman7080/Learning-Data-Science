""" 2. You are given following list of stocks and their prices in last 3 days,

    |Stock|Prices|
    |-------|----------|
    |info|[600,630,620]|
    |ril|[1430,1490,1567]|
    |mtl|[234,180,160]|

    1. Write a program that asks user for operation. Value of operations could be,
        1. print: When user enters print it should print following,
            ```
            info ==> [600, 630, 620] ==> avg:  616.67
            ril ==> [1430, 1490, 1567] ==> avg:  1495.67
            mtl ==> [234, 180, 160] ==> avg:  191.33
            ```
        2. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

 """
import statistics

stocks={
    "info":[600,630,620],
    "ril":[1430,1490,1567],
    "mtl":[234,180,160],
}

def print_all():
    for name,prices in stocks.items():
        print(f"{name} ==> {prices} ==> avg: {round(statistics.mean(prices),2)}")

def add_stock():
    name = input("Enter stock ticker to add : ")
    price = int(input("Enter price : "))
    if name in stocks:
        stocks[name].append(price)
    else:
        stocks.update({name:[price]})  
    print_all()     

operation = input("What do you want to do (print / add) : ").lower()

if operation == "print":
    print_all()
elif operation == "add": 
    add_stock()
else:
    print("WRONG ENTRY!!!")    