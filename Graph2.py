# One central node with many spokes
star_graph = {
    'Hub': ['Node1', 'Node2', 'Node3', 'Node4', 'Node5'],
    'Node1': ['Hub'],
    'Node2': ['Hub'],
    'Node3': ['Hub'],
    'Node4': ['Hub'],
    'Node5': ['Hub']
}

def BFS(star_graph,Node):
  visited=[]
  queue=[]
  visited.append(Node)
  queue.append(Node)
  while queue:
    m=queue.pop(0)
    print(m, end= " ")
    for n in star_graph[m]:
      if n not in visited:
        visited.append(n)
        queue.append(n)
BFS(star_graph,"Hub")
