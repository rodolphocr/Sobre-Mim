#QUANDO VOCÊ USA UMA CONDIÇÃO COMO IF - ENTÃO - SENÃO, E NA SEQUENCIA FOR USAR UM PRINT(Ex01) PARA MOSTRAR NA TELA VOCÊ VERÁ QUE EXISTIRA 4 ESPAÇOS DO INICIO DO PARAGRAFO ATÉ A PRIMEIRA LETRA DE 'PRINT', ISSO QUER DIZER QUE TUDO QUE ESTIVER COM ESSES 4 ESPAÇOS EMBAIXO DO IF, PERTENCE A ESSE COMANDO. E ASSIM PARA O ELIF E ELSE.

# CHECAGEM DE VELOCIDADE.
v=int(input('Entre com a velocidade da pista: '))
if v > 110:
   print('Acima da velocidade permitida')
   print('Reduza a velocidade')
elif  v < 60:
   print('Aumente a velocidade até 80KM/h')
else:
    print('Velocidade ok')

#CHECAR O FINANCIMANETO.
renda=float(input('Entre com a renda: '))
nome=str(input('Nome limpo sim ou não: '))
if renda >= 5000 and nome == "sim":
    print('Financiamento aprovado')
else:
    print('Financiamento não aprovado')

#CALCULO DE IDADE PARA VOTAÇÃO
idade=int(input('Qual a idade do cidadão? '))
if idade >=16:
    print('Você pode votar')
else:
    print('Você é muito novo para votar')

# CALCULANDO MÉDIAS DE NOTAS.
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
sn = nota1 + nota2
m = sn / 2
print('A média entre {} e {} é igual a {}'.format(nota1, nota2, m))

if m >=6:
    print('Sua média foi {} então você passou.'.format(m))
else:
    print('Sua média foi {} então você não passou.'.format(m))


#FINANCIMENTO DE VEÍCULO COM DESCONTO.
automovel = str(input('Carro ou Moto: '))
while automovel == 'carro':
    print('Entre com os dados dos valores abaixo.')
    break
while automovel == 'moto':
    print('Não temos mais motos no estoque.')
    break
preco = float(input('Digite valor do carro: '))
if preco > 50000:
    porcentagem = (preco * 10  / 100)
    novo = (preco - porcentagem)
    print('Voce tem R$ {:.0f} de desconto.'.format(preco * 10 / 100))
    print('Sendo o valor do carro de R${:.0f}'.format(novo))
else:
    print("Valores de automoveis menores de R$50.000,00 não tem desconto.")

# Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input('Entre com o primeiro número: '))
n2 = int(input('Entre com o segundo número: '))

if n1 > n2:
    print('O maior número informado é {}'.format(n1))
else:
    print('O maior número informado é {}'.format(n2))

# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra = str(input('Entre com a letra F para Feminino or M para Masculino: '))
if letra == 'F':
    print('FEMININO')
if letra == 'M':
    print('MASCULINO')
elif letra != 'F' and 'M':
    print('Sexo Inválido.')

# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
# Comando exit(), é uma função que termina um outro comando ou finaliza um programa ou função.
materia = str(input('Entre com a matéria de referencia: '))
nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))
soma = (nota1 + nota2)
media = (soma / 2)
print('Sua média é {}.'.format(media))
while media == 10:
    print('Aprovado com distinção na máteria de {}.'.format(materia))
    exit()
if media < 7:
    print('Reprovado na matéria de {}, estude mais.'.format(materia))
elif media >= 7:
    print('Você foi aprovado na máteria de {}.'.format(materia))

#UTILIZAÇÃO DE IMPORTAÇÃO DE MODULOS, GOTO_PY.
from goto_py import goto
user = str(input('Entre com o usuário: '))
senha = str(input('Entre com a senha: '))

if user == senha:
    print(f' O usuário {user} não pode ser o mesmo que a senha {senha}, entra novamente com os dados.')
    goto(2)
else:
    print('Alteração de senha feita com sucesso.')
