'''[PY-A01]Faça um programa em Python que, utilizando estruturas de repetição, calcule a média de idade dos alunos de uma turma. O programa deve pedir ao usuário a quantidade de alunos na turma e, em seguida, solicitar a idade de cada um. O programa deve utilizar um laço FOR para receber as idades dos alunos e um laço WHILE para realizar a soma das idades. Ao final, o programa deve exibir a média de idade da turma.'''




alunos = int(input('Digite a quantidade de alunos na sala:'))
somaIdade = 0
for c in range(1, alunos +1):
    nome = str(input('Nome do {}º aluno: '.format(c)))
    idade = int(input('Idade do {}º aluno: '.format(c)))
    somaIdade += idade

media = somaIdade / alunos

while c < alunos+1:
    print('Temos {} alunos em sala com uma média de idade de {} anos'. format(alunos,media))
    c += 1

    
    




       



