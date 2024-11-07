def get_bit(number, i):
    return (number>>i)&1

def and_arr(arr):
    s = 2**32 - 1
    for i in arr:
        s&=i
    return s>0

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # l = len(candidates)
        # lengths = []
        # for i in range(1, 2**l):
        #     q = []
        #     for n in range(l):
        #         if get_bit(i, n):
        #             q.append(candidates[n])
        #     if len(q) > 1:
        #         if and_arr(q):
        #             lengths.append(len(q))
        # return max(lengths)
        max_count = 0
        for bit in range(32):
            count = 0
            for num in candidates:
                if (num& (1<<bit) != 0):
                    count+=1
            max_count=max(max_count, count)
        return max_count
