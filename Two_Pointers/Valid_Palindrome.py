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