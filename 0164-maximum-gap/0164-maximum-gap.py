class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        out=[0]
        for i in  range(1,len(nums)):
            out.append(nums[i]-nums[i-1])
        return max(out)