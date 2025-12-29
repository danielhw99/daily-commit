function solution(n) {
    // n x n 배열을 0으로 초기화
    const answer = Array.from({ length: n }, () => Array(n).fill(0));

    // 이동 방향: 오른쪽, 아래, 왼쪽, 위
    const directions = [
        [0, 1],   // →
        [1, 0],   // ↓
        [0, -1],  // ←
        [-1, 0]   // ↑
    ];

    let num = 1;     // 채울 숫자
    let x = 0, y = 0; // 현재 위치
    let d = 0;       // 방향 인덱스

    while (num <= n * n) {
        answer[x][y] = num++;
        
        // 다음 위치 계산
        let nx = x + directions[d][0];
        let ny = y + directions[d][1];

        // 범위를 벗어나거나 이미 값이 있으면 방향 전환
        if (
            nx < 0 || ny < 0 ||
            nx >= n || ny >= n ||
            answer[nx][ny] !== 0
        ) {
            d = (d + 1) % 4; // 방향 전환
            nx = x + directions[d][0];
            ny = y + directions[d][1];
        }

        x = nx;
        y = ny;
    }

    return answer;
}
