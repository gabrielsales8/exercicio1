listaNumeros= []
print ('Informe os 10 numeros')
for i in range(10):
    listaNumeros.append(input('Numero '+ str(i+1) + ':\n'))
    listaNumeros.reverse()
print (listaNumeros)