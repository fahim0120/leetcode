"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/lru-cache/
# Medium
# Amazon
# Most Liked
# Top Interviews


'''
Using Doubly Linked List and Dictionary.
'''
class LRUCache:
    class Node:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None


    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.remove_from_linked_list(key)
            self.insert_into_first(node)
            return node.value

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.remove_from_linked_list(key)
            node.value = value
        else:
            node = self.Node(key, value)
            self.cache[key] = node

        self.insert_into_first(node)

        if len(self.cache) > self.capacity:
            self.delete_last_node()


    def insert_into_first(self, node: Node):
        self.head.next, node.next = node, self.head.next
        node.next.prev = node
        node.prev = self.head


    def remove_from_linked_list(self, key: int):
        node = self.cache[key]
        node.prev.next, node.next.prev = node.next, node.prev

        return node


    def delete_last_node(self):
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        key = node.key
        del self.cache[key]
        del node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''
Using OrderedDict only.
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            oldest = next(iter(self.cache))
            del self.cache[oldest]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
