import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> answer = new ArrayList<>();
        for(int cur:arr){
            boolean flag = true;
            for(int del:delete_list){
                if(cur==del) flag=false;
            }
            if(flag) answer.add(cur);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}