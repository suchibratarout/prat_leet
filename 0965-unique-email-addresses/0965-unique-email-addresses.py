class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        out=set()
        for i in emails:
            v,v1=i.split('@')
            if '+' in v:
                v=v[:v.index('+')]
            v=v.replace('.','')
            out.add(v+'@'+v1)
        return len(out)