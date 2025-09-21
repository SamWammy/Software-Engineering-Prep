
class Solution:
            #[-3,-3,1,2,3,4]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i, val in enumerate(nums): 
            if i > 0 and val == nums[i-1]: 
                continue 
            left =i+1
            right =len(nums)-1 

            while left< right: 
                total = val +nums[left]+nums[right]

                if total >0: 
                    right -=1
                elif total < 0: 
                    left +=1
                else:
                    res.append([val,nums[left],nums[right]])
                    left+=1
                    while nums[left]== nums[left-1] and left < right: 
                        left +=1
        return res 


        
        # this solution takes a list sorts it, finds the first a (three sum asks for a+b+c=0) and does two sum on the rest of the list to find b and c 
        #sorting the list allows us to avoid duplicates since a duplicate will likely be in the index position less of itself 
                #[-3,-3,1,2,3,4]
