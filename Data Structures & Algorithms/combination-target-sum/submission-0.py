class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        
        def back(path,ind,sum_):
            if sum_==target:
                res.append(path.copy())
                return
            if sum_> target:
                return
            if ind==len(nums):
                return
            path.append(nums[ind]) 
            
                                          
            back(path,ind,sum_+nums[ind])

            path.pop()
            
            back(path,ind+1,sum_)
        back([],0,0)
        return res

            

        