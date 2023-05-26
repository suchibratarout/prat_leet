class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        out=[]
        n=0
        for i in nums:
            if i==1:
                n+=1
            else:
                out.append(n)
                n=0
        out.append(n)
        return max(out)