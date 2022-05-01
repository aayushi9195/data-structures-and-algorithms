"""
Tuples are the same as lists are with the exception that the data once entered into the tuple cannot be changed no
matter what. The only exception is when the data inside the tuple is mutable, only then the tuple data can be changed.

Time complexity:
Tuples have the same operations (non-mutable) and complexities as lists.
"""


def main():
    my_tuple = (1, 2, 3)  # create tuple
    print(my_tuple)

    my_tuple = (1, 2, 3, 'edureka')  # access elements
    for x in my_tuple:
        print(x)
    print(my_tuple)
    print(my_tuple[0])
    print(my_tuple[:])
    print(my_tuple[3][4])

    my_tuple = (1, 2, 3)
    my_tuple = my_tuple + (4, 5, 6)  # add elements
    print(my_tuple)

    my_tuple = (1, 2, 3, ['hindi', 'python'])
    my_tuple[3][0] = 'english'
    print(my_tuple)
    print(my_tuple.count(2))
    print(my_tuple.index(['english', 'python']))


if __name__ == '__main__':
    main()