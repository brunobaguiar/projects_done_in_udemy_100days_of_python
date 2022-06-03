from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bids = {}
new_bid = True
while new_bid == True:
  name = input("What is your name? ")
  bid = input("What is your bid? $")
  bids[name] = bid
  decision = input("Are there new users that whant to bid? ")
  if decision == "no":
    new_bid = False
  elif decision == "yes":
    clear()
fin_max = max(bids, key=bids.get)
print(f"Winner bid is: {fin_max} with a bid of $ {bids[fin_max]}")
