class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        jq = []
        for query in queries:
            s = 0
            for point in points:
                if (point[0] - query[0])**2 + (point[1] - query[1])**2 <= query[2]**2:
                    s+=1
            jq.append(s)
        return jq
