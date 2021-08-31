#Uses python3


def reach(adj, current):
    vertecis_visited[current] = True
    sink = True
    for vertix in adj[current]:
        if removed_vertecis[vertix]:
            pass
        elif vertecis_visited[vertix]:
            return 1
        else:
            if reach(adj, vertix) == 1:
                return 1
            if not removed_vertecis[vertix]:
                sink = False
    if sink:
        removed_vertecis[current] = True
    return 0


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    vertecis_visited = [False for i in range(int(v) + 1)]
    removed_vertecis = [False for i in range(int(v) + 1)]
    conn_list = [set() for i in range(int(v) + 1)]
    for i in range(e):
        v1, v2 = [int(x) for x in input().split()]
        conn_list[v1].add(v2)
    print(reach(conn_list, 1))

