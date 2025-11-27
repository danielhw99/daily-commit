from collections import deque

def solution(blen, weight, tw):
    answer = 0
    
    bq = deque([0] * blen)   # 다리 위 상태
    tw = deque(tw)            # 남은 트럭들
    cur = 0                   # 다리 위 총 무게
    
    # 다리가 빌 때 까지
    while bq:
        # 1초 경과
        answer += 1
        
        # 먼저 한 칸 전진 -> 맨 앞 트럭/빈칸 내려감
        off = bq.popleft()
        cur -= off
        
        # 아직 대기 트럭 있으면, 다음 트럭 올릴지 결정
        if tw:        
            # 다음차가 올라올 수 있다면
            if cur + tw[0] <= weight:
                added = tw.popleft()
                bq.append(added)
                cur += added
            # 아니면 빈칸
            else:
                bq.append(0)
        
        # 더 이상 대기 트럭이 없으면
        else:
            if sum(bq) == 0:
                break
            bq.append(0)
    
    return answer