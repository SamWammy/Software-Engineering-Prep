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


#################################################################

#implementing a deque cuts our time complexity by alot 
# the above varient uses pop(0) which is O(n) but the below varient uses deque.popleft() which is O(1)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left =0 
        final=[]
        q= deque()
        for right in range(len(nums)): 
            q.append(nums[right])

            if (right-left+1) == k : 
                final.append(max(q))
                left +=1 
                q.popleft()
        return final
