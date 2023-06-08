class Solution:
    def removeDuplicates(self, s: str) -> str:
        out=[]
        for i in s:
            if out and out[-1]==i:
                out.pop()
            else:
                out.append(i)
        return ''.join(out)        
