class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        ans=[0]*n
        for i in range(n):
            while stack and temperatures[i]>stack[-1][0]:
                ans[stack[-1][1]]=i-stack[-1][1]
                stack.pop()
            stack.append((temperatures[i],i))
        return ans

        