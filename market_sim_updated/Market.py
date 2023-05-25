from dataclasses import dataclass
from typing import List


@dataclass
class Order(object):
    id: int
    creator_id: int
    type: bool # false: bid; true: ask
    price: int


class Market(object):
    def __init__(self):
        # the orderbook
        self.bids: List[Order] = []
        self.asks: List[Order] = []

    def add_order(self, order: Order):
        # if bid
        if not order.type:
            self.bids.append(order)
        else:
            self.asks.append(order)

    def delete_order(self, order: Order):
        # if bid
        if not order.type:
            self.bids.remove(order)
        else:
            self.asks.remove(order)




# inspiration: https://www.noveltech.dev/simulation-market-python/