class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #length from  the first element(r-l) * height of min element 
        area =0 
        left =0 
        right= len(heights)-1 

        while left< right : 
            res = min(heights[left], heights[right]) * (right -left)
            area= max(res,area)

            if heights[left] <= heights[right]:
                left+=1
            else: 
                right -=1
        return area 