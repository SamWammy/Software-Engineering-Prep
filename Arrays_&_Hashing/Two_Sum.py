class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker ={}

        for index, value in enumerate(nums):
            tracker[value]= index
        
        # use the difference target - value to find missing val 

        for index, value in enumerate(nums):
            difference= target- value
            if difference in tracker and tracker[difference] != index:
                return [index,tracker[difference]]

                #o(n) run time and o(n) space