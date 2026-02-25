def solution(sides):
    answer = 0
    max_num = max(sides)
    sum_num = sum(sides)
    return 1 if (max_num < sum_num-max_num) else 2