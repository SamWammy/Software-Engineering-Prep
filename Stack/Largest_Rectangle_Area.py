class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        output=0

        for index, height in enumerate(heights): 
            start=index
            while stack and height < stack[-1][1]: 
                stackid,stackHeight= stack.pop()
                area= (index-stackid) * stackHeight
                output=max(output,area)
                start= stackid
            stack.append((start,height))

        for index,height in stack: 
            output=max(output,height*(len(heights)-index))
        return output