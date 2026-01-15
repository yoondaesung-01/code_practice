# [LeetCode] 197. Rising Temperature

## 1. ❓ 문제 정의
- **목표:** 어제보다 기온이 높았던 날의 `id`를 모두 찾아야 한다.
- **조건:**
    1. 테이블은 하나(`Weather`)지만, 서로 다른 날짜의 데이터를 비교해야 한다.
    2. 날짜(`recordDate`)가 하루 차이가 나는 행을 찾아 비교해야 한다.

## 2. 💡 풀이 접근
- **셀프 조인 (Self Join):**
  - 같은 테이블의 행끼리 비교하려면, 테이블을 두 개(`w1`, `w2`)인 것처럼 별칭을 붙여서 조인해야 한다.
  - `w1`: 기준이 되는 날 (오늘)
  - `w2`: 비교 대상이 되는 날 (어제)
- **날짜 계산:**
  - 단순히 `id - 1`을 하면 안 된다. (날짜가 1월 1일 다음에 1월 5일이 올 수도 있기 때문)
  - 반드시 **날짜 컬럼(`recordDate`)을 기준**으로 계산해야 한다.

## 3. 📝 정답 코드 (PostgreSQL)
```PostgreSQL
SELECT w1.id
FROM Weather w1
JOIN Weather w2 
    ON w1.recordDate - w2.recordDate = 1  
WHERE w1.temperature > w2.temperature;    
```

### ✅체크포인트
- Self Join (셀프 조인)
하나의 테이블 안에서 서로 다른 행을 비교할 때 사용한다.
FROM Table A, Table B 처럼 같은 테이블을 다른 별칭으로 두 번 부르면 된다.

- 날짜 연산 (PostgreSQL)
PostgreSQL에서는 날짜형(Date)끼리 뺄셈을 하면 **일(Day) 수 차이(정수)**가 반환된다.

MySQL에서는 DATEDIFF(w1.recordDate, w2.recordDate) = 1 함수를 사용해야 하지만, PostgreSQL는 직관적인 뺄셈이 가능하다.
