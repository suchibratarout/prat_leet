class Solution:
    def findComplement(self, num: int) -> int:
        out=''
        while num>0:
            if num%2==1:
                out+='0'
            else:
                out+='1'
            num=num//2
        return int(out[::-1],2)

