class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=int(math.sqrt(num))
        if n*n==num:
            return True
        else:
            return False
