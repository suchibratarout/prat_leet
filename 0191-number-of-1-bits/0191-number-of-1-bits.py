class Solution:
    def hammingWeight(self, n: int) -> int:
        out=0
        while n:
            out += n & 1
            n >>= 1
        return out
       
