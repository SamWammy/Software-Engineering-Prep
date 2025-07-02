class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker ={}
        freq=[[] for i in range(len(nums)+1)]

        for val in nums :
            tracker[val]=tracker.get(val,0) +1
        
        # now fill freq list, index is count val is list of values with that count 

        for num,count in tracker.items():
            freq[count].append(num) #append because list of list 

        # loop through buckets backwards and return top k, remember this is a list of lists 
        res=[]
        for i in range(len(freq)-1,0,-1):
            for val in freq[i]:
                res.append(val)
                if len(res) ==k :
                    return res 