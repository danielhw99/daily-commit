function solution(date1, date2) {
  for (let i = 0; i < 3; i++) {
    if (date1[i] < date2[i]) return 1; // 처음으로 작아지는 순간: date1이 앞섬
    if (date1[i] > date2[i]) return 0; // 처음으로 커지는 순간: date1이 앞서지 않음
  }
  return 0; // 완전히 같은 날짜면 "앞선다"가 아니므로 0
}
