class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([1 for i in details if int(i[-4:-2])>60])
