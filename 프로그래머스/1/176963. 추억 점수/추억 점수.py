def solution(name, yearning, photo):
    answer = []
    yearn = {names: i for names, i in zip(name, yearning)}
    
    for people in photo:
        yearnAdd=0
        for person in people:
            if person in yearn:
                yearnAdd = yearnAdd + yearn[person]
        answer.append(yearnAdd)
    
    return answer

'''
점수 dictionary {may:5, kein:10, kain:1, radi:3}
[for]photo 의 요소 수 만큼 i 로 for문을 돌릴 때
    photo 의 [i] 의 순서대로 요소를 찾는다. dict[name]
    위계산은 temp 에 합을 더한다.
for문이 종료되면 temp를 answer 에 넣어준다.

'''