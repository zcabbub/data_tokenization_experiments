import random
from Agent import Agent
from Asset import DataAsset


asset = DataAsset()
print("asset qualities: {price}".format(price = asset.qualities))
print("asset value: {price}\n".format(price = asset.get_value()))

num_bidders = 10
bidders = [Agent(iid=bidder, asset=asset) for bidder in range(num_bidders)]

bids = [bidders[x].get_bid() for x in range(num_bidders)]

# determine winner and the price paid
highest_bid = max(bids)
second_highest_bid = max(bid for bid in bids if bid != highest_bid)

if highest_bid == second_highest_bid:
    # tie, choose a winner randomly
    winner_index = random.choice([index for index in range(num_bidders) if bids[index] == highest_bid])
else:
    # clear winner
    winner_index = bids.index(highest_bid)

price_paid = second_highest_bid if second_highest_bid > 0 else 0

# Calculate the profit of the winner
profit = asset.get_value() - price_paid

print("Bids:", bids)
print("Winner index:", winner_index)
print("Price paid:", price_paid)
print("Profit:", profit)