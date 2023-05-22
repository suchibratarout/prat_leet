class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=min(strs)
        n1=max(strs)
        out=''
        for i in range(min(len(n),len(n1))):
            if n[i]!=n1[i]:
                break
            out+=n[i]
        return out