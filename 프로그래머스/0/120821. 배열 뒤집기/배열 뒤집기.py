def solution(num_list):
    answer = []
    size = len(num_list)
    for i in range(size):
        answer += [num_list[size-i-1]]
    return answer