"""
Heap data structure is mainly used to represent a priority queue.
heapq module is a collection of methods that allows us to use lists as binary min-heaps.

If you need to compare against multiple fields to find out which element is smaller or bigger, consider having the
heap’s elements be tuples.

Applications:
https://www.geeksforgeeks.org/applications-of-heap-data-structure/

Time complexity:
heapify - O(N), in-place
heappush - O(logN)
heappop - O(logN)
heappushpop - slightly more efficient than calling heappush and heappop individually
heapreplace - slightly more efficient than calling heappop and heappush individually
nlargest - O(N+klogN) [equivalent to sorted(iterable, key=key, reverse=True)[:n] which takes O(NlogN)]
nsmallest -  O(N+klogN) [equivalent to sorted(iterable, key=key)[:n] which takes O(NlogN)]
merge - takes more time than k-way merge (itertools.chain.from_iterable + sorted) but way more memory efficient
https://stackoverflow.com/questions/23038756/what-is-the-time-complexity-of-heapq-nlargest

Should we use sorted or list.sort? And what about min and max?
If you only need the single largest or smallest record (k=1), then use min or max.
If k is "small" -- compared to the size of the dataset -- then use heapq.nsmallest and heapq.nlargest.
Otherwise, use sorted or list.sort.
Reason -- in theory, even though the time complexity of heapq.nsmallest will always be at least as good as that of
sorting, O(nlogn) -- in practice, Python's timsort may be quicker when k is close to n.
"""

import heapq
import sys


def heap_lib():
    li = [5, 7, 9, 1, 3]

    heapq.heapify(li)

    print("The created heap is : ", end="")
    print(li)

    heapq.heappush(li, 4)
    print("The modified heap after push is : ", end="")
    print(li)

    print("The popped and smallest element is : ", end="")
    print(heapq.heappop(li))

    print("Current heap : ", end="")
    print(li)

    # using heappushpop() to push and pop items simultaneously
    # pops 2
    print("The popped item using heappushpop() is : ", end="")
    print(heapq.heappushpop(li, 2))

    # using heapreplace() to push and pop items simultaneously
    # pops 3
    print("The popped item using heapreplace() is : ", end="")
    print(heapq.heapreplace(li, 2))

    print("Current heap : ", end="")
    print(li)

    print("The 3 largest numbers in list are : ", end="")
    print(heapq.nlargest(3, li))

    print("The 3 smallest numbers in list are : ", end="")
    print(heapq.nsmallest(3, li))


class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (maxsize + 1)
        self.heap[0] = -1 * sys.maxsize
        self.front = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return 2 * pos + 1

    def isLeaf(self, pos):
        return pos * 2 > self.size

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if self.heap[pos] > self.heap[self.leftChild(pos)] or self.heap[pos] > self.heap[self.rightChild(pos)]:
                if self.heap[self.leftChild(pos)] < self.heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = element
        current = self.size
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.minHeapify(self.front)
        return popped

    def print(self):
        for i in range(1, (self.size//2)+1):
            print("Parent:", self.heap[i], "Left child:", self.heap[2*i], "Right child:", self.heap[2*i+1])


def main():
    # heapq implementation
    heap_lib()
    print('\n')

    # array implementation
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()
    minHeap.print()
    print("The min val is " + str(minHeap.remove()))


if __name__ == '__main__':
    main()
