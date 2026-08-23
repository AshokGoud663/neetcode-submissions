class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi=0
        i=0
        j=len(heights)-1
        while i<j:
            h=min(heights[i],heights[j])
            b=j-i
            maxi=max(maxi,h*b)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxi
        