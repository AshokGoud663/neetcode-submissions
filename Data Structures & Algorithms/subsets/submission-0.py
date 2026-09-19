class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(nums, path, ind, res):
            if ind == len(nums):
                res.append(path.copy())  # important
                return

            path.append(nums[ind])
            backtrack(nums, path, ind + 1, res)

            path.pop()
            backtrack(nums, path, ind + 1, res)

        backtrack(nums, [], 0, res)
        return res

