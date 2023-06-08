class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out=[]
        for i in range(len(nums)):
            out.append(nums[i]**2)
        return sorted(out)