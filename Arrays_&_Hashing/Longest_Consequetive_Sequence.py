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

#################################################################################
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        # this gives us O(1) lookup and duplicates shouldnt be counted 

        #we want to find the start of the sequence, and count up from there 
        longest=0

        for value in nums: 
            # this checks if we are in the start of the sequence 
            if value -1 not in numset: 
                length =1
                # count the value, start of sequence, count for every value + 1 after
                while value + 1 in numset: 
                    length +=1 
                    value+=1
                longest= max(longest,length)
        return longest

