class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p=p[::-1].replace('**','**\\')[::-1]
        return re.match(f"^{p}$",s)
        