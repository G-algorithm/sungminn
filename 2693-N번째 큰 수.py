'''
문제:
배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.
배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.
'''

x = int(input())
for i in range(x):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[-3])