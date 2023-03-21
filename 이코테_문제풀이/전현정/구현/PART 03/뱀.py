import sys
from collections import deque
from pprint import pprint
N=int(sys.stdin.readline())
board=[[0]*N for i in range(N)]
poslist=[[0,1],[1,0],[0,-1],[-1,0]]
pos=0

for i in range(int(sys.stdin.readline())):
    applex,appley=map(int,sys.stdin.readline().split())
    board[applex-1][appley-1]='a'
board[0][0]=1#시작점 표시
cnt=0
x=0
y=0
flag=0
que=deque()
que.append([x,y])

for i in range(int(sys.stdin.readline())):
    cmd=list(sys.stdin.readline().split())
    cmd[0]=int(cmd[0])
    
    for j in range(cmd[0]-cnt):
        cnt+=1
        #머리이동,이동한 부분이 몸인지 벽인지 확인
        x+=poslist[pos][0]
        y+=poslist[pos][1]
        if x>=N or y>=N or x<0 or y<0:
            flag=1
            break
        elif board[x][y]==1:
            flag=1
            break
        elif board[x][y]=='a':
            que.append([x,y])
            board[x][y]=1
        else:
            que.append([x,y])
            temp=que.popleft()
            board[x][y]=1
            board[temp[0]][temp[1]]=0
    if flag==1:
        break

    #방향설정
    if cmd[1]=='L':
        pos-=1
        pos%=4
    else:
        pos+=1
        pos%=4
if flag==0:
    while True:
        cnt+=1
        #머리이동,이동한 부분이 몸인지 벽인지 확인
        x+=poslist[pos][0]
        y+=poslist[pos][1]
        if x>=N or y>=N or x<0 or y<0:
            flag=1
            break
        elif board[x][y]==1:
            flag=1
            break
        elif board[x][y]=='a':
            que.append([x,y])
            board[x][y]=1
        else:
            que.append([x,y])
            temp=que.popleft()
            board[x][y]=1
            board[temp[0]][temp[1]]=0
    print(cnt)
else:
    print(cnt)
