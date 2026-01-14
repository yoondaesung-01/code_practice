# [LeetCode] 1148. Article Views I

## 1. 문제
  Write a solution to find all the authors that viewed at least one of their own articles.
  Return the result table sorted by id in ascending order.
  
- **목표:** 자신의 기사를 스스로 조회한(viewed) 저자(author)의 ID를 모두 찾아야 한다.
- **조건:**
    1. `author_id`와 `viewer_id` 값이 같은 행을 찾는다.
    2. 결과는 오름차순으로 정렬해야 한다.
    3. 결과에 중복된 값이 있으면 안 된다.

## 2. 💡 풀이 접근
- 테이블에 중복된 행이 있으므로 `DISTINCT` 사용이 필요하다.
- 저자와 시청자가 같아야 하므로 `WHERE author_id = viewer_id` 조건을 사용해야 한다.
- 결과 컬럼명을 `id`로 표시해야하므로 `as id`를 사용해야 한다.

## 3. 📝 정답 코드 (PostgreSQL)
```PostgreSQL
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC; 
```

## 4. 📝 내가 적은 코드 (PostgreSQL) 
```PostgreSQL
SELECT DISTINCT author_id as id
FROM Views
Where author_id = viewer_id
ORDER BY author_id ASC;
```
### ✅ 체크 포인트
1. SELECT절에서 'id'라는 별칭을 지정해서 
2. 처음에는 DISTINCT를 사용하지 않음. 조건을 만족하는 데이터가 중복이 될 수 있음을 항상 고려해야 한다.
