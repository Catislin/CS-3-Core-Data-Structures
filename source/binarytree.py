#!python
from queue import LinkedQueue

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        return not self.left and not self.right

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # Check if either left child or right child has a value
        return (self.left is not None) or (self.right is not None)

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best case running time: O(1) if tree is empty
        Worst case running time: O(n) if the tree is on one long branch"""
        right_height, left_height = 0, 0
        # base case
        if self.is_leaf():
            return 0
        if self.right:
            right_height = self.right.height() # use ternary
        if self.left:
            left_height = self.left.height()
        return max(left_height, right_height) + 1


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def items(self):
        """Returns a list of all items in the tree, in-order"""
        items = []
        self._traverse_in_order_recursive(self.root, items.append)
        return items

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        # Check if root node has a value and if so calculate its height
        if self.root:
            return self.root.height()
        else:
            return 0

    def length(self):
        """Returns the number of items in the tree"""
        return self.size

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what \?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item)
        # Return the node's data if found, or None
        if node:
            return node.data
        else:
            return None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        newNode = BinaryTreeNode(item)
        if self.is_empty():
            # Create a new root node
            self.root = newNode
            # Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node(item)
        # Check if the given item should be inserted left of parent node
        if item < parent.data:
            #  Create a new node and set the parent's left child
            parent.left = newNode
        # Check if the given item should be inserted right of parent node
        elif item > parent.data:
            # Create a new node and set the parent's right child
            parent.right = newNode
        # Increase the tree size
        self.size += 1

    # swaps two nodes
    def swap(self, a, b):
        # swap data
        a_data = a.data
        b_data = b.data
        a.data = b_data
        b.data = a_data
        # swap child pointers
        a_left = a.left
        a_right = a.right
        a.left = b.left
        a.right = b.right
        b.left = a_left
        b.right = a_right

    def _find_successor(self, node):
        # if the node has a right child, then:
        # find the leftmost (that is, the smallest) node in the right subtree
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current

        # otherwise, if the node has no right child
        # then start from the root and search for the largest node that comes
        # before it in the tree
        current = self.root
        succ = None
        while current:
            if node.data > current.data:
                current = current.right
            elif node.data < current.data:
                succ = current
                current = current.left
            else:
                break
        return succ

    def delete(self, item, root=None):
        if not root:
            found = self._find_node_recursive(item)
        else:
            found = self._find_node_recursive(item, root)

        if found is not None:    # only attempt to delete if the element is present
            parent = self._find_parent_node(item)

            # Case 1: node to be removed has no children
            if not found.left and not found.right:
                if self.root is found:
                    self.root = None
                else:
                    if parent.right is found:
                        parent.right = None
                    elif parent.left is found:
                        parent.left = None
            # Case 2: node to be removed has one child
            if found.right and not found.left:       # node to remove has only right child
                if found is self.root:               # node to remove is root
                    self.root = found.right
                else:
                    if parent.right is found:        # node to remove is right child
                        parent.right = found.right
                    if parent.left is found:         # node to remove is left child
                        parent.left = found.right
            if found.left and not found.right:       # node to remove has only left child
                if found is self.root:               # node to remove is root
                    self.root = found.left
                else:
                    if parent.right is found:        # node to remove is right child
                        parent.right = found.left
                    if parent.left is found:         # node to remove is left child
                        parent.left = found.left

            # Case 3: node to be removed has three children
            # First find the successor of the this node.
            # Delete the successor from the tree.
            # Replace the node to be deleted with the successor (or predecessor)
            if found.left and found.right:
                succ = self._find_successor(found)
                print(succ)
                found.data = succ.data
                if succ.data > found.data:
                    self.delete(found.data, found.right)
                else:
                    self.delete(found.data, found.left)

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node=None):
        # start with the root node
        if node is None:
            node = self.root

        # check if this node has the item
        if node.data == item:
            return node

        # recurse left IFF the item is smaller than the current
        # node's data and the current node has a left child
        elif item < node.data and node.left is not None:
            return self._find_node_recursive(item, node.left)
        # recurse right IFF the item is larger than the current
        # node's data and the current node has a right child
        elif item > node.data and node.right is not None:
            return self._find_node_recursive(item, node.right)
        else:
            return None

    def _find_parent_node(self, item):
        return self._find_parent_node_iterative(item)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                #  Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, parent=None):
        if parent is None:
            if self.root.data == item:
                return None
            parent = self.root

        if parent.left is not None:
            if item == parent.left.data:
                return parent
        if parent.right is not None:
            if item == parent.right.data:
                return parent

        if item > parent.data:
            return self._find_parent_node_recursive(item, parent=parent.right)
        elif item < parent.data:
            return self._find_parent_node_recursive(item, parent=parent.left)

    # This space intentionally left blank (please do not delete this comment)

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Traverse left subtree, if it exists
        if node.left:
            self._traverse_in_order_recursive(node.left, visit)
        #  Visit this node's data with given function
        visit(node.data)
        # Traverse right subtree, if it exists
        if node.right:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Visit this node's data with given function
        visit(node.data)
        #  Traverse left subtree, if it exists
        if node.left:
            self._traverse_pre_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        if node.right:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Traverse left subtree, if it exists
        if node.left:
            self._traverse_post_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        if node.right:
            self._traverse_post_order_recursive(node.right, visit)
        # Visit this node's data with given function
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Create queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.is_empty():
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right:
                queue.enqueue(node.right)

def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))


if __name__ == '__main__':
    test_binary_search_tree()
