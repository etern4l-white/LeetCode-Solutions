class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for domain in cpdomains:
            n = int(domain.split()[0])
            qdomain = domain.split()[1].split('.')[::-1]
            i = 0
            while i < len(qdomain):
                k = '.'.join(qdomain[:i+1][::-1])
                if k not in d:
                    d[k] = n
                else:
                    d[k]+=n
                i+=1
        cplist = []
        for k in d.keys():
            cplist.append(f"{d[k]} {k}")
        return cplist
