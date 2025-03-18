import heapq

class Puzzle:
    def __init__(self, board, goal):
        self.board = board  # Current state of the board
        self.goal = goal    # Goal state
        self.goal_positions = {self.goal[i][j]: (i, j) for i in range(3) for j in range(3)}

    def heuristic(self, state):
        """Manhattan Distance Heuristic"""
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = state[i][j]
                if tile != 0:  # Ignore the empty tile (0)
                    goal_x, goal_y = self.goal_positions[tile]
                    distance += abs(goal_x - i) + abs(goal_y - j)
        return distance

    def get_neighbors(self, state):
        """Generate possible moves (Up, Down, Left, Right)"""
        neighbors = []
        x, y = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(new_state)
        return neighbors

    def solve(self):
        """A* Algorithm"""
        priority_queue = []
        heapq.heappush(priority_queue, (0, self.board, []))  # (f(n), state, path)
        visited = set()

        while priority_queue:
            f, current, path = heapq.heappop(priority_queue)
            if current == self.goal:
                return path + [current]  # Return the path to the solution

            visited.add(tuple(map(tuple, current)))
            for neighbor in self.get_neighbors(current):
                if tuple(map(tuple, neighbor)) not in visited:
                    g = len(path) + 1
                    h = self.heuristic(neighbor)
                    f = g + h
                    heapq.heappush(priority_queue, (f, neighbor, path + [current]))

        return None  # No solution found

# Example Usage
initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]  # 0 represents the empty tile
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state

puzzle = Puzzle(initial_state, goal_state)
solution = puzzle.solve()

if solution:
    print("Solution found:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
