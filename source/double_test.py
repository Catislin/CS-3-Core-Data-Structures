
from doublylinked import DoublyLinkedList, Node
import unittest

class NodeTest(unittest.TestCase):

    def test_init(self):
        node = Node('a')
        assert node.data == 'a'
        assert node.prev is None
        assert node.next is None

class LinkedListTest(unittest.TestCase):

    def test_init(self):
        # without items
        dll = DoublyLinkedList()
        assert dll.head is None
        assert dll.tail is None

    def test_append(self):
        dll = DoublyLinkedList()
        dll.append('A')
        assert dll.head.data == 'A'
        assert dll.tail.data == 'A'
        dll.append('B')
        assert dll.head.data == 'A'
        assert dll.tail.data == 'B'

    def test_prepend(self):
        dll = DoublyLinkedList()
        dll.prepend('A')
        assert dll.head.data == 'A'

    def test_delete(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.delete('A')
        assert dll.head is None
        assert dll.tail is None
        dll.append('A')
        dll.append('B')
        dll.delete('B')
        assert dll.head.data == 'A'
        assert dll.tail.data == 'A'
        dll.append('B')
        dll.append('C')
        dll.append('D')
        dll.delete('B')
        assert dll.tail.data == 'D'
        assert dll.head.data == 'A'

    def test_get_at_index(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.append('B')
        dll.append('C')
        assert dll.get_at_index(0) == 'A'
        assert dll.get_at_index(1) == 'B'
        assert dll.get_at_index(2) == 'C'
        dll.append('D')
        assert dll.get_at_index(3) == 'D'

    def test_insert_at_index(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.append('B')
        dll.append('D')
        dll.insert_at_index('C', 1)
        assert dll.get_at_index(1) == 'C'
        dll.insert_at_index('D', 0)
        assert dll.get_at_index(0) == 'D'
        dll.insert_at_index('E', 2)
        assert dll.get_at_index(2) == 'E'


if __name__ == '__main__':
    unittest.main()
