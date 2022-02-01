def gestion_except(x=input("Saisir une chaine de caractères : ")):
    
    #Saisie d'un nombre complex 
    comp = 0
    while isinstance(comp, complex) == False:
      try:
        print("Saisir un nombre complex (ex: 5+6j): ")
        comp = complex(input())
        if isinstance(comp, complex) == False:
          raise ValueError("Nombre non complex !")
      except ValueError as erreur:
        print(erreur)

    #Saisie d'un nombre négatif 
    neg = 0
    while neg >= 0:
      try:
        print("Saisir un nombre négatif : ")
        neg = int(input())
        if neg >= 0:
          raise ValueError("Nombre non négatif !")
      except ValueError as erreur:
        print(erreur)

    #Saisie d'un très grand nombre
    big = 0
    while big < 1000:
      try:
        print("Saisir un très grand nombre (>= 1000): ")
        big = int(input())
        if big < 1000:
          raise ValueError("Nombre trop petit !")
      except ValueError as erreur:
        print(erreur)

    #Saisie d'un très petit nombre
    small = 1000
    while small >= 1000:
      try:
        print("Saisir un très petit nombre (< 1000): ")
        small = int(input())
        if small >= 1000:
          raise ValueError("Nombre trop grand !")
      except ValueError as erreur:
        print(erreur)

    
gestion_except()





#Factorielle avec exceptions :
def factorielle_except(n = input()):
  #Saisie d'une chaine de caractère
  if(n.isalpha()):
    raise Exception("Erreur, vous avez saisi une chaine de caractère !")
  #Saisie d'un très petit nombre
  elif(n.isdigit() and int(n)<5):
    raise Exception("Erreur, vous avez saisi un très petit nombre (<5) !")
  
  #Saisie d'un très grand nombre
  elif(n.isdigit() and int(n)>100):
    raise Exception("Erreur, vous avez saisi un très grand nombre (>100)!")
  
  #Saisie d'un nombre complexe
  elif(isinstance(complex(n), complex) and 'j' in n):
    raise Exception("Erreur, vous avez saisi un nombre complexe!")
  
  #Saisie d'un nombre négatif
  elif(n.isdigit() and int(n)<0):
    raise Exception("Erreur, vous avez saisi un nombre négatif !")
  else:
      return int(n)*factorielle_except(int(n)-1)

factorielle_except()