#Uses python3


def reach(adj, current):
    vertecis_visited[current] = True
    sink = True
    for vertix in adj[current]:
        if vertecis_visited[vertix] or removed_vertecis[vertix]:
            pass
        else:
            reach(adj, vertix)
            if not removed_vertecis[vertix]:
                sink = False
    if sink:
        removed_vertecis[current] = True
        vertix_order.append(current)


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    vertecis_visited = [False for i in range(int(v) + 1)]
    removed_vertecis = [False for i in range(int(v) + 1)]
    vertix_order = []
    conn_list_reverse = [set() for i in range(int(v) + 1)]
    for i in range(e):
        v1, v2 = [int(x) for x in input().split()]
        conn_list_reverse[v2].add(v1)
    for i in range(1, len(vertecis_visited)):
        if not vertecis_visited[i]:
            reach(conn_list_reverse, i)
    print(" ".join([str(x) for x in vertix_order]))

