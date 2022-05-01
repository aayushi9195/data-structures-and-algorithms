"""
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.

Operations:
empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
https://wiki.python.org/moin/TimeComplexity

Ways of implementation:
list
Collections.deque
queue.LifoQueue

Deque internal implementation:
https://stackoverflow.com/questions/6256983/how-are-deques-in-python-implemented-and-when-are-they-worse-than-lists
https://www.geeksforgeeks.org/python-queue-lifoqueue-vs-collections-deque/
"""


def main():
    stack = []
    stack.append('a')
    stack.append('b')
    stack.append('c')
    print('Initial stack')
    print(stack)
    print('Elements popped from stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print('Stack after elements are popped:')
    print(stack)
    # stack.pop() will cause an IndexError as the stack is now empty

    # Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends
    # of the container, as deque provides O(1) time complexity for append and pop operations as compared to list which
    # provides O(n) time complexity.
    from collections import deque
    stack = deque()
    stack.append('a')
    stack.append('b')
    stack.append('c')
    print('\nInitial stack')
    print(stack)
    print('Elements popped from stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print('Stack after elements are popped:')
    print(stack)

    # The queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put()
    # function and get() takes data out from the Queue.
    from Lib.queue import LifoQueue
    stack = LifoQueue(maxsize=3)
    print('\n')
    print(stack.qsize())
    stack.put('a')
    stack.put('b')
    stack.put('c')
    print("Full: ", stack.full())
    print("Size: ", stack.qsize())
    print('Elements popped from the stack')
    print(stack.get())
    print(stack.get())
    print(stack.get())
    print("Empty:", stack.empty())


if __name__ == '__main__':
    main()