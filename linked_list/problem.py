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
    # problem one
    # *********************
    def __reverse__(self):
        pass

    # *********************
    # problem two
    # *********************
    def insert_advance(self, data, new_data, order):
        # Insert new data after the first data
        # order tells you which number the user has chosen
        new_node = Linked_list.Node(new_data)
        orginal = order
        curr = self.head
        while curr:
            # If find the location of that data
            if curr.data == data:
                if orginal == 1:
                # if orginal = 1, which means find the number
                # of element in the linked list
                    pass
                # Do four step
                # set new node's prev to curr
                # set new node's next to curr's next
                # set curr's next's prev to new node
                # set curr's next to new node
                # if the orginal is not 1, which means we did find 
                # the same elment but it is not the one we want, so we
                # go to next
                orginal -= 1
            # Look through the linked list
            curr = curr.next




    # test case
linked_list = Linked_list()

linked_list.insert_head(10)
linked_list.insert_head(6)
linked_list.insert_tail(5)
linked_list.insert_tail(10)
print(linked_list)
linked_list.insert_from(10, 3)
linked_list.insert_from(10, 12)
linked_list.insert_from(10, 18)
linked_list.insert_advance(10, 13, 2)
linked_list.insert_advance(13, 14, 2)
linked_list.insert_advance(14, 14, 1)
print(linked_list)

print(list(reversed(linked_list)))