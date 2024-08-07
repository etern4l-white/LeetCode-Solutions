class Solution:
    def do_3_digits(self, num, dn):
        # 123
        s = []
        while num > 0:
            if num>=100:
                t = num//100
                s.extend([dn[t], "Hundred"])
                num-=(t*100)
            elif num >= 10 and num//10 > 1:
                t = num//10
                s.append(dn[t*10])
                num-=(t*10)
            elif num >= 10:
                t = num%100
                s.append(dn[t])
                num-=t
            else:
                t = num%10
                s.append(dn[t])
                num-=t
        return s
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        dn = {
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:'Eleven',
            12:'Twelve',
            13:'Thirteen',
            14:'Fourteen',
            15:'Fifteen',
            16:'Sixteen',
            17:'Seventeen',
            18:'Eighteen',
            19:'Nineteen',
            20:"Twenty",
            30:"Thirty",
            40:"Forty",
            50:"Fifty",
            60:"Sixty",
            70:"Seventy",
            80:"Eighty",
            90:"Ninety",
            100:"Hundred",
            1000:"Thousand",
            1000000:"Million",
            1000000000:"Billion"
        }
        s = []
        while num>0:
            if num>=10**9:
                t = num//(10**9)
                s.extend([dn[t], "Billion"])
                num-=(t*(10**9))
            elif num >=10**6:
                t = num//(10**6)
                s.extend(self.do_3_digits(t, dn))
                s.append("Million")
                num-=t*10**6
            elif num>=1000:
                t = num//(10**3)
                s.extend(self.do_3_digits(t, dn))
                s.append("Thousand")
                num-=t*1000
            else:
                s.extend(self.do_3_digits(num, dn))
                num-=num%1000
        return ' '.join(s)
            
