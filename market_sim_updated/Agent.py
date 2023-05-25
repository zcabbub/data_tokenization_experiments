import numpy as np

class Agent():
    def __init__(self, iid, asset):
        # define strategy
        self.iid = iid
        # agent's own asset valuation strategy
        self.strategy = self.generate_new_strategy(asset)
        # if the player has to choose an option that is not his preference, he will be regretful.
        self.regret = None
        # self.preference = np.random.choice(asset.get_fractions())

    def generate_new_strategy(self, asset):
        # generate agent's valuation according the asset qualities
        # 66% of the data should fall within one standard deviation of the mean, [mu - sigma, mu + sigma]
        strategy = {quality: (np.random.default_rng().normal(0, asset.qualities[quality]/2) + asset.qualities[quality])
                    for quality in asset.qualities.keys()}
        # print(strategy)

        return strategy

    def set_bid(self):
        """ Return: sum the valuations for all qualities"""
        self.bid = sum(self.strategy.values())


    def get_bid(self):
        return self.bid


    def set_price_limit(self):
        # set a behavioral limit to check if they will pay or not.
        # if the price seems fair after it is set by the auction, let's pay it: but how do I embed this?