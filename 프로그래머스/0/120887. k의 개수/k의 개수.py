def solution(i, j, k):
    count = 0

    for number in range(i, j + 1):
        count += str(number).count(str(k))

    return count