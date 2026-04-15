import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        List<Integer> days = new ArrayList<>();

        // 각 작업이 완료되기까지 필요한 날짜를 계산
        for (int i = 0; i < progresses.length; i++) {
            int remain = 100 - progresses[i];
            int day = (remain + speeds[i] - 1) / speeds[i]; // 올림 계산
            days.add(day);
        }

        // 첫 번째 작업의 완료일을 기준으로 배포 묶음 시작
        int current = days.get(0);
        int count = 1;

        for (int i = 1; i < days.size(); i++) {
            // 현재 기준일보다 빨리 끝나거나 같은 날 끝나면 함께 배포
            if (days.get(i) <= current) {
                count++;
            } else {
                // 새로운 배포 묶음 시작
                answer.add(count);
                current = days.get(i);
                count = 1;
            }
        }

        // 마지막 배포 묶음 추가
        answer.add(count);

        // List<Integer>를 int[]로 변환
        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }

        return result;
    }
}
