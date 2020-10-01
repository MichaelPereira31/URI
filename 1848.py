n = 0
valor = 0
while n<3:
    entrada =  input()
    if(entrada == 'caw caw'):
        print(valor)
        valor = 0
        n += 1
    for i in range(3):
        if (entrada[i] == '*' or entrada[i] == '-'):
            if(entrada[i] == '*'):
                if( i == 2):
                    valor += 1
                elif( i == 0):
                    valor += 4