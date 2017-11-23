
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList(object):
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0

        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, item):
        """Adds an item to the end of the list"""
        new_node = Node(item)        # create a new node

        if not self.head:            # case where the list is empty
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node    # have the tail point towards the new node
        new_node.prev = self.tail    # the new node points back at the old tail
        self.tail = new_node         # and the new node is the new tail of the list

        self.size += 1               # record that the list's size has increased


    def prepend(self, item):
        """Adds an item to the beginning of the list"""
        new_node = Node(item)

        if not self.head:              # if the list is empty
            self.head = new_node       # then make the list's head and tail be
            self.tail = new_node       # the new node
            return

        new_node.next = self.head  # otherwise have the new node point towards the old head
        self.head.prev = new_node  # have the old head point back at the new node
        self.head = new_node       # and make the new node the new head

        self.size += 1                 # record that the list's size has increased

    def get_at_index(self, index):
        """Returns the item at the specified index"""
        if index > self.size:
            raise IndexError("Index out of range")
            return

        mid = self.size // 2           # find the middle index of the list

        if index < mid:                # if the index we want is towards the front
            current = self.head
            for i in range(index):     # then we want to loop from the head to index
                current = current.next
            return current.data
        else:
            current = self.tail        # otherwise, loop from the tail backwards
            for i in range(self.size - index):
                current = current.prev
            return current.data

    def insert_at_index(self, item, index):
        """Inserts an item at a specific index"""
        if index == self.size:
            self.append(item)
            return
        if index == 0:
            self.prepend(item)
            return
        if index > self.size:
            raise IndexError("Index out of range")
            return

        mid = self.size // 2
        new_node = Node(item)

        if index < mid:
            current = self.head
            for i in range(index):
                current = current.next
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
        else:
            current = self.tail
            for i in range(self.size - index):
                current = current.prev
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node


    def delete(self, item):
        """Removes the first instance of an item from the list"""
        prev = self.head

        if prev.data == item:              # case where we delete the first item
            self.head = prev.next
            if not prev.next:              # case where the item to be deleted
                self.tail = None           # is the only item in the list
            return

        while prev.next:
            current = prev.next
            if current.data == item:
                if current is self.tail:     # deleting the last item in the list
                    self.tail = prev
                    prev.next = None
                    self.size -= 1
                    return
                else:
                    prev.next.next = prev.next    # have the node just before the deleted item point after it
                    prev.next.prev = prev         # and have the new next node point back at the one before the deleted item
                    self.size -= 1
                    return










if __name__ == '__main__':
    print('I am a doubly linked list')
