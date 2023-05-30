class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # out=0
        # for i in range(1,num):
        #     if num%i==0:
        #         out+=i
        # if out==num:
        #     return True
        # else:
        #     return False
        return num in [6,28,496,8128,33550336]