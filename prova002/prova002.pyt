'''Crie um exemplo de cada uma das principais tipagens de variáveis.
Crie uma solicitação de dados ao usuário.
Imprima a solicitação anterior na tela com uma mensagem personalizada.'''

'''Exemplo com variável "str"'''

nome = str(input('Qual seu nome?'))

'''Exemplo com variável "int"'''

idade = int(input('Qual sua idade?'))

'''Exemplo com variável "float"'''

altura = float(input('Qual sua altura?'))

'''Exemplo com variável "bool"'''

print(bool(altura > 1.80))

print('Seu nome é {}, tem {} anos e mede {} de altura' .format(nome,idade,altura))



