import unittest
from collections import deque


# dqueue provide an O(1) time complexity for append and pop as compare to list which provide O(n) time complexity

def is_route_bfs(graph, start, end):
    # Time complexcity: O(k^d)            
    # With: 
    if start == end:
        return True

    q = deque()
    visited = set()

    q.append(start)

    while q:
        node = q.popleft()
        for adjacent in graph[node]:
            if adjacent not in visited:
                if adjacent == end:
                    return True
                else:
                    q.append(adjacent)
        visited.add(adjacent)
    return False                    


def is_route_dfs(graph, start, end):
    visited = set()
    return is_route_dfs_helper(graph, start, end, visited)


def is_route_dfs_helper(graph, start, end, visited):
    if start == end:
        return True

    visited.add(start)
    rs = False
    for node in graph[start]:
        if node not in visited:
            if is_route_dfs_helper(graph, node, end, visited):
                return True
    return False

class Test(unittest.TestCase):
    graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["A", "E"],
            "D": ["B", "C"],
            "E": ["C", "F"],
            "F": ["E", "O", "I", "G"],
            "G": ["F", "H"],
            "H": ["G"],
            "I": ["F", "J"],
            "O": ["F"],
            "J": ["K", "L", "I"],
            "K": ["J"],
            "L": ["J"],
            "P": ["Q", "R"],
            "Q": ["P", "R"],
            "R": ["P", "Q"]
           }


    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]

    def test_is_route_bfs(self):
        for [start, end, expect] in self.tests:
            actual = is_route_bfs(self.graph, start, end)
            assert expect == actual

    def test_is_route_dfs(self):
        for [start, end, expect] in self.tests:
            actual = is_route_dfs(self.graph, start, end)
            #print(f"start={start}, end={end}, expect={expect}, actual={actual}")
            assert expect == actual
 
if __name__ == "__main__":
   unittest.main()
