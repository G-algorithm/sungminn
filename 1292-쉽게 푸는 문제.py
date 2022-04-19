## 1292 / https://www.acmicpc.net/problem/1292
## 시작과 끝 수 입력
a, b = map(int, input().split())

## 수열 만들기
arr = []
for i in range(1, 100):
    for j in range(i):
        arr.append(i)

print(sum(arr[a - 1:b]))