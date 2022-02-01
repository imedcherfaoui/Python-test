def polynomiale(x):
    return(x**3-(x**2)*1.5-6*x+5)
polynomiale(5)

def factorielle(n):
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return n*factorielle(n)
print(factorielle(5))

def fibonnaci(n = int(input("Entrer un nombre : "))):
  a = 0
  b = 1
  print("La suite de fibonnaci est :")
  if n == 0:
    return a
  elif n == 1:
    return b
  else:
    print(a, " , ")
    print(b, " , ")
    for i in range(n-2):
      c = a + b
      print(c, " , ")
      a = b
      b = c

fibonnaci()