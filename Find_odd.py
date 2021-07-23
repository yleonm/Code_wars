
#Primera forma 
""" def find_it(seq):
    frecuencia ={};
    for n in seq:
        if n in frecuencia:
            frecuencia[n] +=1
        else:
             frecuencia[n] = 1

    for clave,valor in frecuencia.items():
        if (valor%2) != 0:
            return clave """

#Segunda forma
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

#Tercera forma
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2 != 0][0]

print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))