class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        out=1
        res=0
        i=0
        if i<len(s) and (s[i]=='-' or s[i]=='+'):
            if s[i]=='-':
                out=-1
            i+=1
        while i<len(s) and s[i].isdigit():
            res=res*10+int(s[i])
            i+=1
        res=max(min(res*out,2**31-1),-2**31)
        return res
