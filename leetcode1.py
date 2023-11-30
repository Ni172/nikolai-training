# class Solution:
#     def isValid(self, s: str) -> bool:
#         open_brackets = '({['
#         close_brackets = ')}]'
#         l = ['1']
#         for i in s:
#             if i in open_brackets:
#                 l.append(i)
#             if i in close_brackets:
#                 if (i == ')' and l[-1] == '(') or (i == ']' and l[-1] == '[') or (i == '}' and l[-1] == '{'):
#                     l.pop()
#                 else:
#                     return False
#         if len(l) == 1:
#             return True
#         else:
#             return False
# print(Solution().isValid('{[)]}'))

# class Solution:
#     def longestCommonPrefix(self, v: list[str]) -> str:
#         ans=""
#         v=sorted(v)
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans
# a = Solution()
# print(a.longestCommonPrefix(["flower","flow","flight"]))

# class Solution:
#     def mergeTwoLists(self, list1: list, list2: list) -> list:
#         return sorted(list1 + list2)
#
# print(Solution().mergeTwoLists([1,3], [0,2,6]))

# from collections import Counter
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         return len(Counter(nums))
#
# a = Solution()
# print(a.removeDuplicates([1, 1, 2]))

# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         return len([num for num in nums if num != val])
#
# print(Solution().removeElement([0,1,2,2,3,0,4,2], 3))

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle in haystack:
#             for i in range(len(haystack)):
#                 if haystack[i:i + len(needle)] == needle:
#                     return i
#         else:
#             return -1
#
# print(Solution().strStr("eqqqqqqqqqsadbutsad", "sad"))

# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         if len(nums) == 0:
#             return 0
#         for i in range(len(nums)):
#             if nums[i] >= target:
#                 return i
#         return len(nums)
#
# print(Solution().searchInsert([1,8, 9,23], 15))

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         d = {}
#         for i in range(len(nums)):
#             diff = target - nums[i]
#             if diff in d:
#                 return [d[diff], i]
#             else:
#                 d[nums[i]] = i
#
# print(Solution().twoSum([1,8,23,9], 17))

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if target == nums[i] + nums[j]:
#                     return [i, j]
#
# print(Solution().twoSum([1,9,23,5,9,10], 11))

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return str(bin(int(a, 2) + int(b, 2)))[2:]
#
# print(Solution().addBinary('11', '1'))

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         number=1
#         while number*number<=x:
#             number+=1
#         return number-1
#
# print(Solution().mySqrt(100))


# class Solution:
#     def removeDuplicates(self, nums: list[int]):
#         l = []
#         for i in nums:
#             if i not in l:
#                 l.append(i)
#         return l
#
# print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         profit = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[j] - prices[i] > 0:
#                     profit = max(prices[j] - prices[i], profit)
#         return profit
#
# print(Solution().maxProfit([7,1,5,3,6,4]))

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         profit = 0
#         buy = prices[0]
#         for i in prices[1:]:
#             if i > buy:
#                 profit = max(profit, (i-buy))
#             else:
#                 buy = i
#         return profit
#
# print(Solution().maxProfit([1,5,3,6,4,2,10]))

# class Solution:
#     def rotate(self, nums: list[int], k: int) -> list:
#
#         if k == 0 or len(nums) <= 1 or k == len(nums):
#             return nums
#         else:
#             k = k % len(nums)
#             return nums[-k:] + nums[:(len(nums) - k)]
#
# print(Solution().rotate([1,2,3,4,5,6,7], 10))

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         t = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         number = 0
#         for i in range(len(s) - 1):
#             if t[s[i]] < t[s[i+1]]:
#                 number -= t[s[i]]
#             else:
#                 number += t[s[i]]
#         return number + t[s[-1]]
#
# print(Solution().romanToInt("DIV"))

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         pointer = 0
#         for i in s:
#             try:
#                 pointer = t.index(i, pointer)
#                 pointer += 1
#             except:
#                 return False
#         return True
#
# print(Solution().isSubsequence('cg', 'bcbg'))


