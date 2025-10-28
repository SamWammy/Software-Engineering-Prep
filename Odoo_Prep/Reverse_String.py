class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        return s.reverse()
        #this is one way to do it 

        class Solution(object):
#########################################################################################
# another way to solve this, the top is using a built in function that changes the array in place
# top function works in O(n) time and O(1) space, utilizing a backwards iterator
# the bottom does the same but is slightly more manual and slower since we need to swap each element
#
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l =0 
        r = len(s)-1

        while l < r:
            temp=s[l]
            s[l]= s[r]
            s[r]=temp
            l+=1
            r-=1