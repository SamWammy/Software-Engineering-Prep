class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs: 
            count=[0] *26 #initialize a size 26 list of all 0
            
            for c in s : 
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(s) # add this list(must be a tuple) as key and string as value 
        return list(res.values())



                
