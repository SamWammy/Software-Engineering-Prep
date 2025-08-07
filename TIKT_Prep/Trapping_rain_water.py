class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left= 0
        right = len(height) -1
        res=0
        leftmost=height[left]
        rightmost=height[right]
        while left< right: 
            if leftmost < rightmost: 
                left+=1
                leftmost= max(height[left],leftmost)
                res+= leftmost -height[left]
            else: 
                right-=1
                rightmost=max(height[right],rightmost)
                res+= rightmost -height[right]
        return res


                