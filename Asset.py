import numpy as np

class DataAsset:
    def __init__(self):
        # values
        self.qualities = self._generate_qualities()

    def _generate_qualities(self):
        qualities = {"consistency": 0,
                     "completeness": 0,
                     "timeliness": 0,
                     "accuracy": 0,
                     "privacy": 0,
                     "variety": 0}

        # TODO: maybe use a normal distribution to generate the asset qualities
        data_product = {quality: np.random.randint(1, 10) for quality in qualities}

        print("Generated data product:", data_product)

        return data_product

    def get_value(self):
        return sum(self.qualities.values())
