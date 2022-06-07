
import os
clear = lambda: os.system('cls')

from art import logo
print(logo)
print("Welcome to the Secret Auction Program!")

bidders = {}
bid_go = True

while bid_go == True:
  name = input("What is your name?\n")
  bid = int(input("What is your bid price?\n"))
  bidders[name] = bid
  more_bid = input("Are there other users who want to bid?\n").lower()

  if more_bid == "yes":
    clear()
  elif more_bid == "no":
    bid_go = False
  else:
    print("Please enter 'yes' or 'no'.")
    while True:
      more_bidders = input("Are there other users who want to bid?\n").lower()
      if more_bidders == "yes":
        clear()
        break
      elif more_bidders == "no":
        bid_go = False
        break
      else:
        print("Please enter 'yes' or 'no'.")
        
highest_offer = 0
highest_bidder = ""
tied_bidders = []
total_bidders = 0

for key, value in bidders.items(): 
  if value > highest_offer:
    highest_offer = value
    highest_bidder = key
    total_bidders = 0
    tied_bidders.append(key)

  elif value == highest_offer:
    highest_offer = value
    tied_bidders.append(key)
    total_bidders += 1


def listToString(s):
  final_tied_bidders_2 = " and "
  return (final_tied_bidders_2.join(s))

final_tied_bidders = listToString(tied_bidders)

if total_bidders == 0:
  print(f"The highest bidder is {highest_bidder} with a bid price of {highest_offer}.")
elif total_bidders >=1:
    print(f"There is a tie. {final_tied_bidders} tied with a bid price of {highest_offer}.")