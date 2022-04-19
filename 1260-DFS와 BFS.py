import sys

def dfs(n):
  visited[n] = True
  print(n, end=' ')
  for i in graph[n]:
    if not visited[i]:
      dfs(i)

## 정점, 간선, 첫번째 노드
N,M,V=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
  a,b=map(int, sys.stdin.readline().split())
  graph[a].append(b)
for i in range(1, N+1):
  graph[i].sort()

visited = [False] * (N+1)

dfs(V)

print()
visited = [False] * (N+1)