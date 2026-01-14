# [LeetCode] 1683. Invalid Tweets

## 1. ❓ 문제 정의
Write a solution to find the IDs of the invalid tweets. 
The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than .15
Return the result table in any order.

- **목표:** 'content'의 길이가 15자를 **넘는** 트윗의 ID를 찾아야 한다.
- **조건:**
  1. 'content' 컬럼의 문자 길이를 잰다.
  2. 길이가 15보다 큰(`> 15`) 행만 필터링하여 출력한다.
  3. 순서는 상관없다고 명시되었다.

## 2. 💡 풀이 접근
- 문자열의 '내용'이 아닌 **'길이'**를 비교해야 하므로 문자열 길이 함수가 필요하다.
- PostgreSQL(및 표준 SQL)에서 문자열 길이를 구하는 함수인 **'LENGTH()'**를 사용하여 조건절을 작성한다.

## 3. 📝 정답 코드 (PostgreSQL)
```PostgreSQL
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
```

### ✅ 체크 포인트
- 문자열 길이 함수: LENGTH(컬럼명)을 사용하여 문자열의 길이를 숫자로 반환받을 수 있다.
