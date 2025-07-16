class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        lowest=prices[0]
        for price in prices[1:]: 
            if  price < lowest: 
                lowest = price 
            else: 
                res= max(res,price-lowest)
        return res