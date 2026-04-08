import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;

        // 의상 종류별 개수를 저장할 Map
        HashMap<String, Integer> hashDict = new HashMap<>();

        // 각 의상의 종류(cloth[1])별로 개수 카운트
        for (String[] cloth : clothes) {
            String kind = cloth[1];
            if (hashDict.containsKey(kind)) {
                hashDict.put(kind, hashDict.get(kind) + 1);
            } else {
                hashDict.put(kind, 1);
            }
        }

        // 각 종류별로 (선택안함 포함) 경우의 수를 곱함
        for (String key : hashDict.keySet()) {
            answer *= (hashDict.get(key) + 1);
        }

        // 모든 종류에서 전부 안 입는 경우 1가지를 제외
        return answer - 1;
    }
}
