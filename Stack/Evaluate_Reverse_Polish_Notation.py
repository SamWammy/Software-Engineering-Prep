class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
         
        for char in tokens: 
            print(char)
            print(stack)
            if char == '+': 
                stack.append(stack.pop() + stack.pop())
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char =='-': 
                a = stack.pop()
                b= stack.pop()
                # since this is a stack, the most recent number would be most right 
                # but we do arethmatic from left to right 
                # so we pop both off first, and append the value of b - a 
                #if we did stack.append(stack.pop()-stack.pop()) that would be like saying 4-3 
                # but the example is 3-4, so we want to pop them both off seperatly to perserve this 
                stack.append(b-a)
            elif char== '/': 
                a= stack.pop()
                b=stack.pop()
                stack.append(int(b/a))

            else: 
                stack.append(int(char))
        return stack[-1]