class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker ={}
        res =0 
        left =0 
        
        for r in range(len(s)): 
            tracker[s[r]]= tracker.get(s[r],0)+1

            while (r-left+1) - max(tracker.values())> k: 
                tracker[s[left]]-=1
                left+=1
            res= max(res,r-left+1)
        return res

