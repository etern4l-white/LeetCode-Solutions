class Solution:
    def makeGood(self, s: str) -> str:
        l = len(s)
        if l <=1:
            return s
        st = [s[0]]
        i = 1
        while i<l :
            # print(s[i], st[-1])
            if len(st) > 0:
                if abs(ord(st[-1]) - ord(s[i])) == 32:
                    st.pop(-1)
                else:
                    st.append(s[i])
            else:
                st.append(s[i])
            i+=1
        return ''.join(st)
