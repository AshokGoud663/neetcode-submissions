class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c={}
        ans=[]
        for n in nums:
            c[n]=c.get(n,0)+1
        for element, count in sorted(c.items(), key=lambda x: x[1], reverse=True)[:k]:
            ans.append(element)
        return ans

        