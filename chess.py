n = int(input())
start1 = input().split()
start2 = input().split()
x1 = start1[0][0]
y1 = int(start1[0][1])
x2 = start2[1][0]
y2 = int(start2[1][1])

desk = [[-1 for j in range(8)] for i in range(8)]
desk[x1][y1] = 0
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

queue_x = []
queue_y = []

queue_x1 = []
queue_y1 = []
queue_x1.append(x1)
queue_y1.append(y1)

queue_x2.append(x2)
queue_y2.append(y2)

while queue_x1:
    x = queue_x1.pop(0)
    y = queue_y1.pop(0)
    for i in range(len(dx)):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
            if desk[x + dx[i]][y + dy[i]] == -1:
                desk[x + dx[i]][y + dy[i]] = desk[x][y] + 1
                queue_x.append(x + dx[i])
                queue_y.append(y + dy[i])
            else:
                if desk[x + dx[i]][y + dy[i]] > desk[x][y] + 1:
                    desk[x + dx[i]][y + dy[i]] = desk[x][y] + 1
                    queue_x.append(x + dx[i])
                    queue_y.append(y + dy[i])

print(desk[x2][y2]) = int(input())
start = input().split()
finish = input().split()
x1 = int(start[0]) - 1
y1 = int(start[1]) - 1
x2 = int(finish[0]) - 1
y2 = int(finish[1]) - 1


desk = [[-1 for j in range(n)] for i in range(n)]
desk[x1][y1] = 0
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


queue_x = []
queue_y = []

queue_x.append(x1)
queue_y.append(y1)


while queue_x:
    x = queue_x.pop(0)
    y = queue_y.pop(0)
    for i in range(len(dx)):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
            if desk[x + dx[i]][y + dy[i]] == -1:
                desk[x + dx[i]][y + dy[i]] = desk[x][y] + 1
                queue_x.append(x + dx[i])
                queue_y.append(y + dy[i])
            else:
                if desk[x + dx[i]][y + dy[i]] > desk[x][y] + 1:
                    desk[x + dx[i]][y + dy[i]] = desk[x][y] + 1
                    queue_x.append(x + dx[i])
                    queue_y.append(y + dy[i])


print(desk[x2][y2])


