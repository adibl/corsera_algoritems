def reach(adj, x):
    vertecis_visited[x] = True
    for vertix in adj[x]:
        if not vertecis_visited[vertix]:
            reach(adj, vertix)

if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    vertecis_visited = [False for i in range(int(v) + 1)]
    conn_list = [set() for i in range(int(v) + 1)]

    for i in range(e):
        v1, v2 = [int(x) for x in input().split()]
        conn_list[v1].add(v2)
        conn_list[v2].add(v1)

    conected_components = 0
    for i in range(1, v + 1):
        if not vertecis_visited[i]:
            reach(conn_list, i)
            conected_components += 1
    print(conected_components)