class Solution {
    public String solution(String n_str) {
        StringBuilder answer = new StringBuilder();
        boolean flag = false;
        
        for(int i=0;i<n_str.length();i++){
            char c = n_str.charAt(i);
            if(!flag && c =='0'){
                continue;
            }
            if(!flag && c!='0'){
                flag=true;
            }
            answer.append(c);
            //System.out.println(n_str.charAt(i));
                
        }
        return answer.toString();
    }
}