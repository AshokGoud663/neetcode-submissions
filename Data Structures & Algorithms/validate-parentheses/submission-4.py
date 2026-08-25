class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        find={')':'(','}':'{',']':'['}
        for c in s:
            if c in find:
                if stack and stack[-1]==find[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack)==0
        

        