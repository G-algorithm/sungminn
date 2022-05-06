def solution(s):
    s = s[2:-2].split("},{")
    numArr = []
    for i in range(len(s)):
        S = s[i].split(",")
        numArr.append(set(S))

    numArr.sort(key=lambda x: len(x))

    ans = set()
    res = []
    for a in numArr:
        tmp = a - ans
        res.append(list(tmp)[0])
        ans = ans | tmp

    res = [int(i) for i in res]
    print(res)
    return res

s = input()
solution(s)