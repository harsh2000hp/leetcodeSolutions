class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]].append(i)
            else:
                hashMap[nums[i]] = [i]
        for i in hashMap:
            if len(hashMap[i]) > 1:
                valArray = hashMap[i]
                for currentVal in range(len(valArray)-1):
                    if valArray[currentVal+1]-valArray[currentVal] <=k:
                        return True
                
                    
            else:
                continue
        return False