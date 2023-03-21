from collections import deque
import sys
N,M=map(int,sys.stdin.readline().split())
tray=[list(map(int,sys.stdin.readline().strip())) for i in range(N)]
total=0
def dfs(p):
    q=deque()
    if p[1]+1>=0 and p[1]+1<M:
        if tray[p[0]][p[1]+1]==0:
            tray[p[0]][p[1]+1]=1
            q.append([p[0],p[1]+1])
    if p[1]-1>=0 and p[1]-1<M:
        if tray[p[0]][p[1]-1]==0:
            tray[p[0]][p[1]-1]=1
            q.append([p[0],p[1]-1])
    if p[0]+1>=0 and p[0]+1<N:
        if tray[p[0]+1][p[1]]==0:
            tray[p[0]+1][p[1]]=1
            q.append([p[0]+1,p[1]])
    if p[0]-1>=0 and p[0]-1<N:
        if tray[p[0]-1][p[1]]==0:
            tray[p[0]-1][p[1]]=1
            q.append([p[0]-1,p[1]])
    while q:
        n=q.popleft()
        dfs(n)
for i in range(N):
    for j in range(M):
        if tray[i][j]==0:
            dfs([i,j])
            total+=1
print(total)
