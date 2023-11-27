# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         n_bin = bin(n)
#         return len([i for i in n_bin[2:] if i == '1'])
#
# print(Solution().hammingWeight(2))

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_bracket = '(('
        close_bracket = '))'
        pair = '()'
        total_pairs = ''
        l = []
        c = 0
        for i in range(len(s)-1):
            if s[i:i+1] == open_bracket:
                c += 1
        return total_pairs



print(Solution().removeOuterParentheses("(()()),(()),(()(()))"))