import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        low=1
        high=max(piles)
        k=float('inf')
        while low<=high:
            time=0
            mid=(low+high)//2
            for n in piles:
                time+=math.ceil(n/mid)
            
            if time<=h:
                k=min(k,mid)
                high=mid-1
            else:
                low=mid+1
        return k


        