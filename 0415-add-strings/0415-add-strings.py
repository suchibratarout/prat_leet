class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(100000)
        v=int(num1)
        v1=int(num2)
        return str(v+v1)