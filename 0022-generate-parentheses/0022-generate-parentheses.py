class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        result = []
        for i in range(n):
            list1 = self.generateParenthesis(i)
            list2 = self.generateParenthesis(n - i - 1)
            for left, right in product(list1, list2):
                result.append('({}){}'.format(left, right))
        return result