def solution(mats, park):
    answer = 0

    H = len(park)
    W = len(park[0])
    dp = [[0]*W for _ in range(H) ]
    maxSide = 0
    
    for i in range(H):
        for j in range(W):
            # 모든 자리를 확인하며 -1 이라면 dp를 쌓는다.
            if park[i][j] == "-1":
                if i==0 or j==0: # 돗자리 최대크기 1일 수 밖에 없는 좌측 최상단
                    dp[i][j] = 1 # 1로 고정
                else:
                    # 왼쪽, 위쪽, 왼대각선이 전부 비어있다면 돗자리 크기가 증가한다.
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                # 최대 변의 길이는 dp에 저장된 내용 중 가장 큰 값임
                maxSide = max(maxSide, dp[i][j])
    answer = -1
    for ans in mats:
        if ans <= maxSide:
            answer = max(answer, ans)
    
    return answer