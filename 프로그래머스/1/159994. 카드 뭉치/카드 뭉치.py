def solution(cards1, cards2, goal):
    answer = 'Yes'
    for item in goal:
        if len(cards1) <1 and len(cards2)<1: break
        if len(cards1) >= 1 and item == cards1[0]:
            cards1 = cards1[1:]
        elif len(cards2) >= 1 and item == cards2[0]:
            cards2 = cards2[1:]
        else:
            return 'No'
        print(item)
    return answer