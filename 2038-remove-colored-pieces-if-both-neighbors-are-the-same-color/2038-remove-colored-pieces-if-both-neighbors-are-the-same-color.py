class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        countA = 0
        countB = 0
        for something in range(1,len(colors)-1):
            if colors[something] == colors[something+1] == colors[something-1]:
                if colors[something] == "A":
                    countA += 1
                elif colors[something] == "B":
                    countB += 1
                
        if countA > countB:
            return True
        else:
            return False