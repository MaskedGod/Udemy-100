print("Welcome to the tip calculator.")
bill = float(input("what was the total bill? \n"))
guests = float(input("How many people to split the bill? \n"))
tip = (bill / 100) * float(input("What percentage tip would you like to give? \n"))
total = (bill + tip) / guests
print(round(total))