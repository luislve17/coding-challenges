"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

class OrderPile():
    def __init__(self):
        self._container = []

    def record(self, order_id): # push action
        self._container.append(order_id)

    def get_last(self, i): # pop action
        pile_length = len(self._container)
        i_from_last = pile_length -  i - 1
        if i_from_last >= len(self._container) or i_from_last < 0: return None
        return self._container[i_from_last]

# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
order_pile = OrderPile()
for id in range(10,21):
    order_pile.record(id)

for index in range(-1, 12):
    print(order_pile.get_last(index))

