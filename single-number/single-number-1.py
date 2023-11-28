class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
            if d[i] == 2:
                del d[i]
        return list(d.items())[0][0]
        
