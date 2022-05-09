"""
Merge sort:
Time Complexity: O(N * Log N) in all 3 cases (worst, average and best) as it always divides the array into two halves
and takes linear time to merge two halves.
Auxiliary Space: O(n)
Algorithmic Paradigm: Divide and Conquer
Sorting In Place: No in a typical implementation
Stable: Yes

Quick sort:
https://www.geeksforgeeks.org/quick-sort/

Insertion sort:
Time Complexity: O(n^2)
Auxiliary Space: O(1)
Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum
time (Order of n) when elements are already sorted.
Algorithmic Paradigm: Incremental Approach
Sorting In Place: Yes
Stable: Yes
Online: Yes
Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted,
only few elements are misplaced in complete big array.
"""


def merge_sort(arr):
    return merge_sort_util(arr, 0, len(arr)-1)


def merge_sort_util(arr, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort_util(arr, low, mid)
        merge_sort_util(arr, mid+1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    m, n = mid-low+1, high-mid
    left, right = [0]*m, [0]*n
    for i in range(0, m):
        left[i] = arr[low+i]
    for i in range(0, n):
        right[i] = arr[mid+1+i]
    i, j, k = 0, 0, low
    while i < m and j < n:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < m:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n:
        arr[k] = right[j]
        j += 1
        k += 1


def quick_sort(arr):
    return quick_sort_util(arr, 0, len(arr)-1)


def quick_sort_util(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_util(arr, low, pi-1)
        quick_sort_util(arr, pi+1, high)


def partition(arr, low, high):
    i = (low-1)
    pi = arr[high]
    for j in range(low, high):
        if arr[j] <= pi:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i-1
        while j >= 0 and arr[j] > curr:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr


def main():
    arrays = [[12, 11, 13, 5, 6, 7], [], [1], [1, 0], [1, 2, 3], [10, 7, 4, 1], [1, 1, 1, 1, 1]]
    for array in arrays:
        merge_sort(array)
        print('Merge sort:', array)
        quick_sort(array)
        print('Quick sort:', array)
        insertion_sort(array)
        print('Insertion sort:', array)


if __name__ == "__main__":
    main()

