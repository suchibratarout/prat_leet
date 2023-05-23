class Solution:
    def toHex(self, num: int) -> str:
        if num>=0:
            n=str(hex(num))
            return n[2:]
        else:
            n=hex(num+2**32)
            return n[2:]