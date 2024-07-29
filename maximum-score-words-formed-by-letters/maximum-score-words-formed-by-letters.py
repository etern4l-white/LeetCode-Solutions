class Solution:
    def get_combs(self, items):
        N = len(items)
        combs = []
        for i in range(2**N):

            comb=[]
            for j in range(N):
                if (i >> j) % 2 == 1:
                    comb.append(items[j])
            combs.append(comb)
        return combs

    def calculate_score(self, comb, ld, score_dict):
        score = score_dict.copy()
        ld = ld.copy()
        s = ''.join(comb)
        res = 0
        for i in s:
            if i not in ld or ld[i] == 0:
                return -1
            else:
                res+=score[i]
                ld[i]-=1
        return res

    def maxScoreWords(self, words, letters, score) -> int:
        letters_dict = {}
        for i in letters:
            if i in letters_dict:
                letters_dict[i]+=1
            else:
                letters_dict[i] = 1
        score_d = {}
        for i in range(26):
            score_d[chr(i + 97)] = score[i]
        combs = self.get_combs(words)
        scores = []
        for comb in combs:
            scores.append(self.calculate_score(comb, letters_dict, score_d))
            # print(comb, scores[-1])
        return max(scores)
