## 시험 과목 수
n = int(input())

## int형 수를 입력받아서 list 화 한다.
s = list(map(int, input().split()))

## 예외처리
sub = len(s) - n
if sub >= 1:
    for i in range(sub):
        del s[-1]

# print(s)

## 리스트에서 최댓값을 가져오기
max = max(s)

## 값을 더해주고 그 값을 넣는 변수
sum = 0

## 새롭게 계산되는 평균값
for i in range(n):
    sum += s[i]/max*100

result = sum / n
print(result)
