from itertools import combinations
import heapq

left = {'A', 'B', 'C', 'D'}
right = set()
torch = 'left'

time = {
    'A': 1,
    'B': 2,
    'C': 5,
    'D': 10
}

def crossing_time(a, b):
    return max(time[a], time[b])

def heuristic(left):
    if not left:
        return 0
    return max(time[p] for p in left)

def astar():
    start_left = frozenset(['A', 'B', 'C', 'D'])

    # (f, g, left, torch)
    queue = [(heuristic(start_left), 0, start_left, 'left', [])] 

    visited = set()

    while queue:
        f, g, left, torch, path = heapq.heappop(queue)

        if not left: 
            return g, path

        state = (left, torch) 

        if state in visited: 
            continue

        visited.add(state) 

        right = set(time.keys()) - set(left)

        if torch == 'left':
            for a, b in combinations(sorted(left), 2):
                new_left = set(left) 
                new_left.remove(a)
                new_left.remove(b)

                new_left = frozenset(new_left) 

                new_g = g + max(time[a], time[b]) 
                new_h = heuristic(new_left) 
                new_f = new_g + new_h 

                new_path = path + [ f"{a} + {b} cross right"]

                heapq.heappush(
                    queue,
                    (new_f, new_g, new_left, 'right', new_path)
                )

        else:
            for a in sorted(right): 
                new_left = set(left)
                new_left.add(a)

                new_left = frozenset(new_left)

                new_g = g + time[a]
                new_h = heuristic(new_left)
                new_f = new_g + new_h
                new_path = path + [
                    f"{a} returns left"
                ]

                heapq.heappush(
                    queue,
                    (new_f, new_g, new_left, 'left', new_path)
                )

    return None, []


result, path = astar()

print("Optimal solution:")

for step in path:
    print(step)

print("Minimum time:", result, "minutes")