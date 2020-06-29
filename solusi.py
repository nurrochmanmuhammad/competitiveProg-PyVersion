def main():
    x=input().split()
    a=list()
    for u in range(1,len(x)):
        a.append([int(v, base=16) for v in x[u]])
    n=int(x[0])
    if n<2000:
        solution=0
        for i in range(n):
            for j in range(n):
                if a[i][j]==1:
                    for k in range(1,int(n/2)+1):
                        if i-k < 0 or i+k >= n or j-k < 0 or j+k >= n:
                            break
                        if a[i][j-k] == 0 or a[i][j+k] == 0 or a[i-k][j] == 0 or a[i+k][j] == 0:
                            break
                        cek=1
                        x=0
                        while cek and x<2*k+1:
                            if x != k:
                                if a[i-k][j-k+x] == 1 or a[i+k][j-k+x] == 1:
                                    cek = 0;
                            x+=1
                        y=0
                        while cek and y < 2*k+1:
                            if y != k:
                                if a[i-k+y][j-k] == 1 or a[i-k+y][j+k] == 1:
                                    cek = 0;
                            y+=1
                        if cek == 0:
                            break
                        solution+=1
        print(solution)
        
    else:
        print('n more than 2000')

if __name__ == "__main__":
    main()