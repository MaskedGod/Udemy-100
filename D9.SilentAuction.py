import os

print("Welcome to the secret auction program.")

def clear():
    os.system('cls')

def highest_bidder():
    auction = True
    bidders = {}
    
    while auction:
        name = input("What's your name: ")
        bid = int(input("What's your bid: $"))
        bidders[name] = bid
        clear()
        
        if input("Are there any other bidders? 'yes' or 'no' \n") == "no":
            # auction = False
            break
        clear()
        
    for name, bid in bidders.items():
        max = bid
        if bid > max:
            max = bid 
    clear()     
    print(f"The winner is {name} with ${max}")

    if input("Want another auction? 'yes' or 'no' \n") == "yes":
        clear()
        highest_bidder()
    
highest_bidder()