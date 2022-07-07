
class Linked_list():

    class Node():

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, data):
        new_node = Linked_list.Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, data):
        new_node = Linked_list.Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_from(self, data, new_data):
        curr = self.head
        while curr:
            if curr.data == data:
                new_node = Linked_list.Node(new_data)
                new_node.prev = curr
                new_node.next = curr.next
                curr.next.prev = new_node
                curr.next = new_node
                return

            curr = curr.next

    def remove_head(self):
        if self.head:
            self.head.next.prev = None
            self.head = self.head.next

    def remove_tail(self):
        if self.head:
            self.tail.prev.next = None
            self.tail = self.head.prev

    def __str__(self):
        output = ""
        curr = self.head
        while curr:
            output += str(curr.data)
            curr = curr.next
        return output

linked_list = Linked_list()

linked_list.insert_head(10)
linked_list.insert_head(7)
linked_list.insert_tail(5)
linked_list.insert_tail(9)
linked_list.insert_from(10, 3)

print(linked_list)

linked_list.remove_head()
linked_list.remove_tail()

print(linked_list)