class Solution:

    def make_zeros(self, matrix, i, j, n, m, vr, vc):
        if i not in vr:
            vr[i] = 1
            for x in range(0, m):
                matrix[i][x] = 0
        if j not in vc:
            vc[j] = 1
            for x in range(0, n):
                matrix[x][j] = 0
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zz = []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zz.append([i,j])
        vr = {}
        vc = {}
        for coord in zz:
            self.make_zeros(matrix, coord[0], coord[1], n, m, vr, vc)


        # vr = {}
        # vc = {}
        # n, m = len(matrix), len(matrix[0])
        # for i in range(n):
        #     if i in vr:
        #         continue
        #     for j in range(m):
        #         if j in vc:
        #             continue
        #         if matrix[i][j] == 0:
        #             vr[i] = 1
        #             vc[j] = 1
        #             for x in range(0, m):
        #                 matrix[i][x] = 0
        #             for x in range(0, n):
        #                 matrix[x][j] = 0
        #             break

                    
        
