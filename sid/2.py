from collections import deque

def create_graph():
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }
    return graph

def bfs_recursive(graph, queue, visited):
    
    if not queue:
        return
    
    
    vertex = queue.popleft()
    print(vertex, end=' ')
    
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    
   
    bfs_recursive(graph, queue, visited)

def bfs(graph, start_vertex):
   
    queue = deque()
    
    
    visited = set([start_vertex])
    queue.append(start_vertex)
    
    
    bfs_recursive(graph, queue, visited)


if __name__ == "__main__":
   
    graph = create_graph()

    print("BFS traversal starting from vertex A:")
    bfs(graph, 'A')