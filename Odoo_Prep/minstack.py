#5241
#5221
class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        # min stack will only push elements less than itself, if it is not less than it will just push itself.

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minstack or self.minstack[-1] > val: 
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minstack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()