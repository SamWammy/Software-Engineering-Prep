# PRACTICE PROBLEM URL: https://leetcode.com/problems/license-key-formatting/description/


class Solution(object):
 def licenseKeyFormatting(self, s, k):
        """
        Optimized version using list for O(1) appends
        """
        temp = s.replace('-','')

        charList=[]
        acc=0

        for i in range(len(temp)-1,-1,-1): 
            if acc==k: 
                charList.append('-')
                acc=0
            charList.append(temp[i])
            acc+=1
        
        return upper(''.join(charList[::-1]))
            