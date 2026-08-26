class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        area=float('-inf')
        for r in range(len(heights)):
            while stack and heights[stack[-1]]>heights[r]:
                mid=stack.pop()
                left= -1 if not stack else stack[-1]
                wid=r-left-1
                area=max(area,wid*heights[mid])
            stack.append(r)
        
        right=len(heights)
        while stack:
            mid=stack.pop()
            left=-1 if not stack else stack[-1]
            wid=right-left-1
            area=max(area,wid*heights[mid])
        return area
        


        