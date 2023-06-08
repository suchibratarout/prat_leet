class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        out=0
        res=[]
        for i in s:
            if i==')':
                out-=1
            if out>0:
                res.append(i)
            if i=='(':
                out+=1
        return "".join(res)
