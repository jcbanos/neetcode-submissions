class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = [0] * len(prices)
        min_price = prices[0]

        for i in range(len(prices)):
            best_buy[i] -= min_price
            if prices[i] < min_price:
                min_price = prices[i]

        max_price = prices[len(prices) - 1]
        for i in range(len(prices) - 1, -1 , -1):
            if prices[i] > max_price:
                max_price = prices[i]
            best_buy[i] += max_price
        
        profit = 0

        for num in best_buy:
            if num > profit:
                profit = num
        
        return profit

                
            
        