#Author: Xing Gao
class Linked_list():

    class Node():

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, data):
        # Create a new node
        new_node = Linked_list.Node(data)
        # Check the linked list has data in it or not 
        if not self.head:
            # If not, just set new node to the head and tail
            self.head = new_node
            self.tail = new_node
        # If it has data, do three step
        # set new node's next to the head
        # set head's prev to the new node
        # set head to new node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_tail(self, data):
        new_node = Linked_list.Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        # If it has data, do three step
        # set new node's prev to the tail
        # set head's next to the new node
        # set tail to new node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_from(self, data, new_data):
        # Insert new data after the first data
        # Create a new node
        new_node = Linked_list.Node(new_data)
        curr = self.head
        while curr:
            # If find the location of that data
            if curr.data == data:
                if curr == self.tail:
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                else:
                # Do four step
                # set new node's prev to curr
                # set new node's next to curr's next
                # set curr's next's prev to new node
                # set curr's next to new node
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                    self.size += 1
                return
            # Look through the linked list
            curr = curr.next
        print("Did not find {} in the linked list.".format(data))

    def remove_from(self, data):
        # remove the first data from the linked list
        curr = self.head
        while curr:
            if curr.data == data:
                curr.next.prev = curr.prev
                curr.prev.next = curr.next
                self.size -= 1
                return
            curr = curr.next
        print("Did not find {} in the linked list.".format(data))

    def remove_head(self):
        # If there is a node in the head
        if self.head:
            # set head's next node's prev to None
            self.head.next.prev = None
            # set head to head's next node
            self.head = self.head.next
            self.size -= 1
        else:
            print("Empty linked list.")

    def remove_tail(self):
        if self.head:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.size -= 1
        else:
            print("Empty linked list.")

    def __str__(self):
        output = "("
        curr = self.head
        while curr:
            if curr.next: 
                output += str(curr.data) + ", "
            else:
                output += str(curr.data)
            curr = curr.next
        output += ")"
        return output

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def get_size(self):
        return self.size

    # *********************
    # example
    # *********************
    def __reversed__(self):
        curr = self.tail
        while curr:
            yield curr.data
            curr = curr.prev

    # *********************
    # problem
    # *********************
    def cut(self, data):
        # cut this linked list from the first data and reverse two parts
        curr = self.head
        while curr:
            if curr.data == data:
                # if the data is the tail, do nothing
                if curr == self.tail:
                    pass
                else:
                    # connect head and tail by seting head.prev
                    # to self.tail and tail.next to self.head
                    # set head to curr.next
                    # set tail to curr
                    # set head.prev to None
                    # set tail.next to None
                    self.head.prev = self.tail
                    self.tail.next = self.head
                    self.head = curr.next
                    self.head.prev = None
                    self.tail = curr
                    self.tail.next = None
                return
            curr = curr.next
        print("{} is not in the linked list.".format(data))


linked_list = Linked_list()

linked_list.insert_head(10)
linked_list.insert_head(6)
linked_list.insert_tail(5)
linked_list.insert_tail(14)
print(linked_list)
linked_list.insert_from(10, 3)
linked_list.insert_from(10, 12)
linked_list.insert_from(10, 18)
print(linked_list)
# Example
print(list(reversed(linked_list)))
# Problem
linked_list.cut(18)
linked_list.cut(36)
print(linked_list)
