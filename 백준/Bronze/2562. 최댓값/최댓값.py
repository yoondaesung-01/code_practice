max = 0
n = 0
for i in range(9):
    X = int(input())
    if max < X:
        max = X
        n = i+1
print(max)
print(n)