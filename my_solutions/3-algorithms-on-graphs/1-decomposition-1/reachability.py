#Uses python3

def reach(adj, x, y):
    if adj[x].__contains__(y):
        return 1
    else:
        vertecis_visited[x] = True
        for vertix in adj[x]:
            if not vertecis_visited[vertix]:
                if reach(adj, vertix, y) == 1:
                    return 1
    return 0


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    vertecis_visited = [False for i in range(int(v) + 1)]
    conn_list = [set() for i in range(int(v) + 1)]
    for i in range(e):
        v1, v2 = [int(x) for x in input().split()]
        conn_list[v1].add(v2)
        conn_list[v2].add(v1)

    start, destination = [int(x) for x in input().split()]
    print(reach(conn_list, start, destination))

