class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # l = max(start, goal)
        # n = 0
        # x = 0
        # while l>0:
        #     l//=2
        #     n+=1
        # while n > 0:
        #     x+=((start%2) ^ (goal%2))
        #     n-=1
        # return x
        res = start^goal
        s = 0
        for i in range(32):
            s+=1 if (res&(1<<i))!=0 else 0
        return s
