class Solution:
    def reverseVowels(self, s: str) -> str:
        out=''
        new=''
        for i in s:
            if i in 'aeiouAEIOU':
                new=i+new
        n=0
        for i in s:
            if i in 'aeiouAEIOU':
                out=out+new[n]
                n+=1
            else:
                out+=i
        return out
                
        