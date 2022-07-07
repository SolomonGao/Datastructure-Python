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
            # set tail's prev node's next to None
            # set tail to tail's prev node
            pass
        else:
            print("Empty linked list.")

    def remove_from(self, data):
        # remove the first data from the linked list
        curr = self.head
        while curr:
            if curr.data == data:
                # set curr's next node's prev to curr's prev node
                # set curr's prev node's next to curr's next node
                pass
                self.size -= 1
                return
            curr = curr.next
        print("Did not find {} in the linked list.".format(data))