def solution(array, height):
    answer = 0
    for H in array:
        if height < H:
            answer += 1
    return answer