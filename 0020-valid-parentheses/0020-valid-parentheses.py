class Solution:
    def isValid(self, s: str) -> bool:
        out = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                out.append(char)
            else:
                if not out:
                    return False
                if char == ')' and out[-1] == '(':
                    out.pop()
                elif char == '}' and out[-1] == '{':
                    out.pop()
                elif char == ']' and out[-1] == '[':
                    out.pop()
                else:
                    return False
        return not out