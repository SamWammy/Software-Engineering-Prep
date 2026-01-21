class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) time o(n) space 

        if len(s) != len(t): 
            return False

        Sdict={}
        Tdict={}

        for i in range(len(s)): 
            Sdict[s[i]]= Sdict.get(s[i],0) + 1
            Tdict[t[i]] = Tdict.get(t[i],0) + 1
        
        return Sdict == Tdict