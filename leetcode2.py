# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         triplets = set()
#         for i in range(len(nums) - 2):
#             firstNum = nums[i]
#             j = i + 1
#             k = len(nums) - 1
#             while j < k:
#                 secondNum  = nums[j]
#                 thirdNum = nums[k]
#
#                 potentialSum = firstNum + secondNum + thirdNum
#                 if potentialSum > 0:
#                     k -= 1
#                 elif potentialSum < 0:
#                     j += 1
#                 else:
#                     triplets.add((firstNum , secondNum ,thirdNum))
#                     j += 1
#                     k -= 1
#         return triplets
#
# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         i = 0
#         k = len(height) - 1
#         area_max = 0
#         while i < k:
#             min_number = min(height[i], height[k])
#             distance = k - i
#             area_max = max(area_max, min_number * distance)
#             if height[i] < height[k]:
#                 i += 1
#             else:
#                 k -= 1
#         return area_max
#
# print(Solution().maxArea([-1, 0, 1, 2, -1, -4]))

# class Solution(object):
#     def isValidSudoku(self, board):
#         res = []
#         for i in range(9):
#             for j in range(9):
#                 element = board[i][j]
#                 if element != '.':
#                     res += [(i, element), (element, j), (i // 3, j // 3, element)]
#         return len(res) == len(set(res))
#
# print(Solution().isValidSudoku(
# [["5","3",".",".","7",".",".",".","."]
# ,["5",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 1: return n
#         l = [0] * (n+1)
#         l[1] = 1
#         l[2] = 2
#         for i in range(3, n+1):
#             l[i] = l[i-1] + l[i-2]
#         print(l)
#         return l[n]
#
# print(Solution().climbStairs(0))

# class Solution:
#     def findKthPositive(self, arr: list[int], k: int) -> int:
#         l = []
#         for i in range(1, arr[-1] + 1):
#             if i not in arr:
#                 l.append(i)
#         if len(l) >= k:
#             return l[k-1]
#         else:
#             return arr[-1] + (k - len(l))
#
# print(Solution().findKthPositive([2], 1))

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         bin_number = bin(n)[2:]
#         bin_number_32bit = '0' * (32 - len(bin_number)) + bin_number
#         return int(bin_number_32bit[::-1],2)
#
# print(Solution().reverseBits(43261596))