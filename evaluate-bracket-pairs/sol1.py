import re
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hashmap = {}
        for k in knowledge:
            hashmap[k[0]] = k[1]

        catches = re.findall(r"\([^(]*\)", s)
        for catch in catches:
            print(catch)
            if catch[1:-1] in hashmap:
                s = s.replace(catch, hashmap[catch[1:-1]])
            else:
                s = s.replace(catch, '?')
        return s
