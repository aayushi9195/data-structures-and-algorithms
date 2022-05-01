"""
As a stack, the queue is a linear data structure that stores items in a First In First Out (FIFO) manner.

Operations:
Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition
 – Time Complexity: O(1)
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue
 is empty, then it is said to be an Underflow condition – Time Complexity: O(1)
Front: Get the front item from queue – Time Complexity: O(1)
Rear: Get the last item from queue – Time Complexity: O(1)

Ways of implementation:
list
Collections.deque
queue.Queue
"""


def main():
    queue = []
    queue.append('a')
    queue.append('b')
    queue.append('c')
    print('Initial queue')
    print(queue)
    print("\nElements dequeued from queue")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    print("\nQueue after removing elements")
    print(queue)
    # queue.pop(0) will cause an IndexError as the queue is now empty

    # Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends
    # of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list
    # which provides O(n) time complexity.
    from Lib.collections import deque
    queue = deque()
    queue.append('a')
    queue.append('b')
    queue.append('c')
    print('Initial queue')
    print(queue)
    print('\nElements removed from the queue')
    queue.popleft()
    queue.popleft()
    queue.popleft()
    print('\nQueue after removing elements')
    print(queue)
    # queue.popleft() will cause an IndexError as the queue is now empty

    # queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. A maxsize of zero ‘0’ means an
    # infinite queue. This Queue follows the FIFO rule.
    from Lib.queue import Queue
    queue = Queue(maxsize=3)
    print(queue.qsize())
    queue.put('a')
    queue.put('b')
    queue.put('c')
    print("\nFull: ", queue.full())
    print("\nElements removed from the queue")
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print("\nEmpty: ", queue.empty())
    queue.put(1)
    print("\nEmpty: ", queue.empty())
    print("Full: ", queue.full())
    # This would result into Infinite Loop as the Queue is empty.
    # print(queue.get())


if __name__ == '__main__':
    main()