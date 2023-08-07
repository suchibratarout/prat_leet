class Solution:
    def reverseWords(self, s: str) -> str:
        n=s.split()
        
        return " ".join(n[::-1])