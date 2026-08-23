class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1=set()
        i,j=0,0
        length=0
        while j<len(s):
            if s[j] not in set1:
                set1.add(s[j])
                j+=1
            else:

                length=max(length,j-i)
                while i<j and s[i]!=s[j]:
                    set1.remove(s[i])
                    i+=1
                set1.remove(s[i])
                i+=1
                
            length=max(length,j-i)
        return length
        