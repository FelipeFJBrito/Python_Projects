#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

list_number = []
list_even = []
list_odd = []
print("Enter the numbers")

for i in range(0,5):
    data = int(input())
    list_number.append(data)
print(f"The full list is {list_number}")    

for i in list_number:
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)

print(f"The even list is {list_even}")  
print(f"The odd list is {list_odd}")  