from binarytree import BinarySearchTree

class TreeMap(hashtable):
    def __init__(self, init_size=8):
        self.buckets = [BinarySearchTree() for i in range(init_size)]



if __name__ == '__main__':
    treemap = TreeMap()
    treemap.set('A', 3)
