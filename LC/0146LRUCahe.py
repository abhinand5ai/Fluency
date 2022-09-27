
class Node:
    def __init__(self, key=None, val=None, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt


def remove(node: Node):
    prev = node.prev
    nxt = node.next
    prev.next = nxt
    nxt.prev = prev
    node.next = None
    node.prev = None


def insertAfter(head: Node, node: Node):
    nxt = head.next
    node.prev = head
    head.next = node
    node.next = nxt
    nxt.prev = node


def insertBefore(tail: Node, node: None):
    prev = tail.prev
    node.next = tail
    tail.prev = node
    node.prev = prev
    prev.next = node


class LRUCache:

    def __init__(self, capacity):
        # Write your code here
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        self.capacity = capacity
        self.curr_capacity = 0
        return

    def get(self, x):
        # Write your code here
        if x not in self.cache:
            return -1
        node = self.cache[x]
        self.prioritize(node)
        return node.val

    def prioritize(self, node):
        remove(node)
        insertAfter(self.head, node)

    def invalidate(self, node):
        del self.cache[self.tail.prev.key]
        remove(node)

    def put(self, x, y):
        # Write your code here
        if x in self.cache:
            node = self.cache[x]
            node.val = y
            self.prioritize(node)
        else:
            node = Node(x, y)
            self.cache[x] = node
            if self.curr_capacity == self.capacity:
                self.invalidate(self.tail.prev)
                self.curr_capacity -= 1
            insertAfter(self.head, node)
            self.curr_capacity += 1

        
