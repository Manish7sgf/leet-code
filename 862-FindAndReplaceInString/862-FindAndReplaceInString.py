# Last updated: 8/31/2026, 1:58:04 PM
class Solution:
    def findReplaceString(self, s, indexes, sources, targets):
        for i,src,tar in sorted(zip(indexes,sources,targets), reverse=True):
            if s[i:i+len(src)]==src:
                s=s[:i]+tar+s[i+len(src):]
        return s