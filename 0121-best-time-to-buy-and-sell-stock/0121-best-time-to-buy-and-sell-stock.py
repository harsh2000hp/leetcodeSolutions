class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentProfit = 0
        currentLowestValue = float('inf')
        currentMaxProfit = 0
        for currentDayIndex in range(len(prices)):
            if prices[currentDayIndex] < currentLowestValue:
                currentLowestValue = prices[currentDayIndex]
            currentProfit = prices[currentDayIndex] - currentLowestValue
            if currentProfit > currentMaxProfit:
                currentMaxProfit = currentProfit
        return currentMaxProfit
            
        