def imprime(n):
    print(f"{n:.3f}°")

imprime(5.35135135)

lista1=[]

lista2=[1,5,9]

#add um elemento na lista:
lista1.append(1)

print(lista1)
lista1.append(5)
lista1.append("string")
lista1.append(lista2)
print(lista1)
print("-"*100)
print(lista1[1])

lista1[1] = 9

# print("Lista 1 após alteração: ",lista1)

# print("a lista 1 tem {} itens".format(len(lista1)))

# print(lista1[len(lista1)-1])


# print(lista1[-1])

lista_numero=[5,7,94,5,.85,7956]

# print(sum(lista_numero))

media_da_lista=sum(lista_numero)/len(lista_numero)
#print(media_da_lista)

#retirando itens da lista: temos duas opções

### .pop() , onde escolhemos o Índice
## o .pop() retorna o valor retirado
lista=[1,4,9,7,9]
print("lista original",lista)

print(lista.pop(1))
print("lista após pop(1):",lista)

### .remove(), onde escolhemos o Valor (a primeira ocorrecia)

print(lista.remove(9))
print("lista após remove(9)",lista)

lista=[1,5,7,5,5,9,6,87,4,5]
lista_reserva=lista.copy()

for i in range(len(lista)):
    if lista[i]==5:
        lista_reserva.remove(5)
    print(lista_reserva)
