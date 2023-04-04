import numpy as np

class Agent():
    def __init__(self, iid, asset):
        # define strategy
        self.iid = iid
        # agent's own asset valuation strategy
        self.strategy = self.generate_new_strategy(asset)

    def generate_new_strategy(self, asset):
        # generate agent's valuation according the asset qualities
        # 66% of the data should fall within one standard deviation of the mean, [mu - sigma, mu + sigma]
        strategy = {quality: np.random.default_rng().normal(asset.qualities[quality], scale=1) for quality in asset.qualities.keys()}
        print(strategy)

        return strategy

    def get_bid(self):
        return sum(self.strategy.values())