from functools import reduce

def solution(n):
    return reduce(lambda a, i: a + ('수' if i % 2 == 0 else '박'),range(n),'')