class Node:
    def __init__(self, key, val, prv=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prv
        self.nxt = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def add_to_beginning(self, node):
        curr = self.left.nxt
        self.left.nxt = node
        node.nxt = curr
        curr.prev = node
        node.prev = self.left

        return node
    
    def remove_node(self, node):

        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            this_node = self.cache[key]
            self.remove_node(this_node)
            self.add_to_beginning(this_node)
            self.cache[key] = this_node
            return this_node.val

        return -1

    def put(self, key: int, value: int) -> None:
        
        if key not in self.cache:
            if len(self.cache) == self.cap:
                #remove lru
                lru = self.right.prev
                self.remove_node(lru)
                del self.cache[lru.key]
            
            new_node = Node(key, value)
            self.add_to_beginning(new_node)

            self.cache[key] = new_node
        else:
            this_node = self.cache[key]
            this_node.val = value
            self.remove_node(this_node)
            self.add_to_beginning(this_node)
            self.cache[key] = this_node
