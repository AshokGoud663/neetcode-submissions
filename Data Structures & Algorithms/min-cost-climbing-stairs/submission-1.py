class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n<=1:
            return 0
        if n<3:
            return min(cost)
        arr=[0]*(n+1)
        
        for i in range(2,n+1):
            arr[i]=min(arr[i-1]+cost[i-1],arr[i-2]+cost[i-2])
        return arr[n]
        