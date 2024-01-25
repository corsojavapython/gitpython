
#calcolo fibonacci

def quadrato(lato):

    area = lato * lato
    perimetro = lato * 4
    
    return (area, perimetro)



def calcolafibonacci(lunghezza):
    
    pippo = []

    primo  = 0
    secondo = 1

    for x in range(lunghezza):

        fibo = primo + secondo

        primo = secondo
        secondo = fibo

        pippo.append(fibo)

    return pippo


paperina = quadrato(5)
ar, per = paperina

lista = list(paperina)
print(lista)

print (lista[0])
print (lista[1])

dicquadrato = {}

dicquadrato['AREA'] = ar
dicquadrato['PERIMETRO'] = per

print(dicquadrato)

#print(paperina)
#print(f'Area: {ar}, Perimetro: {per}')
#print('Area: ' + str(ar) + ', Perimetro: '+ str(per))