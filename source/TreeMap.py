from binarytree import BinarySearchTree

class TreeMap(hashtable):
    def __init__(self, init_size=8):
        self.buckets = [BinarySearchTree() for i in range(init_size)]

    def 
