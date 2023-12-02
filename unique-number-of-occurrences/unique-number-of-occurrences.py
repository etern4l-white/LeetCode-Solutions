class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurs = [arr.count(i) for i in set(arr)]
        return len(occurs) == len(list(set(occurs)))
