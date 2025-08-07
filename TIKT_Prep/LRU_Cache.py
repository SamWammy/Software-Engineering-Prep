class Node(): 
    def __init__(self,key,value): 
        self.key=key
        self.value=value
        self.prev=self.next= None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap= capacity 
        self.cache={}
        #cache = key:node pointer
        self.left,self.right= Node(0,0), Node(0,0)
        self.left.next, self.right.prev= self.right, self.left



    def insert(self, node):
        prevMRU= self.right.prev
        prevMRU.next= node
        node.prev = prevMRU
        node.next=self.right 
        self.right.prev=node

    def remove(self,node): 
        temp = node.prev
        temp.next= node.next
        node.next.prev = temp


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # when we get a node or anything from the cache this updates the most recently used key, to move up to the front 
        if key in self.cache: 
            #update node position to MRU create insert and remove helpers
            # remove from linked list, insert to top 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else: 
            return -1



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        #put: update value, if this makes the cache too big than we evict from list and hashmap
        # putting also moves node up to MRU 

        if key in self.cache: 
            # this means it exists in the linked list so remove it and reinsert
            self.remove(self.cache[key])
        # otherwise just readd the key value pair in the dict and re insert into the list 
        self.cache[key]= Node(key,value)
        self.insert(self.cache[key])

        #now check for capacity 

        if len(self.cache) > self.cap: 
            lru = self.left.next # LRU all the way to the left, remove from list and then remove from dict 
            self.remove(lru)
            self.cache.pop(lru.key) # pop based off key value 

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)