# class Solution:
#     def partitionString(self, s: str) -> int:
#         temp_s = ''
#         l1 = []
#         for i in s:
#             if i in temp_s:
#                 l1.append(''.join(ch for ch in temp_s))
#                 temp_s = ''
#                 temp_s += i
#             else:
#                 temp_s += i
#         if len(temp_s) != 0:
#             return len(l1) + 1
#         return len(l1)
#
# print(Solution().partitionString("ab cv"))

# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         zero_length = len(nums1) - m + len(nums2) - n
#         for n in nums2:
#             nums1.append(n)
#
#         for _ in range(zero_length):
#             nums1.remove(0)
#         nums1.sort()
#
# nums1 = [1,2,3,0,0,0]
# print(Solution().merge(nums1, 3, [2,0,5,6], 3))


# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         from collections import Counter
#         ransomNote = Counter(ransomNote)
#         magazine = Counter(magazine)
#         for k,v in ransomNote.items():
#             if k in magazine:
#                 if v > magazine[k]:
#                     return False
#         return True
#
# print(Solution().canConstruct("bcaa", "aab"))

# class Solution:
#     def isIsomorphic(self, s, t):
#         map1 = []
#         map2 = []
#         for idx in s:
#             map1.append(s.index(idx))
#         for idx in t:
#             map2.append(t.index(idx))
#         if map1 == map2:
#             return True
#         return False
#
# print(Solution().isIsomorphic("zxtxp", "abcbp"))

# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         l = []
#         d = {}
#         for word in strs:
#             temp = ''.join(sorted(word))
#             if temp in d:
#                 d[temp].append(word)
#             else:
#                 d[temp] = [word]
#         for k, v in d.items():
#             l.append(d[k])
#         return l

# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         from collections import defaultdict
#         d_l = defaultdict(list)
#         for word in strs:
#             sorted_word = ''.join(sorted(word))
#             d_l[sorted_word].append(word)
#         return list(d_l.values())
#
# print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         l = []
#         while n != 1:
#             c = 0
#             for i in str(n):
#                 c += int(i)**2
#             n = c
#             if n in l:
#                 return False
#             l.append(n)
#         return True
#
# print(Solution().isHappy(2))

# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return 1
#         nums = sorted(nums)
#         count = 1
#         l = [1]
#         for i in range(len(nums)-1):
#             if nums[i+1] - nums[i] < 2:
#                 count += nums[i+1] - nums[i]
#             else:
#                 l.append(count)
#                 count = 1
#         l.append(count)
#         return sorted(l)[-1]
#
# print(Solution().longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))

# class Solution:
#     def merge(self, intervals: list[list[int]]) -> list[list[int]]:
#         l = []
#         intervals = sorted(intervals, key=lambda x:x[0])
#         for i in intervals:
#             if l == [] or l[-1][1]<i[0]:
#                 l.append(i)
#             else:
#                 max_num = max(l[-1][1], i[1])
#                 l[-1][1] = max_num
#         return l
#
# print(Solution().merge([[15,18],[1,3],[10,9], [2,11]]))


# class Solution:
#     def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
#         temp = int
#         if len(matrix)==1:
#             if target in matrix[0]:
#                 temp = target
#
#         for i in range(len(matrix) - 1):
#             if sorted(matrix[i]) != matrix[i]:
#                 return False
#             if target in matrix[i] or target in matrix[i+1]:
#                 temp = target
#             if matrix[i+1][-1]<matrix[i][0]:
#                 return False
#         return temp == target
#
# print(Solution().searchMatrix([[1,3,5,7],[10,1,16,20],[23,30,34,60]], 3))


# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         d = {}
#         for i in nums:
#             d[i] = d.get(i, 0) + 1
#             # if i in d:
#             #     d[i] += 1
#             # else:
#             #     d[i] = 1
#         for k,v in d.items():
#             if v == 1:
#                 return k
#
# print(Solution().singleNumber([1,1,3,2,2]))

# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         if n == 0:
#             return 0
#         sum = 1
#         count = 0
#         for i in range(1, n + 1):
#             sum = sum * i
#         while sum % 10 == 0:
#             count += 1
#             sum = sum // 10
#         return count
#
# print(Solution().trailingZeroes(3))