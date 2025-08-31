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

#############################################################
#optimal O(nlog(n)) time solution using binary search 

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        left,right=1, max(piles)
        rate=right
        
        while left <= right : 
            middle = (left +right)//2
            print(middle)
            hours=0
            for bananas in piles: 
                #compute total number of hours
                hours += math.ceil(bananas/middle)
            if hours > h: 
                    #if it took too long we need to find a faster rate
                left = middle +1
            else: 
                    # if it was fast enough we can try to find a faster result
                rate= middle
                right = middle -1
        return rate
