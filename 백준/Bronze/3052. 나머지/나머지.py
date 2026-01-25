List = []

for _ in range(10):
    n = int(input())
    val = n % 42
    if val not in List:
        List.append(val)
        
print(len(List))