def solution(genres, plays):
    answer = []
    hashdict = {} # 고유번호 : (장르, 재생횟수)
    count = {} # 장르 : 장르재생횟수
    best = {} # 장르 : [(장르,재생횟수), (..,..)]
    
    for i in range(len(genres)):
        hashdict[i] = (genres[i], plays[i])
        
        if genres[i] in count: #이미 있다면
            count[genres[i]] = count[genres[i]] + plays[i]
        else: # 해당 장르가 없다면
            count[genres[i]] = plays[i]
            
        # 장르별 리스트 정리
        if genres[i] not in best:
            best[genres[i]] = []
        best[genres[i]].append((plays[i], i))
            
    # 장르별 곡 정렬: 재생횟수 내림차,고유번호 오름차
    for genre in best:
        best[genre].sort(key=lambda x:(-x[0],x[1]))
    
    # 장르 정렬
    genre_order = sorted(count.keys(), key = lambda g: -count[g])
    
    # 장르 순서대로 상위 2개씩 고유 번호 추가
    for genre in genre_order:
        top_songs = best[genre][:2]
        for play,idx in top_songs:
            answer.append(idx)
    
    return answer

"""
1. 장르 별 총 재생회수를 계산해서 각 고유번호 별로 몇 회 재생되었는지 배열에 저장한다.
2. 장르 배열 내에서 가장 많이 재생된 노래 2개까지 저장한다(재생횟수가 동일하면 고유번호 낮은 순은로)
3. 재생횟수 높은 장르 순으로 노래 반환
"""