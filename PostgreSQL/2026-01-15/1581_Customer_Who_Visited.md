# [LeetCode] 1581. Customer Who Visited but Did Not Make Any Transactions

## 1. ❓ 문제 정의
Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.
Return the result table sorted in any order.

- **목표:** 쇼핑몰에 방문(`Visits`)은 했으나, 물건을 구매하지 않은(`Transactions`에 없음) 고객의 ID와 그 빈도수를 구해야 한다.
- **조건:**
    1. 방문 기록은 있지만, 해당 방문 ID가 거래 테이블에는 존재하지 않아야 한다.
    2. 결과 컬럼명은 `count_no_trans`로 지정한다.
    3. 고객별(`customer_id`)로 묶어서 횟수를 세야 한다.

## 2. 💡 풀이 접근
- **차집합(Difference) 구하기:**
  - 우리가 찾는 것은 "방문한 사람(A)" 중에서 "구매한 사람(B)"을 뺀 **(A - B)** 그룹이다.
  - 교집합만 찾는 `INNER JOIN`으로는 이 데이터를 구할 수 없다.
- **LEFT JOIN + IS NULL 패턴:**
  - `Visits` 테이블을 기준으로 `LEFT JOIN`을 수행하여 모든 방문 기록을 살린다.
  - 매칭되는 거래 내역이 없는 경우 `transaction_id`가 `NULL`이 된다.
  - `WHERE ... IS NULL` 조건을 통해 구매하지 않은 방문만 걸러낸다.

## 3. 📝 정답 코드 (PostgreSQL)
```PostgreSQL
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
```
### ✅ 체크포인트
- LEFT JOIN vs INNER JOIN

INNER JOIN: 두 테이블에 모두 존재하는 데이터(구매한 사람)만 남기 때문에, 구매 안 한 사람을 찾을 수 없다.

LEFT JOIN: 왼쪽 테이블(방문) 데이터를 모두 보존하므로, 오른쪽(거래) 정보가 없는 데이터를 NULL 상태로 확인할 수 있다.

- SQL 차집합 공식
"~하지 않은(Not Exists)" 데이터를 찾을 때는 아래 공식을 기억하자.

```PostgreSQL
SELECT ...
FROM 기준테이블
LEFT JOIN 대상테이블 ON 조건
WHERE 대상테이블.PK IS NULL;
```
- GROUP BY와 집계함수:
COUNT 같은 집계 함수를 쓸 때, 집계되지 않는 컬럼(customer_id)은 반드시 GROUP BY에 적어줘야 한다.
