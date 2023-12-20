class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        minimum = min(prices[0], prices[1])
        secondMinimum = max(prices[0], prices[1])
        
        for i in range(2, len(prices)):
            if prices[i] < minimum:
                secondMinimum = minimum
                minimum = prices[i] 
            elif prices[i] < secondMinimum:
                secondMinimum = prices[i]
        summation = minimum + secondMinimum
        if summation <= money:
            return money - summation
        else:
            return money
        
        