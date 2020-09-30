while True:
    try:
        n = int(input())
        x = input().split()
        j = 0
        for i in range(n):
            if int(x[i]) > j:
                j = int(x[i])

        if j < 10:
            k = 1
        elif j >= 10 and j < 20:
            k = 2
        else:
            k = 3
        print(k)


    except EOFError:
        break
