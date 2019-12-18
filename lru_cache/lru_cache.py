from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.order = DoublyLinkedList()  # need DLL to store the order
        self.storage = dict()  # need Dict to store the key:value pairs
        self.size = 0  # need current size; size is the number of nodes
        self.limit = limit  # need limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # pull value out of dict using the key
        if key in self.storage: # specifying the key in the key, NOT key in dict
            # specify that our node is what's in the key
            node = self.storage[key]
            # update position in list (move node to MRU)
            self.order.move_to_front(node)
            # return the "value" from the node's value tuple(key:value)-key at index 0:value at index 1
            return node.value[1]
        # or return None
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if already exists, overwrite value:
        if key in self.storage:
            # update dict
            node = self.storage[key]  # cache is where key:value pair is stored
            # node.value ties value in DLL to the (key, value) tuple we're storing in the dictionary
            node.value = (key, value)
            # Mark new pair MRU: put at head of DLL
            self.order.move_to_front(node)
            return
        # if at max capacity: dump LRU: remove from tail of DLL
        if self.size == self.limit:
            del self.storage[self.order.tail.value[0]]  # remove LRU from dict.
            self.order.remove_from_tail()  # remove LRU from DLL
            self.size -= 1  # size of cache decreases by 1 node
        # Add new pair to the cache:
        self.order.add_to_head((key, value))  # add to nodes/DLL
        self.storage[key] = self.order.head  # add to dict
        self.size += 1  # size of cache increases by 1 node

    # ALTERNATIVE ROUTE:
    # def __init__(self, limit=10):
        # self.list = DoublyLinkedList()  # need DLL to store the order
        # self.cache = {} # need Dict to store the key:value pairs
        # self.num_nodes = 0  # need current size; size is the number of nodes;
        # self.limit = limit # need limit

    # def get(self, key):
    #     # if key is not in the storage dictionary(cache):
    #     if key not in self.cache:
    #         # return None
    #         return None
    #     move_node = self.cache[key]
    #     # move node with key specified to the head
    #     self.list.move_to_front(move_node)

    #     # return the storage dictionary[key]
    #     return move_node.value[1]

    # def set(self, key, value):
        # self.cache[key] = value
        # # if cache limit is reached:
        # if len(self.cache) == self.limit:
        #     # delete item from end of cache (oldest) if so
        #     self.list.remove_from_head(key)
        #     # add new key:value pair to top of list
        #     self.list.add_to_tail(key)
        # else:
        #     self.list.add_to_tail(key)
        # # move remaining pairs down one spot
