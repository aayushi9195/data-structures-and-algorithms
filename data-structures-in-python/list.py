"""
Lists are used to store data of different data types in a sequential manner.
Lists are similar to arrays with bidirectional adding and deleting capability.
Arrays and lists are the same structure with one difference. Lists allow heterogeneous data element storage whereas
arrays allow only homogeneous elements to be stored within them.

Internal implementation:
https://www.geeksforgeeks.org/internal-working-of-list-in-python/

Time complexity:
https://www.geeksforgeeks.org/complexity-cheat-sheet-for-python-operations/

Why is clear O(1)? - CPython implementation of list.clear is O(n). The code iterates over the elements in order to
decrease the reference count of each one, without a way to avoid it. While CPython's list.clear has to touch every element
to avoid a memory leak, it is quite possible that PyPy's garbage collector never needs to do anything of the sort, and
thus has a true O(1) list.clear.

What is the initial capacity of a list? - http://www.laurentluce.com/posts/python-list-implementation/
"""


def main():
    my_list = []  # creating empty list
    print(my_list)
    my_list = [1, 2, 3, 'example', 3.132]  # creating list with data
    print(my_list)

    my_list.append([555, 12])  # add as a single element
    print(my_list)
    my_list.extend([234, 'more_example'])  # add as different elements
    print(my_list)
    my_list.insert(1, 'insert_example')  # add element at i
    print(my_list)

    del my_list[5]  # deletes element at index 5, does not return anything
    print(my_list)
    my_list.remove('example')  # remove element with value
    print(my_list)
    a = my_list.pop(1)  # pop element from list
    print('Popped Element: ', a, ' List remaining: ', my_list)
    my_list.clear()  # empty the list
    print(my_list)

    my_list = [1, 2, 3, 'example', 3.132, 10, 30]
    for element in my_list:  # access elements one by one
        print(element)
    print(my_list)  # access all elements
    print(my_list[3])  # access index 3 element
    print(my_list[0:2])  # access elements from 0 to 1 and exclude 2
    print(my_list[::-1])  # access elements in reverse

    my_list = [1, 2, 3, 10, 30, 10]
    print(len(my_list))  # find length of list
    print(my_list.index(10))  # find index of element that occurs first
    print(my_list.count(10))  # find count of the element [Time: O(N)]
    print(sorted(my_list))  # print sorted list but not change original
    my_list.sort(reverse=True)  # sort original list
    print(my_list)


if __name__ == '__main__':
    main()

