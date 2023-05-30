class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        out=''
        v=True
        for i in range(0,len(s),k):
            if v:
                out+=(s[i:i+k])[::-1]
                v=False
            else:
                out+=s[i:i+k]
                v=True
        return out