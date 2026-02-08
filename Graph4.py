# A 3x3 grid where each node connects to its neighbors
grid_graph = {
    (0,0): [(0,1), (1,0)],
    (0,1): [(0,0), (0,2), (1,1)],
    (0,2): [(0,1), (1,2)],
    (1,0): [(0,0), (1,1), (2,0)],
    (1,1): [(0,1), (1,0), (1,2), (2,1)],
    (1,2): [(0,2), (1,1), (2,2)],
    (2,0): [(1,0), (2,1)],
    (2,1): [(2,0), (1,1), (2,2)],
    (2,2): [(1,2), (2,1)]
}

def DFS(grid_graph,node,visited):
  if node not in visited:
    visited.add(node)
    print(node)
    for n in grid_graph[node]:
      DFS(grid_graph,n,visited)
visited=set()
DFS(grid_graph,(0,0),visited)
