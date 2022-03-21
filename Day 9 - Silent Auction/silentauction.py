
from art import logo
from os import system
print(logo)

# Ask for name input
name = input("What is your name? ")

# Ask for bid price
bid = int(input("What is your bid? $"))

# Add name and bid into a dictionary as the key and value
auctionBids = {}
auctionBids[name] = bid

# Ask if there are other bidders
other_bidders = input("Other bidders? Answer yes or no ")
bid_flag = True

# Using a while loop to for other bidders
while bid_flag:
  if other_bidders == 'yes':
    system('cls')
    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid? $"))
    auctionBids[user_name] = user_bid
    other_bidders = input("Other bidders? Answer yes or no ")
  else:
    # Using the max function to find the highester bidder and their bid
    highest_bidder = max(auctionBids, key=auctionBids.get)
    biggest_bid = max(auctionBids.values())
    print(f"{highest_bidder} won the auction with a bid of ${biggest_bid}")
    bid_flag = False
