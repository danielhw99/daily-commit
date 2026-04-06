import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        HashMap<String, Integer> hashDict = new HashMap<>();
        
        for (String phoneN:phone_book) {
            hashDict.put(phoneN,1);
        }
        
        
        for (String nums : phone_book) {
            String arr = "";
            
            for (int i=0;i<nums.length();i++) {
                arr += nums.charAt(i);
                
                if (hashDict.containsKey(arr) && !arr.equals(nums))  {
                    answer = false;
                }
            }
        }
        
        return answer;
    }
}