from art import logo
print(logo)

there_is_bidder = True
bidding_details = {}

while there_is_bidder:
  name = input("What is your name?: ").lower()
  bid_amount = int(input("What is your bid?: $"))
  is_there_another = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  # Adding the bidder and their amount to the dictionary
  bidding_details[name] = bid_amount

  if is_there_another != 'yes':
    there_is_bidder = False

max_bid = 0
winner_name = ""

for name in bidding_details:
  if bidding_details[name] > max_bid:
    max_bid = bidding_details[name]
    winner_name = name

print("The winner is {:s} with a bid of ${:d}".format(winner_name, max_bid))
