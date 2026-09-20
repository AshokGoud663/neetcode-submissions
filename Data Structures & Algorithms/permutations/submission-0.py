class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)
        def back(path):
            if len(nums)==len(path):
                res.append(path.copy())
                return
            for i in range(0,len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True
                
                back(path)

                path.pop()
                used[i]=False
        back([])
        return res

        