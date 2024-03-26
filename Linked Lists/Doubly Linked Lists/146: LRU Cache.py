# https://leetcode.com/problems/lru-cache/description/
# difficulty: medium
# topics: hash table, linked list, design, doubly-linked list

# problem:
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
#     LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#     int get(int key) Return the value of the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.size = 0
        self.capacity = capacity

    def insertLeft(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
    
    def insertRight(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def deleteNode(self, curr):
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
    
    def deleteRight(self):
        removed = self.tail.prev
        del self.map[removed.key]
        self.deleteNode(removed)

    def get(self, key: int) -> int:
        if key not in self.map: return -1
        curr = self.map[key]
        self.deleteNode(curr)
        self.insertLeft(curr)
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            curr = self.map[key]
            curr.val = value
            self.deleteNode(curr)
            self.insertLeft(curr)
            return
        newNode = ListNode(key, value)
        self.map[key] = newNode
        self.insertLeft(newNode)
        if self.size == self.capacity: self.deleteRight()
        else: self.size += 1

# takeaways:
#     1) high level for how to implement a DLL
#     2) that if we want O(1) removal from an arbitrary position, we can use a linked list
#     3) you can use a hashmap to store references to the nodes
#     4) you can have flexibility in what you store on the nodes, including the key itself 
