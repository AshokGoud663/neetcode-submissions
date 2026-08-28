class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        mini=float('inf')
        while low<=high:
            mid=(low+high)//2
            mini=min(mini,nums[mid])
            if nums[low]<nums[mid] and nums[mid]>nums[high]:
                low=mid+1
            elif nums[low]>nums[mid] and nums[mid]<nums[high]:
                high=mid-1
            elif nums[low]<nums[mid] and nums[mid]<nums[high]:
                high=mid-1
            else:
                low=mid+1
        return mini
        
        