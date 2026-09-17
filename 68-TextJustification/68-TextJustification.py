# Last updated: 9/17/2026, 9:53:34 AM
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res,cur,num_letters=[],[],0
        for i in words:
            if num_letters+len(i)+len(cur)>maxWidth:
                for j in range(maxWidth-num_letters):
                    cur[j%(len(cur)-1 or 1)]+=' '
                res.append(''.join(cur))
                cur,num_letters=[],0
            cur+=[i]
            num_letters+=len(i)
        return res+[' '.join(cur).ljust(maxWidth)]