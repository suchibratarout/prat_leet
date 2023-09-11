class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        out = {}
        out1 = {}
    
        for i in range(len(s)):
            if s[i] in out:
                if out[s[i]] != t[i]:
                    return False
            else:
                if t[i] in out1:
                    return False
                out[s[i]] = t[i]
                out1[t[i]] = s[i]
    
        return True
        