class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        out=[]
        v=set(nums)
        for i in range(1,len(nums)+1):
            if i not in v:
                out.append(i)
        return out