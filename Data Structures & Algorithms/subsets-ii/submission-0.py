class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dupli=set()
        res=[]
        def back(path,ind,dupli):
            # nonlocal dupli
            if len(nums)==ind:
                a=path.copy()
                t=tuple(a)
                if t not in dupli:
                    res.append(a)
                    dupli.add(t)
                    return
                return
            path.append(nums[ind])
            ind+=1
            back(path,ind,dupli)

            path.pop()
            back(path,ind,dupli)
        back([],0,dupli)
        return res

