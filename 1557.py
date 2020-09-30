N =1

while N >=1:
    N = int(input())

    if N > 0:
        matriz = []

        for i in range(N):
            matriz.append([])
            for j in range(N):
                matriz[i].append(0)


        matriz[0][0] = 1
        for i in range(0,N):
            if i >=1:
                matriz[i][0] = matriz[i - 1][0] * 2
            
            for j in range(1, N):
                matriz[i][j] = matriz[i][j-1] * 2

        T = len(str(matriz[N-1][N-1]))
        for i in range(N):
            for j in range(N):
                matriz[i][j] = str(matriz[i][j])
                while len(matriz[i][j]) < T:
                    matriz[i][j] = ' ' + matriz[i][j]
            R = ' '.join(matriz[i])
        
            print(R)
        print()
