# Algorithm Problem Solving
알고리즘 문제들의 풀이 코드 저장소<br>
백준(Baekjoon)에서 푼 알고리즘 문제를 **BaekjoonHub**를 활용해 자동 커밋
<br><br>

## 문제 풀이 환경
- 플랫폼: 백준 (Baekjoon Online Judge)
- 자동 업로드 도구: BaekjoonHub
- 언어: Python, C
<br><br>

### solved.ac
<a href="https://solved.ac/chanho0526">
  <img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=chanho0526">
</a>
<br><br>

<!-- STATS_START -->

### 📊 난이도 분포

| 항목 | 문제 수 |
|------|---------|
| Bronze V | 15 |
| Bronze IV | 4 |
| Bronze III | 6 |
| Bronze II | 8 |
| Bronze I | 4 |
| Silver V | 9 |
| Silver IV | 7 |
| Silver III | 4 |
| Silver II | 1 |
<br>

### 🏷️ 태그 분포

| 항목 | 문제 수 |
|------|---------|
| implementation | 34 |
| math | 27 |
| arithmetic | 13 |
| string | 12 |
| sorting | 6 |
| dp | 5 |
| bruteforcing | 4 |
| data_structures | 4 |
| geometry | 3 |
| greedy | 2 |

<!-- STATS_END -->
<br>

### 연습 추가 예정
https://www.slideshare.net/slideshow/kucc-2022-4/251739276
<br><br>

## python 정리
<br><br>

## 태그 별 풀이 전략

### DFS/BFS

| 방식           | 특징                 | 데이터 구조 | 일반 사용 상황                 |
| ------------ | ------------------ | ------ | ------------------------ |
| DFS (재귀)     | 깊이 우선, 간단하지만 재귀 제한 | 재귀 호출  | 트리 탐색, 연결 요소 찾기 등 간단한 경우 |
| DFS (반복문 스택) | 깊이 우선, 깊은 탐색 가능    | 스택     | 깊은 그래프 탐색, 재귀 제한 우회      |
| BFS (반복문 큐)  | 너비 우선, 최단거리 유리     | 큐      | 최단 거리 문제, 단계별 탐색         |

- DFS (Depth-First Search)
  - 재귀 DFS
    ```python
    def dfs(x, y):
      visited[x][y] = True

      dx = [-1, 1, 0, 0]
      dy = [0, 0, -1, 1]

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (조건):
          dfs(nx, ny)
    ```
    <br>
    
    ❗ 주의사항<br>
    - python의 기본 재귀 한도는 약 1000회로 제한<br>
    - 재귀 한도를 늘리려면<br><br>
    ```python
    import sys
    sys.setrecursionlimit(10**n)  # 재귀 호출의 깊이를 10^n으로 설정
    ```
    - 너무 큰 값을 설정하면 프로그램이 스택 오버플로우로 인해 비정상 종료될 수 있음<br><br>

  - 반복문 DFS
    ```python
    def dfs_iterative(start):
      stack = [start]
      visited[start] = True

      while stack:
        node = stack.pop()
        for next_node in graph[node]:
          if not visited[next_node]:
            visited[next_node] = True
            stack.append(next_node)

  <br>

- BFS (Breadth-First Search)
  - 반복문 BFS
    ```python
    from collections import deque

    def bfs(start):
      queue = deque([start])
      visited[start] = True

      while queue:
        node = queue.popleft()
        for next_node in graph[node]:
          if not visited[next_node]:
            visited[next_node] = True
            queue.append(next_node)
