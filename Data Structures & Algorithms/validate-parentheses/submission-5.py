class Solution:
    def isValid(self, s: str) -> bool:
        find={')':'(','}':'{',']':'['}
        stack=[]
        for ch in s:
            if ch in find:
                if stack and stack[-1]==find[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack)==0
            
                
        