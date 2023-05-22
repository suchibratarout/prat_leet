class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        out=0
        for i in columnTitle:
            out=out*26+ord(i)-ord('A')+1
        return out