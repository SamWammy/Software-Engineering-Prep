class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=[]

        for i in range(len(nums)): 
            a = nums[i]

            if i>0 and a == nums[i-1]: 
                continue 
            
            l=i+1 
            r = len(nums) -1 

            while l< r: 
                amount = a + nums[l] + nums[r]
                if amount >0:
                    r-=1 
                elif amount <0: 
                    l+=1
                else: 
                    output.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r: 
                        l+=1
        return output

