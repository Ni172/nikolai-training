# def largest_palindromic_number(S):
#     from collections import Counter
#     # Remove leading zeros
#     # S = S.lstrip('0')
#     # If the resulting string is empty, it means there were only zeros in the input
#     if not S:
#         return "0"
#     # Sort the string in decreasing order to get the largest digits first
#     sorted_digits = sorted(S, reverse=True)
#     # Find the middle index or indices depending on the length
#     N = len(sorted_digits)
#     if N % 2 == 0:
#         mid1 = N // 2 - 1
#         mid2 = N // 2
#     else:
#         mid1 = mid2 = N // 2
#     # Create the first part by taking the largest digits up to mid1
#     first_part = "".join(sorted_digits[:mid1 + 1])
#     # Create the second part by taking the largest digits from mid2 onwards
#     second_part = "".join(sorted_digits[mid2:])
#     # Reverse the first part and append it to the end of the second part
#     result = second_part + first_part
#     return result
#
# print(largest_palindromic_number('39878'))



# def largest_palindromic_number(S):
#     # Count the occurrences of each digit
#     digit_count = [0] * 10
#     for digit in S:
#         digit_count[int(digit)] += 1
#
#     # Find the largest odd digit (since even occurrences of digits can be placed in the middle)
#     largest_odd_digit = 9
#     while digit_count[largest_odd_digit] % 2 == 0:
#         largest_odd_digit -= 1
#
#     # Initialize the result string with the largest odd digit
#     result = str(largest_odd_digit)
#
#     # Decrease the count of the largest odd digit
#     digit_count[largest_odd_digit] -= 1
#
#     # Build the first half of the palindrome
#     for i in range(9, -1, -1):
#         result += str(i) * (digit_count[i] // 2)
#
#     # Build the second half of the palindrome by reversing the first half
#     result += result[-1::-1]
#
#     return result
#
# # Example usage:
# S = "39878"
# result = largest_palindromic_number(S)
# print(result)  # Output will be "989"


# def largest_palindromic_number(S):
#     from collections import Counter
#     if sum([int(i) for i in S]) == 0:
#         return '0'
#     d = Counter(S)
#     single_digit = True
#     for k, v in d.items():
#         if v != 1:
#             single_digit = False
#             break
#     if single_digit:
#         return max(S)
#
#     digit_count = [0] * 10
#     for digit in S:
#         digit_count[int(digit)] += 1
#
#     first_half = []
#     second_half = []
#
#     middle_digit = ""
#     for digit in range(9, -1, -1):
#         if digit_count[digit] % 2 == 1:
#             middle_digit = str(digit)
#             digit_count[digit] -= 1
#             break
#
#     for digit in range(9, -1, -1):
#         if digit_count[digit] > 0:
#             half_count = digit_count[digit] // 2
#             first_half.extend([str(digit)] * half_count)
#
#     second_half = first_half[::-1]
#
#     palindrome = "".join(first_half) + middle_digit + "".join(second_half)
#
#
#     return palindrome.strip('0')
#
# # Example usage:
# # S = "1128321"
# S = "11283218977777"
# # S = "123456"
# result = largest_palindromic_number(S)
# print(result)  # Output will be "989"
#


# def solution(inner, outer, points_x, points_y):
#
#     l = []
#     import math
#
#
#     for x, y in zip(points_x, points_y):
#         distance_to_circle1 = math.sqrt((x - inner) ** 2 + (y - outer) ** 2)
#         distance_to_circle2 = math.sqrt((x - inner) ** 2 + (y - outer) ** 2)
#
#     return l
#
# print(solution(1, 3, [0,1,2,-2,3],[0,1,4,1,0]))

