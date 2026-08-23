class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        suffix=[]
        prefix.append(1)
        suffix.append(1)
        for i in range(len(nums)-1):
            prefix.append(prefix[-1]*nums[i])
        for i in range(len(nums)-1,0,-1):
            suffix.append(suffix[-1]*nums[i])
        suffix=suffix[::-1]
        res=[]
        for i in range(len(prefix)):
            res.append(prefix[i]*suffix[i])
        return res
        
        