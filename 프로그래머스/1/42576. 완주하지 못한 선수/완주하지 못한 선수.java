import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<Integer, String> hashDict = new HashMap<>();
        int hashNum = 0;
        
        

        for (String part : participant) {
            hashDict.put(part.hashCode(), part);
            hashNum += part.hashCode();
        }

        for (String comp : completion) {
            hashNum -= comp.hashCode();
        }

        answer = hashDict.get(hashNum);

        return answer;
    }
}