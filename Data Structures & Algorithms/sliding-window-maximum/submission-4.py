class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        
        left=0
        
        right=k-1
        maxi=max(nums[left:right+1])
        ans=[]
        while right<len(nums):
            ans.append(maxi)

            if nums[left]==maxi and left < right:
                maxi=max(nums[left+1:right+1])

            left+=1
            right+=1

            if right<len(nums):
                maxi=max(maxi,nums[right])
        return ans
           
        