class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        out = nums1.copy() 
        out.extend(nums2)
        out.sort()

        if len(out)%2!=0:
            return float((out[len(out)//2]))
        else:
            a = out[len(out)//2-1]
            b = out[len(out)//2]
            return float((a+b)/2)