def solution(friends, gifts):
    
    n=len(friends)
    # 자료저장
    people = {name: i for i, name in enumerate(friends)} # 인덱싱
    giftCount = [[0] * n for _ in range(n)]              # 교환 횟수
    giftScore = [0] * n                                  # 선물지수
    
    # 교환횟수, 선물지수 계산
    for pair in gifts:
        give, take = pair.split()
        
        give_index = people[give]
        take_index = people[take]
        
        giftCount[give_index][take_index]+=1
        giftScore[give_index]+=1
        giftScore[take_index]-=1
    
    # next_month 자료
    next_gifts = [0] * n
    
    # 두 명씩 비교
    for first in range(n):
        for second in range(first+1, n):
            first_to_second = giftCount[first][second]
            second_to_first = giftCount[second][first]
            
            if first_to_second > second_to_first:
                next_gifts[first] += 1
            elif second_to_first > first_to_second:
                next_gifts[second] += 1
            else:
                if giftScore[first] > giftScore[second]:
                    next_gifts[first] += 1
                elif giftScore[first] < giftScore[second]:
                    next_gifts[second] += 1
                
    
    answer = max(next_gifts)
    return answer

#자료형 저장
'''
muzi: 0
ryan: 1
frodo: 2
neo: 3
을 형성하는 해시자료 형성
'''
'''
각 인물이 서로 선물을 주고 받은 2차원 배열로 선물 주고 받은 내용 저장
giftswitch["선물준사람"]["선물받은사람"] = 얼마나 줬는지 count
         muzi ryan frodo neo [준사람]
    muzi  x    x    x     x(x:전달된 선물 개수)
    ryan  x    x    x     x
    frodo x    x    x     x
    neo   x    x    x     x
  [받은사람]
'''
'''
선물지수 계산
giftScore[친구 수] = 전체 준 선물 - 전체 받은 선물
'''