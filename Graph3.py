# A graph with cycles and multiple paths
cyclic_mesh = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'C'],
    'C': ['A', 'B', 'F'],
    'D': ['A', 'G'],
    'E': ['B'],
    'F': ['C'],
    'G': ['D']
}

def BFS(cyclic_mesh, Node):
  visited=[]
  queue=[]
  visited.append(Node)
  queue.append(Node)
  while queue:
    m=queue.pop(0)
    print(m,end= " ")
    for n in cyclic_mesh[m]:
      if n not in visited:
        visited.append(n)
        queue.append(n)
BFS(cyclic_mesh,"A")
