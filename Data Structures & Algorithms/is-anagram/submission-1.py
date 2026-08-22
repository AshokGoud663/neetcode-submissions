class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        letter=dict()
        s.lower()
        t.lower()
        for ch in s:
            letter[ch]=letter.get(ch,0)+1
        for ch in t:
            letter[ch]=letter.get(ch,0)-1
        for v in letter.values():
            if v!=0:
                return False
        return True       