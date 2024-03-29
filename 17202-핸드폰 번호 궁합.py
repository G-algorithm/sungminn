'''
문제:
어린시절 다들 한 번씩은 이름으로 궁합을 본 적이 있을 것이다. 이것과 비슷한 방식으로 중앙대학교에는 핸드폰 번호 궁합을 보는 것이 유행이라고 한다.

핸드폰 번호 궁합을 보기 위해서는 먼저 궁합을 보고싶은 두 중앙대생 A와 B의 핸드폰 번호에서 맨 앞의 010과 "-"(하이픈)을 모두 제외한 후, A부터 시작하여 한 숫자씩 번갈아가면서 적는다. 그리고 인접한 두 숫자끼리 더한 값의 일의 자리를 두 숫자의 아래에 적어나가면서 마지막에 남는 숫자 2개로 궁합률을 구하게 된다.

예를 들어, 아래의 그림과 같이 A의 번호가 010-7475-9336 이고, B의 번호가 010-3619-5974 이면, 7346715995393764에서 시작하여 070386484822030, 77314022204233, 4045424424656, 449966866011, 83852442612, 1137686873, 240344450, 64378895, 0705674, 775131, 42644, 6808, 488, 26이 되어 둘은 26%의 궁합률을 가지게 된다.
'''
a = list(input())
b = list(input())
temp = []
answer = ''

## x,y 의 요소들을 순서대로 합쳐주는 과정
for i in range(8):
    answer += a[i] + b[i]

## 문자열 answer의 길이가 2가 될 때까지 반복문
while len(answer) != 2:
    ## index 시작이 0부터이기 때문에 answer의 길이에서 1을 빼준다.
    for i in range(len(answer) - 1):
        temp.append(str((int(answer[i]) + int(answer[i + 1])) % 10))
    answer = ''.join(temp)
    temp = []

print(answer)

