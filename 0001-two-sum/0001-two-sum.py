class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for currentIndex in range(len(nums)):
            if target-nums[currentIndex] in hashMap:
                return [hashMap[target-nums[currentIndex]],currentIndex ]
            else:
                hashMap[nums[currentIndex]] = currentIndex
            