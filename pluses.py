import numpy as np

t=input().split()

a=list()

for u in range(1,len(t)):
    a.append([int(i, base=16) for i in t[u]])

a=np.array(a)


"""
Find and count pluses from given input
a = [[0, 0, 0, 1, 0, 0, 0, 0], 
     [0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0], 
     [1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 1, 0, 0, 0, 0], 
     [0, 0, 0, 1, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 1, 1], 
     [0, 0, 0, 1, 0, 0, 1, 0]]
"""


n=len(a)

sol=0


for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            for k in range(1,int(n/2)):
                if i-k < 0 or i+k >= n or j-k < 0 or j+k >= n:
                    break
                if a[i][j-k] == 0 or a[i][j+k] == 0 or a[i-k][j] == 0 or a[i+k][j] == 0:
                    break
                ok=1
                x=0
                while ok and x<2*k+1:
                    if x != k:
                        if a[i-k][j-k+x] == 1 or a[i+k][j-k+x] == 1:
                            ok = 0;
                    x+=1
                y=0
                while ok and y < 2*k+1:
                    if y != k:
                        if a[i-k+y][j-k] == 1 or a[i-k+y][j+k] == 1:
                            ok = 0;
                    y+=1
                if ok == 0:
                    break
                sol+=1
print(sol)
