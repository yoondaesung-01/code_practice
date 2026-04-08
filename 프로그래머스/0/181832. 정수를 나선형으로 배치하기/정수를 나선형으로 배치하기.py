def solution(n):
    answer = [[0] * n for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    row, col = 0, 0
    dist = 0
    
    for i in range(1, n**2 + 1):
        answer[row][col] = i 
        nr = row + dr[dist]
        nc = col + dc[dist]
        if nr < 0 or nr >= n or nc < 0 or nc >= n or answer[nr][nc] != 0:
            dist = (dist + 1) % 4
            nr = row + dr[dist]
            nc = col + dc[dist]
        row, col = nr, nc
        
    return answer