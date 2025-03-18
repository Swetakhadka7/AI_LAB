from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list representation

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def bfs(self, start, goal):
        queue = deque([[start]])  # Queue stores paths
        visited = set()

        while queue:
            path = queue.popleft()  # Get the first path from the queue
            node = path[-1]  # Last node in the path

            if node == goal:
                return path  # Return the shortest path found

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    new_path = path + [neighbor]  # Create a new path
                    queue.append(new_path)  # Add new path to the queue

        return None  # No path found

# Example Usage
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')
g.add_edge('F', 'G')

start, goal = 'A', 'G'
path = g.bfs(start, goal)
if path:
    print("Shortest path:", path)
else:
    print("No path exists")
