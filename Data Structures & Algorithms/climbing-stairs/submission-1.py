class Solution:
    def climbStairs(self, n: int) -> int:
        if n<1:
            return 0
        if n==1 or n==2:
            return n
        prev1=1
        prev2=2
        for _ in range(n-2):
            temp=prev1+prev2
            prev1=prev2
            prev2=temp
        return prev2
        