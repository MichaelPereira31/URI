T = int(input())


for cont in range(1,T+1):
    x, y = input().split()
    
    
    if x == "tesoura" and y == "papel":
        print("Caso #%d: Bazinga!"%cont)
    elif x == "papel" and y == "pedra":
        print("Caso #%d: Bazinga!"%cont)
    elif x == "pedra" and y == "lagarto":
        print("Caso #%d: Bazinga!"%cont)
    elif x == "lagarto" and y == "Spock":
        print("Caso #%d: Bazinga!"%cont)
    elif x ==  y:
        print("Caso #%d: De novo!"%cont)
    elif x == "Spock" and y == "tesoura":
        print("Caso #%d: Bazinga!"%cont)
    elif x == "tesoura" and y == "lagarto":
        print("Caso #%d: Bazinga!"%cont)
    elif x == "lagarto" and y == "papel":
        print("Caso #%d: Bazinga!"%cont)
    elif x == "papel" and y == "Spock":
        print("Caso #%d: Bazinga!"%cont)
    elif x == "Spock" and y == "pedra":
        print("Caso #%d: Bazinga!"%cont)
    elif x == "pedra" and y == "tesoura":
        print("Caso #%d: Bazinga!"%cont)
    else:
        print("Caso #%d: Raj trapaceou!"%cont)
