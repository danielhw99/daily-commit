function solution(arr) {
    var answer = 1;
    
    for (let i=0;i<arr.length;i++){
        for(let j=i;j<arr[i].length;j++){
            if (arr[i][j] != undefined) {
                if (arr[i][j] == arr[j][i]) {
                    continue
                } else {
                    return 0;
                }
            }
        }
    }
    return answer;
}