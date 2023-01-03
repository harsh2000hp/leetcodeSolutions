class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        value1 = edges[0][0]
        value2 = edges[0][1]
        value3 = edges[1][0]
        value4 = edges[1][1]
        if value1 == value2 or value1 == value3 or value1 == value4:
            return value1
        if value2 == value3 or value2 == value4:
            return value2
        if value3 == value4:
            return value3