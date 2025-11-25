# [level 2] 올바른 괄호 - 12909 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12909) 

### 성능 요약

메모리: 9.31 MB, 시간: 9.26 ms

### 구분

코딩테스트 연습 > 스택／큐

### 채점결과

정확성: 69.5<br/>효율성: 30.5<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 11월 25일 11:59:39

### 문제 설명

<p>괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어</p>

<ul>
<li>"()()" 또는 "(())()" 는 올바른 괄호입니다.</li>
<li>")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.</li>
</ul>

<p>'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.</p>

<h5>제한사항</h5>

<ul>
<li>문자열 s의 길이 : 100,000 이하의 자연수</li>
<li>문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>"()()"</td>
<td>true</td>
</tr>
<tr>
<td>"(())()"</td>
<td>true</td>
</tr>
<tr>
<td>")()("</td>
<td>false</td>
</tr>
<tr>
<td>"(()("</td>
<td>false</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1,2,3,4<br>
문제의 예시와 같습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 문제 풀이

첫 문제 풀이는 다음과 같다.
```java

def solution(s):
    answer = True

    arr= []
    counter = 0
    for c in s:
        if len(arr) == 0:
            if c != '(:
                return False
            arr.append(c)
            counter += 1

        else:
            if c == '(:
                arr.append(c)
                counter += 1
            elif c == ')':
                arr.pop(0)
                counter -= 1
    if counter != 0 or len(arr)>0:
        answer = False

return answer
```
> 이렇게 풀었더니 효율성 테스트에서 모두 떨어졌다. 원인을 찾아보니 `arr.pop(0)` 이 원인이었다.

list.pop(0)는 맨 앞 원소를 제거하면서 모든 원소를 한 칸씩 당기기 때문에 O(n) 이다. 이를 반복하면 전체가 O(n²) 로 커져 효율성 테스트에서 실패하게 된다.
