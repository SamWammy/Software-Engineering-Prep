class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]

        def parent(openN,closeN): 
            if openN == closeN == n: 
                res.append(''.join(stack))
                return 
            if openN < n:
                stack.append('(')
                parent(openN+1,closeN)
                stack.pop()
            if closeN< openN: 
                stack.append(')')
                parent(openN,closeN+1)
                stack.pop()
        parent(0,0)
        return res 
