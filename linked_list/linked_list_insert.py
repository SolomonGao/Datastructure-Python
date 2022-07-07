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
        # Size + 1
        self.size += 1

    def insert_tail(self, data):
        # Create a new node
        new_node = Linked_list.Node(data)
        # set new node's prev to the tail
        # set head's next to the new node
        # set tail to new node
        pass


    def insert_from(self, data, new_data):
        # Insert new data after the first data
        # Create a new node
        new_node = Linked_list.Node(new_data)
        curr = self.head
        while curr:
            # If find the location of that data
            if curr.data == data:
                # if the data is at the tail
                if curr == self.tail:
                    pass
                else:
                # Do four step
                # set new node's prev to curr
                # set new node's next to curr's next
                # set curr's next's prev to new node
                # set curr's next to new node
                    pass
                return
            # Look through the linked list
            curr = curr.next
        print("Did not find {} in the linked list.".format(data))
