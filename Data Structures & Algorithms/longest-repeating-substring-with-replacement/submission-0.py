class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        left=0
        length=float('-inf')
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            while right-left+1-max(freq.values())>k:
                left_char=s[left]
                freq[left_char]-=1
                left+=1
            length=max(length,right-left+1)
        return length if length!=float('-inf') else 'inf'
        