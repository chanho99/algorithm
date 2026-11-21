# Algorithm Study
> 알고리즘 공부
<br>

## 연습
- 푸는 방법을 대충이라도 알 것 같다 ➡ Keep going<br>
- 전혀 감이 안 잡힌다 ➡ 알고리즘 분류 확인<br>
- 출력 초과, 런타임 에러, 시간/메모리 초과 ➡ 예외 케이스 확인, 시간/공간복잡도 확인<br>
- 문제를 풀고 나서 ➡ 어떤 상황에서 어떤 알고리즘/자료구조/테크닉 확인 후 정리<br>
<br><br>

## Python 기초
<br>

## 유형 별 학습

## 🏷️ 태그 별 풀이 전략

### DFS/BFS

| 방식           | 특징                 | 데이터 구조 | 일반 사용 상황                 |
| ------------ | ------------------ | ------ | ------------------------ |
| DFS (재귀)     | 깊이 우선, 간단하지만 재귀 제한 | 재귀 호출  | 트리 탐색, 연결 요소 찾기 등 간단한 경우 |
| DFS (반복문 스택) | 깊이 우선, 깊은 탐색 가능    | 스택     | 깊은 그래프 탐색, 재귀 제한 우회      |
| BFS (반복문 큐)  | 너비 우선, 최단거리 유리     | 큐      | 최단 거리 문제, 단계별 탐색         |

- DFS (Depth-First Search)
  - 재귀 DFS
    ```python
    def dfs(node):
      visited[node] = True
    
      for next_node in graph[node]:
        if not visited(next_node]:
          dfs(next_node, visited)
    
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
    ```

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
    ```
