from librerias import definiciones_matematicas

def main():
  print("Hello learners!")

  #agrego casos de prueba hardcodeados para las funciones declaradas
  print(definiciones_matematicas.addmultiplenumbers([1,2,3,4,5]))
  print(definiciones_matematicas.multiplymultiplenumbers([1,2,4,8,16,32]))
  print(definiciones_matematicas.isiteven(1))
  print(definiciones_matematicas.isiteven(4))
  print(definiciones_matematicas.isitaninteger(1))
  print(definiciones_matematicas.isitaninteger(89.99))
  print(definiciones_matematicas.isitaninteger("generation"))
  print(definiciones_matematicas.isitaninteger(False))
  

if __name__=="__main__":
  main()
