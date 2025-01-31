class Endpoints:
    def __init__(self, ac):
        self.ac = ac
        self.LinkedList = Linkedlist()


class Node:
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value


class Linkedlist:
    def __init__(self, head=None):
        self.head = head
        self.tail = self.head

    def append(self, value):
        new_node = Node(value)

        if self.head is not None:
            self.tail.next, new_node.previous, self.tail = new_node, self.tail, new_node

        else:
            self.head = new_node
            self.tail = self.head

    def insert(self, value, key):
        temp = self.head
        new_node = Node(value)
        if self.tail is None:
            self.head, self.tail = new_node, self.head
            return

        if key is None:
            self.tail.next, new_node.previous, self.tail = new_node, self.tail, new_node
            return

        while temp.next is not None:
            if temp.value == key:
                break
            temp = temp.next

        temp.previous.next = new_node
        new_node.previous = temp.previous
        temp.previous = new_node
        new_node.next = temp

    def remove(self, value):
        if self.head is None or value is None:
            return
        temp = self.head
        while temp.next is not None:
            if temp.value == value:
                break
            temp = temp.next

        if temp.previous is not None:
            temp.next.previous, temp.previous.next = temp.previous, temp.next

        elif temp.previous is None:
            temp.next.previous = temp.previous
            self.head = temp.next

    def to_string(self):
        if self.head is None:
            return
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
