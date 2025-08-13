class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0] * len(temperatures)
        stack=[] # fill this stack with touples to keep track of indexes and temp

        for index, temp in enumerate(temperatures): 
            while stack and temp> stack[-1][1]: 
                stackindex,stacktemp= stack.pop()
                res[stackindex]= index-stackindex
            stack.append((index,temp))
        return res