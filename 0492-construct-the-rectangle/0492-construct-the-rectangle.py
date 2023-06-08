class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        out=int(area**0.5)
        while out>0:
            if area%out==0:
                return [area//out,out]
            out-=1
        