print("Enter the number of queen")
N=int(input())
board=[[0]*N for _ in range(N)]

def attack(i,j):
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(0,N):
        for l in range(0,N):
             if(k+l==i+j) or (k-l==i-j):
                     if board[k][l]==1:
                             return True
                        
    return False

def N_q(n):
    if n==0:
        return True
        
    for i in range(0,N):
        for j in range(0,N):
            if(not(attack(i,j))) and (board[i][j]!=1):
                return True
            board[i][j]=0
    return False
N_q(N)
for i in board:
    print(i)