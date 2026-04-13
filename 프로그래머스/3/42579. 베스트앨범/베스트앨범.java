import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        // 장르별 총 재생 횟수
        Map<String, Integer> count = new HashMap<>();
        // 장르별 곡 목록: (재생횟수, 고유번호)
        Map<String, List<int[]>> best = new HashMap<>();

        // 1) 장르별 총 재생 횟수 계산 + 장르별 곡 리스트 구성
        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];

            count.put(genre, count.getOrDefault(genre, 0) + play);

            best.putIfAbsent(genre, new ArrayList<>());
            best.get(genre).add(new int[]{play, i});
        }

        // 2) 장르별 곡 정렬: 재생횟수 내림차순, 고유번호 오름차순
        for (String genre : best.keySet()) {
            best.get(genre).sort((a, b) -> {
                if (a[0] != b[0]) return b[0] - a[0]; // 재생횟수 내림차순
                return a[1] - b[1];                  // 고유번호 오름차순
            });
        }

        // 3) 장르 정렬: 총 재생횟수 내림차순
        List<String> genreOrder = new ArrayList<>(count.keySet());
        genreOrder.sort((g1, g2) -> count.get(g2) - count.get(g1));

        // 4) 장르 순서대로 상위 2곡씩 고유번호 추출
        List<Integer> answerList = new ArrayList<>();
        for (String genre : genreOrder) {
            List<int[]> songs = best.get(genre);
            for (int i = 0; i < Math.min(2, songs.size()); i++) {
                answerList.add(songs.get(i)[1]); // 고유번호
            }
        }

        // List -> int[] 변환
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}
