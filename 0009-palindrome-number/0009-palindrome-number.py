class Solution:
    def isPalindrome(self, x: int) -> bool:
        out=str(x)
        n=out[::-1]
        if out==n:
            return True
        else:
            False