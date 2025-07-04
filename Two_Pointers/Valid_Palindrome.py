class Solution:
    def isPalindrome(self, s: str) -> bool:

        string=""
        for c in s : 
            if c.isalnum():
                string +=c.lower() # make this into lower case 
        return string == string[::-1]

        #Approach, create a new string with only the alpha numeric chars
        # (only a-z 1-9) add each character to this string as lower case since we dont care about case sesnitivity 
        # compare the string with all lower case and only alpha numeric chars 
        # to its reverse form 
        #returns true if palindrome, false if not 

        # THERE EXISTS A MORE OPTIMAL SOLUTION, this one is just linear space optimal is constant


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

