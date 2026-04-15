import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        int days = 0;
        int count = 0;
        
        while (progresses.length > 0) {
            if (progresses[0] + days * speeds[0] >= 100) {
                System.out.print("여기");
                progresses.pop(0);
            } 
        }
        
        return answer;
    }
}