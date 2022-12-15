import collections
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        a = collections.Counter(nums)
        a = sorted(a.items(), key=lambda a: a[1], reverse = True)
        i = 0
        result = []
        while i<len(a) and a[i][1] == 2:
            result.append(a[i][0])
            i += 1
        return result