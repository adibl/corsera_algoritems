#Uses python3
import sys
sys.setrecursionlimit(10**4)

def reach(adj, current, post_order, vertecis_visited):
    vertecis_visited[current] = True
    for vertix in adj[current]:
        if not vertecis_visited[vertix]:
            reach(adj, vertix, post_order, vertecis_visited)
    post_order.append(current)

def reach_cycle(adj, current, vertecis_visited):
    vertecis_visited[current] = True
    for vertix in adj[current]:
        if not vertecis_visited[vertix]:
            reach_cycle(adj, vertix, vertecis_visited)

def reverse_edges(conn_list):
    conn_list_reversed = [set() for _ in range(len(conn_list) + 1)]
    for index, connections in enumerate(conn_list):
        for con in connections:
            conn_list_reversed[con].add(index)
    return conn_list_reversed


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    vertecis_visited = [False for _ in range(int(v) + 1)]
    conn_list_reverse = [set() for _ in range(int(v) + 1)]

    post_order = list()
    for i in range(e):
        v1, v2 = [int(x) for x in input().split()]
        conn_list_reverse[v2].add(v1)
    for i in range(1, len(vertecis_visited)):
        if not vertecis_visited[i]:
            reach(conn_list_reverse, i, post_order, vertecis_visited)
    conn_list = reverse_edges(conn_list_reverse)
    vertecis_visited = [False for _ in range(int(v) + 1)]
    conected_components_counter = 0
    for vertix in reversed(post_order):
        if not vertecis_visited[vertix]:
            reach_cycle(conn_list, vertix, vertecis_visited)
            conected_components_counter += 1
    print(conected_components_counter)



