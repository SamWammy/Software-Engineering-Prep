class Solution:
      def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for t in tokens: 
            if t == '+': 
                stack.append(stack.pop()+stack.pop())
            elif t == '-': 
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif t == '*': 
                stack.append(stack.pop()*stack.pop())
            elif t == '/':
                a= stack.pop()
                b=stack.pop()
                stack.append(int(float(b)/a))
            else: 
                stack.append(int(t)) # chars are initially string characters so convert to integer 
        return stack[-1]