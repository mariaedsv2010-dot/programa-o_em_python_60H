import statistics








def verificar(lista):
     variancia = statistics.mean(lista)
     print('variancia:',variancia)
     moda = statistics.mode(lista)
     print('moda:',moda)
     desvio = statistics.stdev(lista)
     print('desvio:',desvio)



