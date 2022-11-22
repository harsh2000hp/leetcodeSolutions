class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        currentStack = []
        for character in s:
            if currentStack and currentStack[-1][0] == character:
                currentStack[-1][1] += 1
            else:
                currentStack.append([character,1])
            if currentStack[-1][1] == k:
                currentStack.pop()
            
        res = ""
        for char, count in currentStack:
            res += char*count
        return res
        