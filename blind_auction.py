import operator
from art import logo

print(logo)
print("Welcome to the secret bids program.")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What's your name? ")
    price = input("What's your bid? $")
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    if other_bidders == "no":
        bidding_finished = True
        max_key = max(bids, key=lambda key: bids[key])
        max_value = bids[max(bids, key=bids.get)]
        print(f"The winner is {max_key} with a bid of ${max_value}")
    else:
        bidding_finished = False