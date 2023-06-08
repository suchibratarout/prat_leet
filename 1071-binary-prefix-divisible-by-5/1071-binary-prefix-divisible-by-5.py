class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        out=0
        res=[]
        for i in nums:
            out=(out*2+i)%5
            res.append(out==0)
        return res
