class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def back(path,r_used,l_used):
            if len(path)==2*n :
                res.append("".join(path))
                return

            if l_used<n:
                path.append('(')
                back(path,r_used,l_used+1)
                path.pop()
            if r_used<l_used:
                path.append(')')
                back(path,r_used+1,l_used)
                path.pop()
        back([],0,0)
        return res


        