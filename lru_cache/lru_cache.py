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
        self.limit = limit
        # self.val = val
        # self.key = key
        self.list = DoublyLinkedList()
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        pass
        # access key:value pair
        # move accessed pair to top of cache
        # move other pairs down one spot
        # return the value associated with the key
        # OR return None if key:value doesn't exist
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
        self.cache[key] = value
        # if cache limit is reached:
        if len(self.cache) == self.limit:
            # delete item from end of cache (oldest) if so
            self.list.remove_from_head(key)
            # add new key:value pair to top of list
            self.list.add_to_tail(key)
        else:
            self.list.add_to_tail(key)
        # move remaining pairs down one spot
