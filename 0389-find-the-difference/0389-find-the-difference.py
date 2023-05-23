class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        out=list(t)
        for i in range(len(s)):
            out.remove(s[i])
        return out[0]

