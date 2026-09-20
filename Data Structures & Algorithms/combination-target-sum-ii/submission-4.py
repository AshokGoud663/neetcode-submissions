class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def back(path,ind,remaining):
            if remaining ==0:
                res.append(path.copy())
                return
            if ind==len(candidates) or candidates[ind]>remaining:
                return
            path.append(candidates[ind])
            back(path,ind+1,remaining-candidates[ind])

            path.pop()

            next_ind=ind+1
            while next_ind<len(candidates) and candidates[next_ind]==candidates[ind]:
                next_ind+=1
            back(path,next_ind,remaining)
        back([],0,target)
        return res
        