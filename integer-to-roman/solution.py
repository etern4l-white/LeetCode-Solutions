class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {
            "k":
                {
                    1:"m",
                    2:"mm",
                    3:"mmm"
                },
            "h":
                {
                    1:"c",
                    2:"cc",
                    3:"ccc",
                    4:"cd",
                    5:"d",
                    6:"dc",
                    7:"dcc",
                    8:"dccc",
                    9:"cm"
                },
            "t":
                {
                    1:"x",
                    2:"xx",
                    3:"xxx",
                    4:"xl",
                    5:"l",
                    6:"lx",
                    7:"lxx",
                    8:"lxxx",
                    9:"xc"
                },
            "o":
                {
                    1:"i",
                    2:"ii",
                    3:"iii",
                    4:"iv",
                    5:"v",
                    6:"vi",
                    7:"vii",
                    8:"viii",
                    9:"ix"
                },
        }

        hi = {}

        hi['k'] = num//1000
        num%=1000

        hi['h'] = num//100
        num%=100

        hi['t'] = num//10
        num%=10

        hi['o'] = num




        final_string = ""
        for i in 'khto':
            if hi[i] > 0:
                final_string+=hashmap[i][hi[i]]
        return (final_string.upper())
