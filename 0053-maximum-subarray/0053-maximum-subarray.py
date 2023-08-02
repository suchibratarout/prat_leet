class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out=s=nums[0]
        for i in range(1,len(nums)):
            s=max(s+nums[i],nums[i])
            out=max(out,s)
        return out
