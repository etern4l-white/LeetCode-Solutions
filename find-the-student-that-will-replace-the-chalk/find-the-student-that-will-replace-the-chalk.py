class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        l = len(chalk)
        s = sum(chalk)
        if k>s:
            k-=((k//s)*s)
        while k>0:
            k-=chalk[i%l]
            if k >= 0:
                i+=1
        return i%l





# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
#         i = 0
#         ll = len(chalk)
#         s = sum(chalk)
#         if s >= k:
#             k-=(s//k)
#             pf = [chalk[0]]
#             i = 1
#             while i < ll:
#                 pf.append(chalk[i] + chalk[i-ll])
#                 i+=1
#             i = 0

#             l,r = 0, ll
#             while l < r:
#                 if pf[l] < k:
#                     return l
#                 elif pf[(l+r)//2] < k:
#                     l = l+r
#                 elif
#             while k>0:
#                 k-=chalk[i%ll]
#                 if k >= 0:
#                     i+=1
#             return i%ll
#         else:
#             while k>0:
#                 k-=chalk[i%ll]
#                 if k >= 0:
#                     i+=1
#             return i%ll
