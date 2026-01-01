function solution(arr) {
    const row = arr.length;
    const col = arr[0].length;
    const max = Math.max(row, col);

    for (let i = 0; i < row; i++) {
        while (arr[i].length < max) {
            arr[i].push(0);
        }
    }

    while (arr.length < max) {
        arr.push(new Array(max).fill(0));
    }

    return arr;
}
