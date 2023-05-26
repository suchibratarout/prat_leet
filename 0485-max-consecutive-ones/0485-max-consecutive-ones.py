class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        out=0
        n=0
        for i in nums:
            if i:
                n+=1
            else:
                out=max(n,out)
                n=0
        return out