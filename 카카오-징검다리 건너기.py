def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0
    while left <= right:
        blankCount = 0

        mid = (right + left) // 2

        for stone in stones:
            if stone - mid <= 0:
                blankCount += 1
            else:
                blankCount = 0

            if blankCount >= k:
                break

        if blankCount < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer





    answer = 0
    return answer