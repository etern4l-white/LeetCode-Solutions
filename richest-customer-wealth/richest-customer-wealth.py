class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_num = 0
        max_person, max_bank = 0,0
        l, ll = len(accounts), len(accounts[0])
        for i in range(l):
            s = sum(accounts[i])
            if s>max_num:
                max_person = i
                max_num = s
        return sum(accounts[max_person])
