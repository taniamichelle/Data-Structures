# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):  # we're just using 'value', no key
        self.value = value  # 'key'='value' since only using 'value'
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        '''
        adds the input value to the binary search tree, adhering to 
        the rules of the ordering of elements in a binary search tree.
        '''

        if self.value <= value:  # if new value >= root's value:
            if self.right == None:  # if there's no root for the right side:
                # new value becomes the right root
                self.right = BinarySearchTree(value)
            else:  # if there is a root for the right side:
                # add new value as a child of right root
                return self.right.insert(value)  # making recursive insert call
        else:
            if self.value > value:  # if new value is < root's value:
                if self.left == None:  # if there's no root for left side:
                    # new value becomes the left root
                    self.left = BinarySearchTree(value)
                else:  # if there is a root for left side:
                    # add new value as child of left root
                    return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        '''
        searches the binary search tree for the input value, returning a 
        boolean indicating whether the value exists in the tree or not.
        stops at first instance of the value.
        '''
        # search tree for input value
        # return boolean of True or False, depending on result
        if self.value == target:
            return True
        else:
            if target < self.value:  # if target < self.value:
                if self.left == None:  # if there are no more left branches:
                    return False    # return False
                elif self.left != None:
                    return self.left.contains(target)  # go left (recursive)
            elif target > self.value:  # if target > self.value:
                if self.right == None:
                    return False
                elif self.right != None:
                    return self.right.contains(target)  # go right (recursive)

    # Return the maximum value found in the tree
    def get_max(self):
        '''
        returns the maximum value in the binary search tree.
        '''
        # look at values in branch right of root
        # if node has no right branch and is at rightmost branch, it's the max value
        # return value
        if self.right != None:
            return self.right.get_max()  # call get_max() recursively
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        '''
        performs a traversal of _every_ node in the tree, executing the 
        passed-in callback function on each tree node value. There is a myriad 
        of ways to perform tree traversal; in this case any of them should work
        '''
        # call cb on the value of each node
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

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
