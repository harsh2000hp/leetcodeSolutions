class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        d = Counter(nums)
        res = []
        for k in d:
            if d[k] >1:
                res.append(k)
        return res
        