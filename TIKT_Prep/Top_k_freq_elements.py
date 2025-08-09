class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker ={}
        freq=[[] for i in range(len(nums)+1)] #+1 to make this 0 indexed each list is at most 0-len(list) freq
        output=[]
        # fill up tracker with frequencies 
        for val in nums: 
            tracker[val]=tracker.get(val,0)+1

        # now we have a dict with val:freq and buckets with each index being a freq, and the list in that index being how many things show up in that freq 
        # now fill buckets 

        for val in tracker: 
            freq[tracker[val]].append(val)
        
        # now buckets 0-6 are now filled, the furthest index freq is the ones that show up the most 
        # so loop through this backwards 

        for i in range(len(freq)-1,-1,-1): 
            for numb in freq[i]: 
                output.append(numb)
                if len(output)==k: 
                    return output

