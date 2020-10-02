while True:
    try:
        v = int(input())

        m=[]

        for i in range(0,v):
            m.append([])
            
            for j in range(0,v):
                m[i].append('0')
        
        for i in range(v):
            m[i][i] = '2'
            m[i][v - 1 - i] = '3'

        for i in range(v // 3,v - v // 3):
                for j in range(v // 3,v - v // 3):
                    m[i][j] = '1'
        m[v // 2][v // 2] = '4'

        for i in range(v):
            M = ''.join(m[i])
            print(M)
        print()
            
    except EOFError:
        break
