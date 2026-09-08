# Last updated: 9/8/2026, 10:20:14 AM
class Solution:
    def findReplaceString(self, s, indexes, sources, targets):
        for i,src,tar in sorted(zip(indexes,sources,targets), reverse=True):
            if s[i:i+len(src)]==src:
                s=s[:i]+tar+s[i+len(src):]
        return s