class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-3,-3,1,2,3,4]
        res=[]
        nums.sort()

        for i, n in enumerate(nums): 
            if i >0 and n == nums[i-1]:
                continue 
            left=i+1
            right = len(nums)-1
            
            while left< right: 
                amount= n +nums[left] +nums[right]
                if amount >0 :
                    right-=1
                elif amount <0:
                    left+=1
                else: 
                    res.append([n,nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left< right: 
                        left +=1
        return res

        
        # this solution takes a list sorts it, finds the first a (three sum asks for a+b+c=0) and does two sum on the rest of the list to find b and c 
        #sorting the list allows us to avoid duplicates since a duplicate will likely be in the index position less of itself 
                #[-3,-3,1,2,3,4]
