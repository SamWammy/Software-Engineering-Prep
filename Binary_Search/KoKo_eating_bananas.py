###########################################################################
#Brute Force O(n^2) approach, times out however logic is correct.

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        output =1 
        
        while output <= max(piles): 
            hours=0
            for bananas in piles: 
                hours += math.ceil(bananas/output)
                if hours > h: 
                    break
                if bananas == piles[-1]: 
                    return output
            output +=1

