import statistics








def verificar(lista,lista2,lista3,lista4):
     variancia = statistics.mean(lista)
     print(variancia)
     moda = statistics.mode(lista)
     print(moda)
     desvio = statistics.stdev(lista)
     print(desvio)

     variancia1 = statistics.mean(lista2)
     print(variancia1)
     moda1 = statistics.mode(lista2)
     print(moda1)
     desvio1 = statistics.stdev(lista2)
     print(desvio1)


     variancia2 = statistics.mean(lista3)
     print(variancia2)
     moda2 = statistics.mode(lista3)
     print(moda2)
     desvio2 = statistics.stdev(lista3)
     print(desvio2)

     variancia3 = statistics.mean(lista4)
     print(variancia3)
     moda3 = statistics.mode(lista4)
     print(moda3)
     desvio3 = statistics.stdev(lista4)
     print(desvio3)