
class Node():
    def __init__(self,key,value):
        self.key= key 
        self.value=value
        self.next=None
        self.prev = None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.cache={}
        self.left= Node(0,0)
        self.right = Node(0,0)
        self.left.next= self.right
        self.right.prev=self.left
        
    def insert(self,node): 
        temp= self.right.prev
        temp.next= node
        self.right.prev=node

        node.next=self.right
        node.prev=temp
    
    def remove(self,node): 
        temp=node.prev
        temp.next= node.next
        node.next.prev= temp

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else: 
            return -1

        # once a get is processed, remove key from Linked list using pointers
        # and insert it at most right 

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache: 
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            self.remove(self.left.next)
            self.cache.pop(self.left.next.key)
