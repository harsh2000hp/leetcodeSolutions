class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return [i,hashMap[nums[i]]]
            else:
                required = target - nums[i]
                hashMap[required] = i
                