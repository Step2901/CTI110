Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\19104\AppData\Local\Programs\Python\Python311\P1HW2E_LiggonsStephanie.py
This program calculates and displays travel expenses
Enter your budget : 1200
Enter your destination : Asheville
How much you will spend on gas : 250
Approximately how much you need for accomodation ? : 300
Last, how much do you need for food? : 200
------------------------------travel expenses----------------------------------
Location : Asheville
Initial budget : 1200.0

Fuel : 250.0
Accomodation : 300.0
Food : 200.0

Remaining balance : 450.0

#output
print("---------------Travel Expense---------------")
print(f"{'Location:' : <20}", f"{ dest : <20}")
print(f"{'Initial budget:' : <20}", f"{ '$'+str(float(amount)) : <20}")
print(f"{'Fuel:' : <20}", f"{'$'+str(float(gas)) : <20}")
print(f"{'Accommodation:' : <20}", f" {'$'+str(float(hotel)) : <20}")
print(f"{'Food:' : <20}", f"{'$'+str(float(food)) : <20}")

#calculating the remaining balance
remaining = amount - (gas+hotel+food)
print("--------------------------------------------")
print(f"{'Remaining balance:' : <20}", f"{'$'+str(float(remaining)) : <20}")
