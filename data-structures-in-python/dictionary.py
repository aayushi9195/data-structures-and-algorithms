"""
A dictionary key must be of a type that is immutable. For example, you can use an integer, float, string, tuple or Boolean
as a dictionary key. However, neither a list nor another dictionary can serve as a dictionary key, because lists and
dictionaries are mutable. Values, on the other hand, can be any type and can be used more than once.
A given key can appear in a dictionary only once. Duplicate keys are not allowed.
Dictionaries use Hash Tables for insertion/deletion and lookup operations.

Internal implementation:
https://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented
https://en.wikipedia.org/wiki/Hash_table#Open_addressing
https://www.geeksforgeeks.org/python-3-6-dictionary-implementation-using-hash-tables/

Time complexity:
https://www.geeksforgeeks.org/complexity-cheat-sheet-for-python-operations/

HashMaps are same as dictionaries.
"""


def main():
    my_dict = dict()  # empty dictionary
    print(my_dict)
    my_dict = {1: 'Python', 2: 'Java'}  # dictionary with elements
    print(my_dict)
    my_dict[1] = 'CPP'  # change element
    print(my_dict)
    my_dict[3] = 'Ruby'
    print(my_dict)

    my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
    a = my_dict.pop('Third')  # pop element
    print('Value:', a)
    print('Dictionary:', my_dict)
    b = my_dict.popitem()  # pop the key-value pair
    print('Key, value pair:', b)
    print('Dictionary', my_dict)
    my_dict.clear()  # empty dictionary
    print(my_dict)

    my_dict = {'First': 'Python', 'Second': 'Java'}
    print(my_dict['First'])  # access elements using keys
    print(my_dict.get('Second'))
    my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
    print(my_dict.keys())  # get keys
    print(my_dict.values())  # get values
    print(my_dict.items())  # get key-value pairs


if __name__ == '__main__':
    main()
