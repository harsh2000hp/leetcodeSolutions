class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for currentCharacterIndex in range(len(strs[0])):
            for value in strs:
                if currentCharacterIndex == len(value) or value[currentCharacterIndex] != strs[0][currentCharacterIndex]:
                    return res
            res += strs[0][currentCharacterIndex]
        return res