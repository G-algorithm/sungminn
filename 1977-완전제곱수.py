'''
문제:
M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 64, 81, 100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.
'''
import math

M = int(input())
N = int(input())

## condition
if M > N:
    print('M>N 이므로 조건을 충족하지 않습니다. 확인해주세요!')
    exit()
else:
    if (M > 10000) or (N > 10000):
        print('M or N > 10000 이므로 조건을 충족하지 않습니다. 확인해주세요!')
        exit()

M_a = math.ceil(M**(1/2))
N_a = math.floor(N**(1/2))

arr = []
sum = 0
for i in range(M_a, N_a+1):
    arr.append(i**2)
    sum += (i**2)

if len(arr)==0:
    print("-1")
    exit()

print(sum)
print(min(arr))