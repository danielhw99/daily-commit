def solution(sizes):
    answer, maxh, maxw = 0, 0, 0
    for h, w in sizes:
        if maxh==0 and maxw==0: # 초기값
            maxh,maxw=h,w
            continue
        # 만약 h나w 둘 중 하나가 업데이트 되려하면
        if maxh < h or maxw < w:
            if max(maxh, h)*max(maxw,w) < max(maxh,w)*max(maxw,h): #바꾼게 더 크면
                maxh = max(maxh,h)
                maxw = max(maxw,w)
                print(h,w,":", maxh, maxw, "바꾼게 더 큰 경우")
            else:
                maxh = max(maxh,w)
                maxw = max(maxw,h)
                print(h,w,":", maxh, maxw, "바꾼게 더 작은 경우")
    answer = maxh*maxw                
    
    return answer

'''
어떻게 기록할건가?
: 명함이 전부 들어가는 최소 크기 지갑
언제 최소인가? h-w or w-h 
이전 값 + h-w vs 이전값 + w-h : 더 작은 거로 누적

'''