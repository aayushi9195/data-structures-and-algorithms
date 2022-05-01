"""
Time complexity:
https://www.geeksforgeeks.org/time-complexities-of-different-data-structures/

Memory efficiency:
Because the data stored in arrays is tightly packed they’re generally more space-efficient than linked lists.
This mostly applies to static arrays, however. Dynamic arrays typically over-allocate their backing store slightly to
speed up element insertions in the average case, thus increasing the memory footprint.
"""


class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_node = DNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

    def push_back(self, new_data):
        new_node = DNode(new_data)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = None

    def peek_front(self):
        if not self.head:
            print("List is empty")
        else:
            return self.head.data

    def peek_back(self):
        if not self.tail:
            print("List is empty")
        else:
            return self.tail.data

    def pop_front(self):
        if not self.head:
            print("List is empty")
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            return temp.data

    def pop_back(self):
        if not self.tail:
            print("List is empty")
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            return temp.data

    def insert_after(self, temp_node_data, new_data):
        temp_node = self.head
        while temp_node and temp_node.data != temp_node_data:
            temp_node = temp_node.next
        if not temp_node:
            print("Given node is empty")
        else:
            new_node = DNode(new_data)
            new_node.next = temp_node.next
            temp_node.next = new_node
            new_node.prev = temp_node
            if new_node.next:
                new_node.next.prev = new_node
            if temp_node == self.tail:
                self.tail = new_node

    def insert_before(self, temp_node_data, new_data):
        temp_node = self.head
        while temp_node and temp_node.data != temp_node_data:
            temp_node = temp_node.next
        if not temp_node:
            print("Given node is empty")
        else:
            new_node = DNode(new_data)
            new_node.prev = temp_node.prev
            temp_node.prev = new_node
            new_node.next = temp_node
            if new_node.prev:
                new_node.prev.next = new_node
            if temp_node == self.head:
                self.head = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


def main():
    print('---Singly Linked List---')
    slinkedlist = SinglyLinkedList()
    slinkedlist.head = SNode(1)
    slinkedlist.head.next = SNode(2)
    slinkedlist.head.next.next = SNode(3)
    slinkedlist.print()
    print('---Doubly Linked List---')
    dlinkedlist = DoublyLinkedList()
    dlinkedlist.push_front(1)
    dlinkedlist.push_front(2)
    dlinkedlist.push_front(3)
    dlinkedlist.push_back(4)
    dlinkedlist.push_back(5)
    print('Front', dlinkedlist.peek_front())
    print('Back', dlinkedlist.peek_back())
    dlinkedlist.print()
    print('\nPopped front', dlinkedlist.pop_front())
    print('Popped back', dlinkedlist.pop_back())
    dlinkedlist.print()
    print('\n')
    dlinkedlist.insert_after(1, 6)
    dlinkedlist.insert_before(4, 7)
    dlinkedlist.insert_before(2, 8)
    dlinkedlist.print()


if __name__ == "__main__":
    main()