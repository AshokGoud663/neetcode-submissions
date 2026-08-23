class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values=set(nums)
        freq={}
        for n in nums:
            if n-1 not in values:
                c=0
                k=n
                while k in values:
                    c+=1
                    k+=1
                freq[n]=c
        return 0 if not freq else max(freq.values())
            

        