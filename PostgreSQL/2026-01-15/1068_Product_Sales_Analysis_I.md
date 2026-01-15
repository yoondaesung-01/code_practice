# [LeetCode] 1068. Product Sales Analysis I

## 1. ❓ 문제 정의
Write a solution to report the , , and for each in the table.product_nameyearpricesale_idSales
Return the resulting table in any order.

- **목표:** `Sales` 테이블에 있는 각 판매 기록에 대해, 해당 제품의 이름(`product_name`)과 판매 연도(`year`), 가격(`price`)을 출력해야 한다.
- **조건:**
    1. `Sales` 테이블에는 제품 이름이 없고 `product_id`만 있다.
    2. `Product` 테이블에는 `product_id`와 `product_name`이 있다.
    3. 두 테이블을 연결해서 정보를 합쳐야 한다.

## 2. 💡 풀이 접근
- 필요한 데이터가 두 테이블(`Sales`, `Product`)에 나뉘어 있으므로 **`JOIN`**을 사용해야 한다.
- 두 테이블을 연결하는 **연결고리(Key)**는 **`product_id`**이다.
- `Sales` 테이블에 존재하는 판매 기록에 대한 정보를 가져오는 것이므로, 일반적인 `JOIN` (Inner Join)을 사용하면 된다.

## 3. 📝 정답 코드 (PostgreSQL)
```PostgreSQL
SELECT product_name, year, price
FROM Product 
JOIN Sales ON Product.product_id = Sales.product_id;
```
### ✅ 체크 포인트
- JOIN:
별도의 수식어 없이 JOIN만 쓰면 기본적으로 **INNER JOIN(교집합)**이 된다.
Sales 테이블의 product_id는 Product 테이블을 참조하는 외래키(Foreign Key)이므로, 두 테이블에 모두 존재하는 데이터가 매칭되어 출력된다.

- 테이블 별칭(Alias) 활용 (꿀팁):
코드가 길어질 때는 아래처럼 별칭을 쓰면 더 간결하게 작성할 수 있다.
```PostgreSQL
SELECT p.product_name, s.year, s.price
FROM Product p
JOIN Sales s ON p.product_id = s.product_id;
```
