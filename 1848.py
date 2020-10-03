valor = 0
c = 0
while(c<3):
  n = input()
  if(n != 'caw caw'):
      
    if(n[0] == '*'):
      valor += 4
    if(n[1] == '*'):
      valor += 2
    if(n[2] == '*'):
      valor += 1
  else:
      print(valor)
      valor = 0
      c += 1
    
