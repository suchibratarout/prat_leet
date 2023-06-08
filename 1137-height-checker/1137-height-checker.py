class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        out=sorted(heights)
        c=0
        for i in range(0,len(heights)):
            if heights[i]!=out[i]:
                c+=1
        return c