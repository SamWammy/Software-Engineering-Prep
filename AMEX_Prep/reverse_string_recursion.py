class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(l,r): 
            if l< r: 
                reverse(l+1, r-1)
                s[l], s[r]= s[r], s[l]
        
        reverse(0,len(s) - 1)

        # o(n) time loop through all of s array 
        #o(n) space because of the call stack for recursion.