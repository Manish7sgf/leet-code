# Last updated: 7/14/2026, 2:18:35 PM
class Solution:
    def intToRoman(self, num: int) -> str:
        vs=[
            (1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')
        ]
        r=[]
        for value,symbol in vs:
            if(num==0):
                break
            count=num//value
            r.append(symbol*count)
            num=num-count*value
        return ''.join(r)
