
def search_second_repeatible_string(strs: list[str]) -> str:
    from collections import Counter
    d = Counter(strs)
    if len(strs)<2:
        return ''.join(strs)

    d = sorted(d.items(),key=lambda x:x[1],reverse=True)
    for i in range(len(d)-1):
        if d[i][1] > d[i+1][1]:
            return d[i+1][0]

print(search_second_repeatible_string(['a','a','a','ba','c','c','c',1,1]))
