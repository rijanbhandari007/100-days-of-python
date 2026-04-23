
#! this is a tip calculator as final project of day 2 where total bill, tip percent, and number of people are given and final amount each person should pay comes out as output

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

person = int(input("How many people to split the bill?"))

total_tip = (tip/100)*total

final = round(((total + total_tip)/ person),2)

print(f"Each person should pay: ${final}")