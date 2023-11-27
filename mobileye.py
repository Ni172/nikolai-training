

# def solution(S):
#     # write your code in Python 3.6
#     S=S.replace(' ','')
#     S=S.replace('-','')
#     if len(S) < 4:
#         return S
#     if len(S) == 4:
#         return '-'.join([S[i:i + 2] for i in range(0, len(S), 2)])
#     if len(S)%3==1:
#         first_sub_string = S[:-4]
#         second_sub_string = S[-4:]
#         first = '-'.join([first_sub_string[i:i + 3] for i in range(0, len(first_sub_string), 3)])
#         second = '-'.join([second_sub_string[i:i + 2] for i in range(0,len(second_sub_string),2)])
#         return first + '-' + second
#     else:
#         return '-'.join([S[i:i + 3] for i in range(0, len(S), 3)])
#
# print(solution(' -0 - 22 1985--3245555-')) # '0 - 22 1985--324' --> 022-198-53-24
# # '0 - 22 1985--32' --> 022-198-532