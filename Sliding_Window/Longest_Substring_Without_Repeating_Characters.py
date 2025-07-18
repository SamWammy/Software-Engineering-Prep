class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars= set()
        left =0 
        res=0 

        for r in range(len(s)): 
            while s[r] in chars: 
                chars.remove(s[left]) # remove
                left+=1
            chars.add(s[r])
            res=max(res,r-left+1)
        return res

        