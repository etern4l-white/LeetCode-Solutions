class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        # number_of_fit = 0
        # i = 0
        # ll = len(fb)
        # c = 0
        # counting = False
        # while i < ll and number_of_fit < n:
            
        #     if fb[i] == 1:
        #         c = 0
        #         counting = False
        #     else:
        #         c+=1
        #         if c > 1:
        #             if fb[0] == 1 and c %2 == 0:
                        
        #                 number_of_fit+=1
        #             elif fb[0] == 0 and c%2 == 1:
        #                 number_of_fit+=1
                        
        #     if number_of_fit >=n:return True
        #     i+=1
        nn = 0
        if len(fb) > 1:
            if fb[0] == 0 and fb[1] == 0:
                fb[0] = 1
                nn+=1
            # else:
            i = 1
            while i < len(fb)-1:
                if nn>=n: return True
                if fb[i] ==0 and fb[i-1] == 0 and fb[i+1] == 0:
                    fb[i] = 1
                    nn+=1

                if i == len(fb) -2:
                    if fb[i] ==0 and fb[i+1] == 0:
                        fb[i+1] = 1
                        nn+=1
                i+=1
        else:
                return (fb[0] == 0 and n == 1 ) or (fb[0] == 1 and n == 0) or (fb[0] == 0 and n == 0)
        return nn>=n
