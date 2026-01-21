from collections import deque
def solution(players, callings):
    answer = []
    pos = {name: i for i, name in enumerate(players)}
    
    for name in callings:
        # 해당 선수의 인덱스 위치 idx에 저장
        idx = pos[name]
        # 해당 선수 앞 위치
        front = players[idx-1]
        
        # swap
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
        pos[name] = idx-1
        pos[front] = idx
    
    return players