class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def back(path,ind,sum_):
            if sum_==target:
                res.append(path.copy())
                return
            if ind==len(candidates):
                return
            if sum_> target:
                return
            
            path.append(candidates[ind])
            sum_+=candidates[ind]

            back(path,ind+1,sum_)

            val=path.pop()
            sum_-=val

            next_ind=ind+1
            while next_ind<len(candidates) and candidates[next_ind]==candidates[ind]:
                next_ind+=1

            back(path,next_ind,sum_)
        back([],0,0)
        return res
        