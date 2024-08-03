class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        s = [chars[0]]
        i = 1
        cur_letter = chars[0]
        cur_sum = 1
        l = len(chars)
        while i < l:
            if chars[i] != cur_letter:
                if cur_sum > 1:
                    s.extend([i for i in str(cur_sum)])
                s.append(chars[i])
                cur_letter = chars[i]
                cur_sum = 1
            else:
                cur_sum+=1
            i+=1
        if cur_sum > 1: s.extend([i for i in str(cur_sum)])
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)
