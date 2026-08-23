class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1=set()
        i,lent=0,0
        for r in range(len(s)):
            while s[r] in set1:
                set1.remove(s[i])
                i+=1
            set1.add(s[r])
            lent=max(lent,r-i+1)
        return lent
        