class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_as_strings = sorted(map(str, nums), key=lambda x: x*10, reverse=True)
        return str(int(''.join(nums_as_strings)))
        
       