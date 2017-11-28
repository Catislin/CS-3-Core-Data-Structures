from binarytree import BinarySearchTree
from hashtable import HashTable

class TreeMap(HashTable):
    def __init__(self, init_size=8):
        self.buckets = [BinarySearchTree() for i in range(init_size)]
        self.size = 0

if __name__ == '__main__':
    treemap = TreeMap()
    treemap.set('A', 3)
    print('value ' + str(treemap.get('A')))
