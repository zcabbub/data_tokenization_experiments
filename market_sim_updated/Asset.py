import numpy as np

class DataAsset:
    def __init__(self):
        # values
        self.qualities = self._generate_qualities()
        # self.n_features = np.random.randint(1, 20)
        # self.fractions = self._generate_fractions(self.n_features)

    def _generate_qualities(self):
        qualities = {"consistency": 0,
                     "completeness": 0,
                     "timeliness": 0,
                     "accuracy": 0,
                     "privacy": 0,
                     "variety": 0}

        values = np.random.randint(1, 10, size=6)
        data_product = dict(zip(qualities, values))
        # print("Generated data product:", data_product)
        return data_product

    def _generate_fractions(self, n_features):
        """
        the agent chooses one. or more?

        :param n_features
        :return: list of 2^n-1 combinations of features
        """
        ...

    def get_fractions(self):
        return self.fractions

    def get_value(self):
        return sum(self.qualities.values())
