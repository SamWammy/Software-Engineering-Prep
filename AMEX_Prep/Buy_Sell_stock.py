class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ideally we want to buy when the price is lowest, and sell when the price is highest 

        buyPrice=prices[0]
        profit=0

        for price in prices[1::]: 
            if price< buyPrice: 
                buyPrice = price
            else: 
                profit = max(profit, price - buyPrice)
        return profit