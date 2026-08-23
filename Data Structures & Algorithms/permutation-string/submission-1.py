from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        i=0
        while i<len(s2)-l1+1:
            if Counter(s1)==Counter(s2[i:i+l1]):
                return True
            i+=1
        return False
        