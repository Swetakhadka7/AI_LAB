class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list representation

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def dfs(self, start, goal, path=None, visited=None):
        if path is None:
            path = []
        if visited is None:
            visited = set()

        path.append(start)
        visited.add(start)

        if start == goal:
            return path  # Goal found, return the path

        if start in self.graph:
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    result = self.dfs(neighbor, goal, path[:], visited)  # Recursively explore
                    if result:  # If a valid path is found, return it
                        return result

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
path = g.dfs(start, goal)
if path:
    print("Path found:", path)
else:
    print("No path exists")
