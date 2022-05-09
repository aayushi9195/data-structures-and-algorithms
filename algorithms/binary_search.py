"""
Binary search implementation:
Recursive
Iterative
Bisect algorithm - https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/

Time complexity in each case: O(log N)
"""

import bisect


def binary_search_recursive(arr, x):
    return binary_search_util(arr, 0, len(arr)-1, x)


def binary_search_util(arr, low, high, x):
    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            return binary_search_util(arr, mid+1, high, x)
        elif arr[mid] > x:
            return binary_search_util(arr, low, mid-1, x)
        else:
            return mid
    else:
        return -1


def binary_search_iterative(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def array_bisect(arr, x):
    ind = bisect.bisect_left(arr, x)
    if ind < len(arr) and arr[ind] == x:
        return ind
    return -1


def main():
    # iterative
    arr = [2, 3, 4, 10, 40]
    print("{} is found at {}".format(10, binary_search_iterative(arr, 10)))
    print("{} is found at {}".format(2, binary_search_iterative(arr, 2)))
    print("{} is found at {}".format(40, binary_search_iterative(arr, 40)))
    print("{} is found at {}".format(3, binary_search_iterative(arr, 3)))
    print("{} is found at {}".format(4, binary_search_iterative(arr, 4)))
    print("{} is found at {}".format(5, binary_search_iterative(arr, 5)))
    print("{} is found at {}".format(5, binary_search_iterative([], 5)))
    print("{} is found at {}".format(5, binary_search_iterative([0], 5)))
    print("{} is found at {}".format(5, binary_search_iterative([5], 5)))
    print("{} is found at {}".format(5, binary_search_iterative([0, 1], 5)))
    print("{} is found at {}".format(5, binary_search_iterative([5, 5], 5)))

    # recursive
    arr = [2, 3, 4, 10, 40]
    print("{} is found at {}".format(10, binary_search_recursive(arr, 10)))
    print("{} is found at {}".format(2, binary_search_recursive(arr, 2)))
    print("{} is found at {}".format(40, binary_search_recursive(arr, 40)))
    print("{} is found at {}".format(3, binary_search_recursive(arr, 3)))
    print("{} is found at {}".format(4, binary_search_recursive(arr, 4)))
    print("{} is found at {}".format(5, binary_search_recursive(arr, 5)))
    print("{} is found at {}".format(5, binary_search_recursive([], 5)))
    print("{} is found at {}".format(5, binary_search_recursive([0], 5)))
    print("{} is found at {}".format(5, binary_search_recursive([5], 5)))
    print("{} is found at {}".format(5, binary_search_recursive([0, 1], 5)))
    print("{} is found at {}".format(5, binary_search_recursive([5, 5], 5)))

    # bisect
    arr = [2, 3, 4, 10, 40]
    print("{} is found at {}".format(10, array_bisect(arr, 10)))
    print("{} is found at {}".format(2, array_bisect(arr, 2)))
    print("{} is found at {}".format(40, array_bisect(arr, 40)))
    print("{} is found at {}".format(3, array_bisect(arr, 3)))
    print("{} is found at {}".format(4, array_bisect(arr, 4)))
    print("{} is found at {}".format(5, array_bisect(arr, 5)))
    print("{} is found at {}".format(5, array_bisect([], 5)))
    print("{} is found at {}".format(5, array_bisect([0], 5)))
    print("{} is found at {}".format(5, array_bisect([5], 5)))
    print("{} is found at {}".format(5, array_bisect([0, 1], 5)))
    print("{} is found at {}".format(5, array_bisect([5, 5], 5)))
    print("{} is found at {}".format(5, array_bisect([5, 5], 5)))


if __name__ == "__main__":
    main()