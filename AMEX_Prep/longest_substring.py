class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest =0 

        subString = set()

        l=0

        for r in range(len(s)): 
            # check if it exists in the substring first, if not than add. 
            while s[r] in subString: 
                subString.remove(s[l])
                l+=1            
            subString.add(s[r])
            longest= max(longest,len(subString))

        return longest