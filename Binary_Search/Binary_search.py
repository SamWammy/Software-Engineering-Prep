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
