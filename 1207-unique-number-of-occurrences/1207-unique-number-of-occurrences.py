class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for currentNum in arr:
            if currentNum in hashMap:
                hashMap[currentNum] += 1
            else:
                hashMap[currentNum] = 1
        values = hashMap.values()
        if len(set(values)) == len(hashMap):
            return True
        else:
            return False
        