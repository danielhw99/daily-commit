import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> result = new ArrayList<>();

        // 배열을 앞에서부터 순회하면서
        // 이전 값과 다를 때만 결과에 추가
        for (int i = 0; i < arr.length; i++) {
            if (i == 0) {
                result.add(arr[i]); // 첫 값은 무조건 추가
            } else if (arr[i] != arr[i - 1]) {
                result.add(arr[i]); // 연속 중복이 아니면 추가
            }
        }

        // List -> int[] 변환
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }
}
