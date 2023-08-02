class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        out=1
        out1=0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                out += 1
            else:
                out1 += (out-1) // 2
                out = 0
    
        out1 += out // 2
        return out1 >= n
        