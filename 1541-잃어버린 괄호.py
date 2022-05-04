m = input().split('-')
# 첫 숫자가 음수일 경우의 오류처리
if m[0] == '':
    m[0] = '0'
num = []
for i in m:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

