# Algorithm Study
> 알고리즘 공부
<br>

## 연습
- 푸는 방법을 대충이라도 알 것 같다 ➡ Keep going<br>
- 전혀 감이 안 잡힌다 ➡ 알고리즘 분류 확인<br>
- 출력 초과, 런타임 에러, 시간/메모리 초과 ➡ 예외 케이스 확인, 시간/공간복잡도 확인<br>
- 문제를 풀고 나서 ➡ 어떤 상황에서 어떤 알고리즘/자료구조/테크닉 확인 후 정리<br>
<br><br>

## 🛠 python 정리
| 자료형     | 순서       | 중복     | 변경 가능 | 예시 사용              |
| ------- | -------- | ------ | ----- | ------------------ |
| 리스트 \[] | O        | O      | O     | 입력, 정렬, 순회         |
| 튜플 ()   | O        | O      | X     | 좌표, 회의 시작/끝, 함수 반환 |
| 세트 {}   | X        | X      | O     | 중복 제거, 집합 연산       |
| 딕셔너리 {} | O (3.7+) | 키 중복 X | O     | 빈도 계산, 매핑          |

- 리스트 ➡ 순서 있고 바뀔 수 있는 묶음
- 튜플 ➡ 순서 있고 바뀔 수 없는 묶음
- 세트 ➡ 순서 없고 중복 없는 묶음
- 딕셔너리 ➡ key:value 쌍으로 묶음
<br><br><br>

### 1️⃣ 리스트 `[]`
- 정의: 순서가 있는 <b>변경 가능한(mutable)</b> 자료구조
- 특징:
  - 값의 중복허용
  - 값 추가/삭제/수정 가능
  - 인덱스로 접근 가능
- 예시:
  ```python
  numbers = [1, 2, 3, 4]
  numbers.append(5)  # [1, 2, 3, 4, 5]
  numbers[0] = 10  #[10, 2, 3, 4, 5]
  ```
- 코테: 입력 저장, 순회, 정렬
<br>

### 2️⃣ 튜플 `()`
- 정의: 순서가 있는 <b>변경 불가능(Immutable)</b> 자료구조
- 특징:
  - 값 추가/삭제/수정 불가능
  - 리스트보다 메모리 효율이 좋음
  - 딕셔너리의 key나 set의 요소로 사용 가능
- 예시:
  ```python
  point = (2, 3)
  # point[0] = 5 ➡ 에러 발생
  x, y = point  # 튜플 언패킹 가능
  ```
- 코테: 값 묶어서 전달
<br>

### 3️⃣ 세트 `{}`
- 정의: 순서 없는 <b>중복 없는 집합 자료형</b>
- 특징:
  - 값의 중복 자동 제거
  - 순서 없어서 인덱스로 접근 불가
  - 교집합, 합집합, 차집합 연산 가능
- 예시:
  ```python
  s = {1, 2, 3, 4}  # {1, 2, 3}
  s.add(4)  #{1, 2, 3, 4}
  s.remove(2)  @{1, 3, 4}
  ```
- 코테: 중복 제거, 집합 연산
<br>
  
### 4️⃣ 딕셔너리 `{key: value}`
- 정의: 키와 값이 쌍으로 저장되는 <b>매핑 자료형</b>
- 특징:
  - 키(key)는 중복 불가
  - 값(value)은 중복 허용
  - 순서 있음 (Python 3.7+)
- 예시:
  ```python
  person = {'name': 'Alice', 'age': 25}
  print(person['name'])  # Alice
  person['age'] = 26
  ```
- 코테: 빈도 계산, 매핑 문제
<br><br><br>

### ✅ 입/출력이 많을 때
```python
import sys

# 입력
input = sys.stdin.readline

# 출력
sys.stdout.write("\n".join(result) + "\n")
```
<br>

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
