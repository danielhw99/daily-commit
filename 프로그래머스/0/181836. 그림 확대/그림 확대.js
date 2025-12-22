function solution(picture, k) {
    var answer = [];
    
    for (var i=0; i<picture.length;i++) {
        var temp = ""
        for (var j = 0; j<picture[i].length;j++) {
            insert = picture[i][j];
            for (var z=0;z<k;z++) {
                temp += insert;
            }
        }
        for ( var x=0; x<k;x++) {
            answer.push(temp);
        }
    }
    
    return answer;
}