# Last updated: 9/8/2026, 10:20:17 AM
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if s=='':
            return ''
        ans =[]
        c=0
        i=j=0
        while i<len(s):
            c+=1 if s[i]=='1' else -1
            if c==0:
                ans.append('1'+self.makeLargestSpecial(s[j+1:i])+'0')
                j=i+1
            i+=1
        ans.sort(reverse=True)
        return ''.join(ans)
