from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        '''
        adds the input value to the binary search tree, adhering to 
        the rules of the ordering of elements in a binary search tree.
        '''
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        '''
        searches the binary search tree for the input value, returning a 
        boolean indicating whether the value exists in the tree or not.
        '''
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        '''
        returns the maximum value in the binary search tree.
        '''
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        '''
        performs a traversal of _every_ node in the tree, executing the 
        passed-in callback function on each tree node value. There is a myriad 
        of ways to perform tree traversal; in this case any of them should work
        '''
        pass

    # DAY 4 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
