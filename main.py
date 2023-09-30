# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# def soma(x,y):
#  return x+y
#
# def sub(x,y):
#     return x-y
#
# def mult (x,y):
#  return x*y
#
# def dive(x,y):
#  return x/y
#
# valor1= int (input('Entre com valor1'))
# op = input('digite a opração desejada')
# valor2=int (input('entre com valor2'))
#
# if op =='+':
#     print(soma(valor1, valor2))
#
# elif op == '-':
#     print(sub(valor1,valor2))
#
# elif op == '*':
#     print(mult(valor1,valor2))
#
# elif op == '/':
#     print(dive(valor1,valor2))
#
# else:
#     # print('funçao invalida')

# //def pessoas (**kwargs):
#     print (kwargs)
#     for nome, idade in kwargs.items():
#         print(f'{nome} tem atualente {idade} anos de idade')
#
#
# pessoas(isaque = '33', jhow = '45', cadu = '22')

# //def a (x):
#     return x**2
# print(a(4))
# b= lambda x: x**2
# print(b(4))
#
# S= lambda x,y: x+y
# print(S(2,3))

# //lista = [4,5,6,7,8]
# print(lista)
#
# lista.append(2)
# print(lista)
#
# lista.insert(2, -3)
# print (lista)
#
# lista.remove(4)
# print(lista)
#
# lista2=[10,5,7,6,1,3,2,70]
# lista2.sort()
# print(lista2)
#
# lista2.reverse()
# print(lista2)
#
# lista3= [2,3,4,5,7,5,9,5]
# qnt = lista3.count(5)
# print(qnt)
#
# lista4 = [1,2,3,4,5,6,7,8,9]
#
# exc = lista4.pop()
#
# print(exc)
#
#
# lista5 = [1,2,3,4,5,6,7,8,9,10]
# lista.pop()
# print(lista5)
#
# lista6 = [1,2,3,4,5]
# del lista6[2]
# print(lista6)
#
# lista7 = [2,4,6,8,10,12]
# del lista[2.5]

#
# nova = []
#
# while True:
#     num = int(input('Digite um numero'))
#        if num == 0:
#         break
#         nova.append(num)
#         print(nova)

#
# lista1 =[]
# listapar=[]
# listaimpar=[]
# soma=0
# somapar=0
# somaimpar=0
# while True:
#     num =int(input("entre com num"))
#     lista1.append(num)
#     soma+=num
#     if num==0:
#         print('assim não mlk')
#         break
#     if num%2==0:
#         listapar.append(num)
#         somapar+=num
#     if num%2!=0:
#         listaimpar.append(num)
#         somaimpar+=num
#
# print(lista1.sort())
# print(listapar.sort())
# print(listaimpar.sort())
# print()
# print(soma)
# print(somapar)
# print(somaimpar)
#
# quantidade = len(lista1)
# print(quantidade)


# lista1 = []
# soma=0
# mult=1
# maior = 0
# menor = 100
#
# while True:
#     num=int (input('Entre com num'))
#     lista1.append(num)
#     soma += num
#     if num == 0:
#         break
#     if num> maior:
#      maior = num
#     if num < menor:
#         menor = num
#
#     if num!=0:
#         mult*=num
#     print(lista1)
#     print(maior)
#     print(menor)
#     print(soma)
#     print(mult)

# //palavra = 'python é uma linguagem de Programação. python é simples python é organizado é uma excelente linguagem '
# print(palavra.count('é'))
# print(palavra.find('python', 25,50))
# print(palavra.rfind('lingua'))
# print(palavra.index('é'))
# print(palavra.rindex('é'))
#
# palavra = 'olá mundo!'
#
# palavra_centro = palavra.center (20)
# palavra_centro_2 = palavra.center (20,'=')
# palavra_esquerda = palavra.ljust(12)
# palavra_direita = palavra.rjust(12)
# print(f'{palavra_esquerda}*{palavra_direita}**')
#
# f1 = f.replace ( 'Python', 'Bicicleta')
# f2 = f.replace ('','#')
#
# print(f1)
# print(f2)
#
# palavra = 'ola mundo'
# print (f'{palavra}')
#
# b= palavra.split()
# print(f'{b}')
#
# c= palavra.lstip()
# print(f'{c}')
#
# d= palavra.rstrip()
# print(f'{d}

# #fazer a palavra ficar  em vertical
# nome = input('entre com uma palavra')
# for i in range (len(nome)):
#     print(nome[i].upper(),'\n')

# nome = input ('Entre com uma palavra')
# print(nome[::-1].upper())
#
# nome = input('entre com palavra')
# vazia = ''
# for letra in nome:
#     vazia += letra
#     print(vazia)
#
#     nome = input ('entre com o nome')
#     vazio1= ''
#     vazio2 = ''
#     for i in nome:
#         vazio1+= letra
#         for i in range (len(nome)):
#             vazio2 = vazio1[0:len(nome)-i:]
#             print(vazio2)

lista = [1,2,3]
lista1 = list (map(lambda x:x*3, lista))
print (lista1)

lista = [1,2,3,4,5,6]
lista1= list (filter (lambda x:x%2!=0,lista))
print(lista1)

#filter(função a ser aplicada, lista)





















