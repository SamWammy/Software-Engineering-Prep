class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left =0 
        chars =set()
        res=0 
        for right in range(len(s)): 
            while s[right] in chars: 
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            res=max(res,len(chars))
        return res 

        # this is a sliding window question, free points review before interviews

