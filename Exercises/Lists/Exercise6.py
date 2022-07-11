
aluno1 = []
aluno2 = []
aluno3 = []


alunos = [aluno1]


for x in range(0, 3):
    nota_aluno1 = int(input("Informe a nota do aluno 1 "))
    aluno1.append(nota_aluno1)   
sum_aluno1 = sum(aluno1)
media_aluno1 = round(sum_aluno1 / len(aluno1))
aluno1.clear()
aluno1.append(media_aluno1)

#for x in range(0, 3):
    #nota_aluno2 = int(input("Informe a nota do aluno 2 "))
    #aluno2.append(nota_aluno2)

#for x in range(0, 3):
    #nota_aluno3 = int(input("Informe a nota do aluno 3 "))
    #aluno3.append(nota_aluno3)
print(media_aluno1)    
print(alunos)