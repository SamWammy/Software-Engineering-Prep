class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        left =0 
        right = len(height) - 1
        maxl=height[left]
        maxr=height[right]

        while left < right:
            if maxl<maxr: 
                left+=1
                maxl= max(maxl,height[left])
                res+= maxl - height[left]
            else:
                right-=1
                maxr= max(maxr,height[right])
                res+= maxr-height[right]
        return res 