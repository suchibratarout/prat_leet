class Solution:
    def reverseWords(self, s: str) -> str:
        out=[]
        for i in s.split():
            out.append(i[::-1])
        return " ".join(out)