class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        last_xor = pref[0]
        for i in range(1, len(pref)):
            temp = pref[i]
            pref[i]^=last_xor
            last_xor = temp
        return pref
