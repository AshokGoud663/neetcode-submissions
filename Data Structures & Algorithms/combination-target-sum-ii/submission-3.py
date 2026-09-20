class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def back(path,ind,sum_):
            if sum_==target:
                res.append(path.copy())
                return
            if ind==len(candidates) or sum_>target:
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                path.append(candidates[i])
                back(path,i+1,sum_+candidates[i])
                path.pop()
        back([],0,0)
        return res

        