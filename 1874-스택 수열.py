import sys
## 입력받기
## 일반적으로 input()을 많이 쓰지만 복수의 입력을 받게되면 시간초과될 수 있음
input = sys.stdin.readline

## n = int(sys.stdin.readline)
n = int(input()) ## 수열의 갯수
targets = [int(input()) for _ in range(n)] ## 입력으로 넣어준 수열이 리스트로 만들어짐
current = 1 ## 오름차순으로 카운팅 될 값
stack, answer = [], [] ## 스택의 요소와 답을 담아놓을 빈 배열

print(targets)
for target in targets:
    ## 오름차순대로 진행하는 과정
    while current <= target:
        stack.append(current)
        answer.append('+')
        current += 1

    ## pop
    if stack[-1] == target:
        answer.append('-')
        stack.pop()

## stack에 요소가 없다면 pop push 출력
if not stack:
    print('\n'.join(answer))
else:
    print('No')