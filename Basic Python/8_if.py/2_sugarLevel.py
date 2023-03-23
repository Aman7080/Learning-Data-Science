""" 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
    1. Ask user to enter his fasting sugar level
    2. If it is below 80 to 100 range then print that sugar is low
    3. If it is above 100 then print that it is high otherwise print that it is normal """

sugarLevel = float(input("Enter your fasting sugar level : "))
if sugarLevel < 80:
    print("sugar is low")
elif sugarLevel < 80:
    print("sugar is high")
else:
    print("sugar is normal")