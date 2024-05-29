print('Qual é o seu nome? ')
nome = (input('')) #determina automaticamente o tipo string, ou caractere

print('Digite a nota da primeira unidade: ')
nota1u = float(input('')) #float é o tipo Real

print('Digite a nota da segunda unidade: ')
nota2u = float(input(''))

print('Digite a nota da terceira unidade: ')
nota3u = float(input(''))

print('Digite a nota da quarta unidade: ')
nota4u = float(input(''))

notaTotal = (nota1u + nota2u + nota3u + nota4u)

notaFinal = (notaTotal / 5.0)

if (notaFinal >= 5.0) :
    print (f"Parabéns {nome}, sua nota final foi de: {notaFinal:.1f}") #o :.2f faz o valor da variável ter somente duas casas decimais
else:
    print(f"Puxa {nome}, você ficou de recuperação. Sua nota foi de: {notaFinal:.1f}")


print("Muito obrigado por terem participado da palestra :)")







# Algoritmo "palestra"
# Var

#  nota1u, nota2u, nota3u, nota4u, notaFinal: Real
#nome: Caractere



# Inicio

# Escreval("Digite a nota da Primeira Unidade: ")
# Leia(nota1u)
# Escreval("Digite a nota da Segunda Unidade: ")
# Leia(nota2u)
# Escreval("Digite a nota da Terceira Unidade: ")
# Leia(nota3u)
# Escreval("Digite a nota da Quarta Unidade: ")
# Leia(nota4u)

# notaUnidades <- (nota1u + nota2u + nota3u + nota4u)

#notaFinal = (notaUnidades / 5)

# Escreval("Sua nota final foi: ", notaFinal)


# Se (notaFinal >= 5.0) entao
#  Escreva("Parabéns, você passou de ano!")
#  Senao
#   Escreva("Infelizmente você não atingiu a média necessária e ficou de recuperação")


# fimSe



# Fimalgoritmo