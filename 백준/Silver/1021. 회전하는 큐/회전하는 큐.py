# BOJ 1021 - 회전하는 큐 (Python)
import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    targets = list(map(int, input().split()))

    dq = deque(range(1, n + 1))
    ops = 0

    for x in targets:
        idx = dq.index(x)          # x의 현재 위치
        left = idx                 # 왼쪽 회전 횟수
        right = len(dq) - idx      # 오른쪽 회전 횟수

        if left <= right:
            dq.rotate(-left)       # 왼쪽으로 left번 (음수는 왼쪽)
            ops += left
        else:
            dq.rotate(right)       # 오른쪽으로 right번
            ops += right

        dq.popleft()               # 맨 앞 원소 제거 (x)

    print(ops)

if __name__ == "__main__":
    main()
