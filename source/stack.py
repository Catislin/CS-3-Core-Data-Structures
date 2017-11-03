#!python

from linkedlist import LinkedList
from linkedlist import Node

class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.head is None

    def length(self):
        """Return the number of items in this stack."""
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) because we only have to reassign the head pointer
        which does not depend on the number of items in the list """
        new_node = Node(item)
        self.list.size += 1
        if self.list.head is None:
            self.list.head = new_node
            return
        new_node.next = self.list.head
        self.list.head = new_node

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if not self.list.is_empty():
            return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) because we only have to ressign the head pointer
        which doesn't depend on the length of the list """
        if self.list.is_empty():                            # first check if list is empty
            raise ValueError("Cannot pop from empty stack")  #raise ValueError if so
            return
        value_to_pop = self.list.head.data      # store value to be returned

        if self.length == 1:                    # case where list has one item (only the head)
            self.list.head = None
        else:
            new_head = self.list.head.next      # if the list has more than one item, assign the
            self.list.head = new_head           # new head to be the second item in the list

        self.list.size -= 1                     # update the list's size
        return value_to_pop                     # return the value of the old head


class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(n) because we have to copy over every item in the
        existing list """
        new_list = list()             # initialize a new list
        new_list.append(item)         # add the new item to the beginning of it
        for old_item in self.list:    # copy over every item in the current list
            new_list.append(old_item) # and add it to the end of the new list
        self.list = new_list          # set the ArrayStack's list to be the new list

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if not self.is_empty():
            return self.list[0]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(n) because we have to loop through each item in the list
        and copy it over to a new list """
        if self.is_empty():
            raise ValueError("Cannot pop from empty stack");
            return
        new_list = list()              # initialize a new list
        value_to_pop = self.list[0]    # store the first item in the ArrayStack for later
        for item in self.list[1::]:    # go through every item in the existing list
            new_list.append(item)      # starting w/ the 2nd element, add to new list
        self.list = new_list           # reassign the ArrayStack's list
        return value_to_pop



# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
