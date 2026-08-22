class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set1=dict()
        # ans=[]
        for i,n in enumerate(nums):
            d=target-n
            if d in set1:
                return [set1[d],i]
            set1[n]=i

        