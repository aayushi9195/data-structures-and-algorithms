"""
Monotonic Queue is a data structure that keeps it’s elements either entirely in non-increasing, or entirely in
non-decreasing order.

https://1e9.medium.com/monotonic-queue-notes-980a019d5793
"""
from collections import deque


class Item:
    def __init__(self, val, ind):
        self.val = val
        self.ind = ind


# increasing monotonic queue
class MQ:
    def __init__(self, default_nearest_value, n):
        self.queue = deque()
        self.default_nearest_value = default_nearest_value
        # nearest value indices
        self.nearest = [0] * n

    def push(self, new_item):
        # if the last element in the queue is bigger, we remove it
        # so we could keep an increasing sequence
        while self.queue and new_item.val <= self.queue[-1].val:
            self.queue.pop()

        # the nearest smallest item will be at the end of the queue
        # since we removed all the values that are bigger then the current
        if self.queue:
            self.nearest[new_item.ind] = self.queue[-1].ind

        # if we can't find the nearest smallest value from the array
        # we will take the default one
        else:
            self.nearest[new_item.ind] = self.default_nearest_value

        # now we can push the new element as the queue is monotonic
        self.queue.append(new_item)
