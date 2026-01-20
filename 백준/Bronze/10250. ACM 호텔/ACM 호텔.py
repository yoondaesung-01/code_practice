T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    
    Floor = N % H
    Room = N // H + 1
    
    if Floor == 0:
        Floor = H
        Room -= 1
    print(Floor*100 + Room)