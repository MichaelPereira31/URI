while True:
    try:
        def matriz_A(n,m):
            for i in range(n // 3,n - n // 3):
                for j in range(n // 3,n - n // 3):
                    m[i][j] = '1'
            return m

        def matriz_B(n,m):
            m[n // 2][n // 2] = '4'
            return m

        v = int(input())

        m=[]

        for i in range(0,v):
            m.append([])
            
            for j in range(0,v):
                m[i].append('0')

        c = v - 1
          
        

        matriz_A(v,m)
        matriz_A(v,m)
        for i in range(v):
            m[i][i] = '2'
        for i in range(v):
            m[i][v - 1 - i] = '3'
        for i in range(v):
            M = ''.join(m[i])
            print(M)
        '''
        for i in range(0,v):
            m[i][i] = '2'
            m[i][c] = '3'
            c -= 1'''
            
    except EOFError:
        break


