import java.util.*;

class Solution {
    
    int[] sorting(int[] num_list) {
        int head = 0;
        int mid = (num_list.length+head)/2+1;
        System.out.println("mid: "+mid+"\nhead: "+head);
        
        return num_list;
    }
    
    public int[] solution(int[] num_list) {
        int[] answer = new int[5];
        
        Arrays.sort(num_list);
        
        for(int i=0;i<5;i++) {
            answer[i] = num_list[i];
        }
        
        
        return answer;
    }
}