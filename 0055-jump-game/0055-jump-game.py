class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndexReached = 0
        for i in range(len(nums)):
            if i> maxIndexReached:
                return False
            if nums[i]+i > maxIndexReached:
                maxIndexReached = nums[i] + i
            if maxIndexReached == len(nums)-1:
                return True
        return True
            
            
        