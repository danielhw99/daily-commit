def solution(A,B):
    n = len(A)
    count = 0
    A.sort()
    B.sort()
    C = B[::-1]
    for i in range(n):
        count += A[i] * C[i]
    return count

'''
자료구조
* 중복x, 양쪽 숫자를 곱해서 누적값이 최솟값
누적된 값

알고리즘
A를 ascending, B를 descending으로 정렬
for i in n:
    A와 B 를 순차적으로 곱해서 누적값

'''