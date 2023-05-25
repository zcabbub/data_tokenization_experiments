import random

import numpy as np

from Agent import Agent
from Asset import DataAsset
import matplotlib.pyplot as plt

def plot(var, n):
    x_axis = list(range(n))

    plt.plot(x_axis, var)
    plt.title('Seller Profit')
    plt.xlabel('Round')
    plt.ylabel('Profit')
    plt.show()

def second_price_auction(bids, pprint=True):
    """
    :param bids:
    :param pprint:
    :return: winner_index, price_paid, seller_profit
    """

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
    seller_profit = price_paid - asset.get_value()

    if pprint:
        print("Bids:", bids)
        print("Winner index:", winner_index)
        print("Price paid:", price_paid)
        print("Seller Profit:", seller_profit)

    return winner_index, price_paid, seller_profit


def rsop_auction(bids, pprint=True):
    """
    Implements Random Sampling Oprimal Price auction.
    Calculates the optimal price considering the bids, accordingly to the Random Sampling Empirical Myerson mechanism.
    :param bids:
    :param pprint: if to print or not
    :return: optimal price, maybe the distribution as well.
    """

    # randomly partition the bids in 2 sets
    c_bids = bids
    random.shuffle(c_bids)

    set_A = bids[:(len(bids)//2)]
    set_B = bids[(len(bids)//2):]

    # randomly choose which price you set, fair coin toss
    if np.random.random() < 0.5:
        optimal_price = max(set_A)
    else:
        optimal_price = max(set_B)

    return optimal_price


# TODO: maybe add dynamic pricing. need variable number of bidders to have variable demand
#       make a demand parameter that modifies the price accordingly to the demand as well

profit_results = []
prices = []

n = 1000

for times in range(n):
    asset = DataAsset()
    # print("data profiler value: {price}\n".format(price = asset.get_value()))

    num_bidders = 10
    bidders = [Agent(iid=bidder, asset=asset) for bidder in range(num_bidders)]

    bids = [bidders[x].get_bid() for x in range(num_bidders)]

    optimal_price = rsop_auction(bids)
    prices.append(optimal_price)



    # are the buyers going to pay this price?
    # depends how far from their bid is? or depends on their preference?

    # show that the convergence to all the possible bidders being fulfilled/happy
    # is faster with a truthful mechanism than without it: just set the highest.



    # _, price_paid, profit = second_price_auction(bids, pprint=False)
    # profit_results.append(profit)

# plot(sorted(profit_results), n)
# plot(sorted(prices_paid), n)