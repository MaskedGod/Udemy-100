import os
# os.system('cls')
print("Welcome to the secret auction program.")
def clearshell():
    os.system('cls')
def highest_bidder():
    auction = True
    bidders = {}
    while auction == True:
        name = input("What's your name: ")
        bid = int(input("What's your bid: $"))
        bidders[name] = bid
        clearshell()
        if input("Are there any other bidders? 'yes' or 'no' \n") == "no":
            auction = False
        clearshell()
    for name, bid in bidders.items():
        print(name)        
    print(bidders)
highest_bidder()