class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n<=1:
            return 0
        if n==2:
            return min(cost)
        p1=0
        p2=0
        for i in range(2,n+1):
            temp=min(p1+cost[i-2],p2+cost[i-1])
            p1=p2
            p2=temp
        return p2
        