"""
Sets are a collection of unordered elements that are unique. Meaning that even if the data is repeated more than one
time, it would be entered into the set only once.
Set use Hash Tables for insertion/deletion and lookup operations.

Internal implementation:
https://www.geeksforgeeks.org/internal-working-of-set-in-python/

Time complexity:
https://www.geeksforgeeks.org/complexity-cheat-sheet-for-python-operations/
"""


def main():
    my_set = {1, 2, 3, 4, 5, 5, 5}
    print(my_set)

    my_set.add(6)
    print(my_set)

    first = {1, 2, 3, 4}
    second = {3, 4, 5, 6}
    print(first.union(second), '----------', first | second)
    print(first.intersection(second), '----------', first & second)
    print(first.difference(second), '----------', first - second)
    print(first.symmetric_difference(second), '----------', first ^ second)

    my_set.clear()
    print(my_set)


if __name__ == '__main__':
    main()
