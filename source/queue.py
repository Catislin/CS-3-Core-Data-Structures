#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(LinkedList):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        super().__init__(iterable)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.head is None

    def length(self):
        """Return the number of items in this queue."""
        return self.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue. """

        """Running time: O(1) because since we have a reference to the
        tail of the linked list, we can just reassign its next pointer
        to point to the new node """

        self.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.head:
            return self.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty. """

        """Running time: O(1) because we just have to reassign the head pointer
        variable, which is constant time  """

        if self.head:
            value_to_deQ = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value_to_deQ
        raise ValueError("Cannot dequeue from empty queue")

# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue. """

        """ Running time: O(1) best case if the total size of the space allocated
        for the array is larger than the number of items in the array, then we can
        just reassign the value after the last filled index, which is a constant
        time operation.

        O(n) worst case if the allocated space for the array is already filled,
        in which case we have to reallocate another larger array and copy each
        item over to that new array """

        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty. O(1) time to access by index"""
        if not self.is_empty():
            return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty. """

        """Running time: O(n) because we have to shift all elements over """
        if not self.is_empty():
            new_list = list()            # initialize a new list to copy items to
            value_to_deQ = self.list[0]  # store value at front of list to return later
            # for item in self.list[1:]:  # starting w/ 2nd element
            #     new_list.append(item)    # copy all items to new list
            #self.list = new_list         # reassign the queue's list
            self.list = self.list[1:]

            return value_to_deQ
        raise ValueError("Cannot dequeue from empty queue")



# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
