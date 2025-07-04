class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tracker ={}

        for i in range(len(numbers)):
            tracker[numbers[i]] = i+1

        #value to index, this is one indexed 

        for index, value in enumerate(numbers):
            difference= target- value
            if difference in tracker and tracker[difference] != index:
                return [tracker[value],tracker[difference]]


# this is a very similar problem to two sum, except it is one indexed to throw people off
# however you can just make the hashmap used one index and return the values from there
# first make a hashmap with values mapped to index (index +1 in thsi case because one index)
# then loop through the indexes and values of the numbers list 
# if the target-value exists in the hashmap and the index is not the same, then we return the indexes from the hashmap 
#simple 



        ########################################### MORE OPTIMAL APPROACH BELOW O(1) Space
        #two pointer approach 

        class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since this is sorted we can take a two pointer approach 
        # this makes this O(1) space which is optimal 

        left= 0 
        right= len(numbers) - 1 

        while left < right : 
            amount= numbers[left] + numbers[right]

            if amount < target: 
                left +=1
            elif amount > target:
                right -=1
            else: 
                return [left+1, right +1]