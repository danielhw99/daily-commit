import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        // 중복 제거를 위한 HashSet사용
        HashSet<Integer> setNums = new HashSet<>();
        
        // nums 배열의 값을 HashSet에 넣어 종류 수를 구함
        for (int num:nums) {
            setNums.add(num);
        }
        
        // 최대 선택 가능한 개수는 nums 길이의 절반
        int pickable = nums.length/2;
        
        // 선택 가능한 개수보다 종류 수가 더 많으면
        // 최대 선택 개수만큼만 고를 수 있음
        if (pickable < setNums.size()) {
            answer = pickable;
        } else {
            // 종류 수가 더 적거나 같으면 종류 수만큼 선택 가능
            answer = setNums.size();
        }
                
        return answer;
    }
}