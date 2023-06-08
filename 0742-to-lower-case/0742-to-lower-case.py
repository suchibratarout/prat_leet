class Solution:
    def toLowerCase(self, s: str) -> str:
        # out=''
        # for i in range(len(s)):
        #     if 'A'<=s[i]<='Z':
        #          out=out+chr((ord(s[i])+32))
        #     else:
        #         out=out+s[i]
        # return out
        return s.lower()
