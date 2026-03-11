SELECT PT_NAME, 
       PT_NO, 
       GEND_CD, 
       AGE, 
       IFNULL(TLNO, 'NONE') AS TLNO -- 전화번호가 없으면 'NONE'으로 표시 (선택사항)
  FROM PATIENT
 WHERE GEND_CD = 'W'             -- 성별이 여자인 환자
   AND AGE BETWEEN 1 AND 12      -- 나이가 12세 이하인 환자
 ORDER BY AGE DESC, PT_NAME ASC; -- 보통 나이 내림차순, 이름 오름차순 정렬 조건이 붙습니다.