nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo ao Python!")
#float: números decimais
#int: números inteiros
#string: texto
#variáveis: são usadas para armazenar valores


#fazendo operações matemáticas
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
soma = valor1 + valor2
print(f"A soma de {valor1} e {valor2} é: {soma}")
subtracao = valor1 - valor2
print(f"A subtração de {valor1} e {valor2} é: {subtracao}")
multiplicacao = valor1 * valor2
print(f"A multiplicação de {valor1} e {valor2} é: {multiplicacao}")
if valor2 != 0:
    divisao = valor1 / valor2
    print(f"A divisão de {valor1} por {valor2} é: {divisao}")   
else:    print("Não é possível dividir por zero.")


# Calculando a área de um triângulo
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
area_triangulo = (base * altura / 2)
print(f"A área do triângulo é: {area_triangulo}")

#convertendo temperatura de Celsius para Fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}")

#par ou ímpar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0: #o operador % é o operador de módulo, que retorna o resto da divisão
    print(f"O número {numero} é par.")
else:    print(f"O número {numero} é ímpar.")