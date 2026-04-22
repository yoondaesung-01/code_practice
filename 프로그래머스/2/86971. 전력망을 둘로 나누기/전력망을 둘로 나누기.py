from collections import deque, defaultdict

def solution(n, wires):
    answer = float('inf') # 최소 차이를 구해야 하므로 초기값은 무한대로 설정
    
    # 1. 양방향 그래프 구축
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    # 2. BFS 탐색 함수 정의
    # start: 탐색을 시작할 노드
    # cut_v1, cut_v2: 이번에 끊어진 것으로 취급할 두 노드
    def bfs(start, cut_v1, cut_v2):
        queue = deque([start])
        visited = [False] * (n + 1)
        visited[start] = True
        
        count = 1 # 현재 전력망에 속한 송전탑의 개수 (시작 노드 포함)
        
        while queue:
            current = queue.popleft()
            
            # 현재 노드와 연결된 다음 노드들을 확인
            for next_node in graph[current]:
                # ✂️ 핵심 로직: 현재 확인하는 간선이 이번에 '끊은' 간선이라면 무시!
                if (current == cut_v1 and next_node == cut_v2) or (current == cut_v2 and next_node == cut_v1):
                    continue
                
                # 방문하지 않은 노드라면 큐에 넣고 개수 증가
                if not visited[next_node]:
                    visited[next_node] = True  # 1. 방문 처리 (다시 방문하는 것 방지)
                    queue.append(next_node)    # 2. 큐에 삽입 (다음 탐색 후보로 등록)
                    count += 1                 # 3. 연결된 송전탑 개수 1 증가
                    
        return count

    # 3. 모든 전선을 하나씩 끊어보며 완전탐색
    for v1, v2 in wires:
        # v1과 v2를 끊었다고 가정하고, v1 쪽 전력망의 개수를 구함
        count_a = bfs(v1, v1, v2) 
        
        # 공식: abs(전체 N - 2 * 한쪽 전력망 개수)
        diff = abs(n - 2 * count_a)
        
        # 최소 차이 갱신
        answer = min(answer, diff)
        
    return answer