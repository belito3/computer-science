from typing import List, Tuple


def build_order(pro: List[str], dep: List[Tuple]) -> List[str]:
    graph = build_graph(dep)

    order = []

    while len(order) < len(pro):
        # find node without incomming edge
        childrens = find_childrens(graph, set(order))
        nodes = find_node_without_incomming_edage(pro, childrens, set(order))
        if len(nodes) == 0:
            # detect cycles
            return None
        order.extend(nodes) 
    return order
        


def find_childrens(graph: dict, order: set()) -> set():
    s = set()
    for node in graph:
        if node not in order:
            for n in graph[node]:
                s.add(n)
    return s

def find_node_without_incomming_edage(pro, childrens, order):
    rs = []
    for n in pro:
        if (n not in childrens) and (n not in order):
            rs.append(n)
    return rs


def build_graph(dep: List[Tuple]) -> dict:
    graph = dict()
    for p in dep:
        if p[0] not in graph:
            graph[p[0]] = [p[1]]
        else:
            graph[p[0]].append(p[1])
    return graph



if __name__ == "__main__":
    projects = [["a", "b", "c", "d", "e", "f", "g"], 
            ["a", "b", "c", "d", "e", "f"], 
            ["a", "b", "c"]]
    dependencies = [[("f", "c"), ("f", "a"), ("f", "b"), ("c", "a"), ("b", "a"), ("b", "e"), ("a", "e"), ("d", "g")],
            [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")], 
            []]

    for i in range(len(projects)):
        print(build_graph(dependencies[i]))
        print(build_order(projects[i], dependencies[i]))

    
