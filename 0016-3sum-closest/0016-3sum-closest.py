class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=sum(nums[:3])
        print(nums)
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while(l<r):
                tarsm=nums[i]+nums[l]+nums[r]
                if(abs(tarsm-target)<abs(res-target)):
                    res=tarsm
                if(tarsm<target):
                    l+=1
                else:
                    r-=1
        return res