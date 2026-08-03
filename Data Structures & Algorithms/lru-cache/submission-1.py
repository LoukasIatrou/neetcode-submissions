class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left,self.right = Node(0,0),Node(0,0)
        #Left is LRU and right is MRU, we need them to point to eachother so we can insert nodes in their middle at the beginning
        self.left.next,self.right.previous = self.right,self.left
    def remove(self,node):
        previous, nxt = node.previous, node.next 
        previous.next  = nxt 
        nxt.previous = previous

    #Insert at right
    def insert(self,node):
        previous,nxt = self.right.previous, self.right
        previous.next = nxt.previous = node
        node.next,node.previous = nxt,previous



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) 
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key]) 
        if len(self.cache) >self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]




        
class Node:
    def __init__(self,key,val):
        self.key, self.val  = key, val
        self.previous = self.next = None
