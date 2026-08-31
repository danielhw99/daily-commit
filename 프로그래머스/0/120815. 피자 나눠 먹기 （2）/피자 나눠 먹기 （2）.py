import math

def solution(n):
    # 최소공배수 구하는 문제
    answerlcm = math.lcm(n, 6)
    answer = answerlcm/6
    return answer