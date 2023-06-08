class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res=""
        for i  in s:
            if i.isalpha():
                res+=i
        res = res[::-1]
        for i, n in enumerate(s):
            if not n.isalpha():
                res = res[:i] + n + res[i:]
        return res
        
