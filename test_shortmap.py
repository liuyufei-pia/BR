import time
n = 5
map = [[0] * n for i in range(n)]
inf  = float("inf")
flag = [[False] * n]
dist = [[0] * n]
p = [[0] * n]
print(map)
print('11111111111111')
print(dist)



def Dijkstra(u, n):
    for i in range(1, n):
        dist[i] = map[u][i]
        flag[i] = False
        if dist[i] is not inf:
            p[i] = -1
        else:
            p[i] = u
    dist[u] = 0
    flag[u] = True
    for i in range(1, n):
        temp = inf
        t = u
        for j in range(1, n):
            if flag[j] is False & dist[j] < temp:
                t = j
                temp = dist[j]
            if t == u:
                return
            flag[t] = True
            for j in range(1, n):
                if flag[j] is False & map[t][j] < inf:
                    if dist[j] > (dist[t] + int(map[t][j])):
                        dist[j] = dist[t] + int(map[t][j])
                        p[j] = t


n = int(input('请输入城市的个数：'))
m = int(input('请输入城市之间的路线个数：'))
for i in range(1, n):
    for j in range(1, n):
        map[i][j] = inf
while m > 0:
    u = int(input('u='))
    v = int(input('v='))
    w = int(input('w='))
    m = m - 1
    map[u][v] = min(map[u][v], w)
    print(map[u][v])
st = int(input('请输入小明所在的位置：'))
Dijkstra(st, n)
print('小明所在的位置' + str(st))
for i in range(1, n):
    print('小明：' + str(st) + '-要去的位置：' + str(i))
    if dist[i] == inf:
        print('无路可达')
    else:
        print('最短距离为：' + str(dist[i]))
