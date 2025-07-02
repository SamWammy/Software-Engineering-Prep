class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0 

        for val in numset: 
            if (val-1) not in numset:
                length=1
                number=val
                while (number+1) in numset: 
                    length+=1
                    number+=1
                longest=max(length,longest)
        return longest


        