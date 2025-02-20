class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        power = len(nums[0])
        d = {int(i, 2) for i in nums}
        for i in range(2**power):
            if i not in d:
                number = bin(i)[2:]
                if len(number) < power:
                    return "0"*(power - len(number)) + number
                else:
                    return number

                
