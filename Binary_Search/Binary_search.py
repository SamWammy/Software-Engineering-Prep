## two solutions here that both run (logn)
## first solution is really simple only a couple lines using bisect
## Second solution is the actual binary search algorithm

import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        index= bisect.bisect_left(nums,target)
        if index< len(nums) and nums[index]== target: 
            return index 
        else: return -1

# bisect returns the index of the target, or where it could be inserted in a sorted list 
#####################################################################################################

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l<= r: 
            m= l + ((r -l) //2)

            if nums[m] > target:
                r = m -1
            elif nums[m] < target: 
                l = m +1
            else: 
                return m 
        return -1 