class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in range(len(strs)):
            if tuple(sorted(strs[i])) in hashMap:
                hashMap[tuple(sorted(strs[i]))].append(strs[i])
            else:
                hashMap[tuple(sorted(strs[i]))] = [strs[i]]
        return hashMap.values()