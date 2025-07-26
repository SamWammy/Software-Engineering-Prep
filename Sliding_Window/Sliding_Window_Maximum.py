class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left =0 
        final=[]
        res=[]
        for right in range(len(nums)): 
            res.append(nums[right])

            if (right-left+1) == k : 
                final.append(max(res))
                left +=1 
                res.pop(0)
        return final


