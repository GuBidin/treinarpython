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

#calculando o fatorial de um número
fatorial = 1
numero_fatorial = int(input("Digite um número inteiro para calcular o fatorial: "))
for i in range(1, numero_fatorial + 1): #for i in range(1, numero_fatorial + 1) significa que o loop vai começar em 1 e vai até numero_fatorial, incluindo o numero_fatorial
    fatorial *= i #fatorial *= i é a mesma coisa que fatorial = fatorial * i
print(f"O fatorial de {numero_fatorial} é: {fatorial}")

#sequencia de Fibonacci
n = int(input("Digite o número de termos da sequência de Fibonacci: "))
a, b = 0, 1 #a primeio termo b segundo termo 0 e 1 são os dois primeiros termos da sequência de Fibonacci
print("Sequência de Fibonacci:")
for _ in range(n):
    print(a, end=' ') #end=' ' é usado para imprimir os números na mesma linha, separados por um espaço
    a, b = b, a + b #a, b = b, a + b é uma forma de atualizar os valores de a e b ao mesmo tempo. 
    #O novo valor de a será o antigo valor de b, e o novo valor de b será a soma do antigo valor de a e do antigo valor de b.


#números primos
numero_primo = int(input("Digite um número inteiro para verificar se é primo: "))
if numero_primo > 1:
    for i in range(2, int(numero_primo**0.5) + 1): #int(numero_primo**0.5) + 1 é usado para otimizar a verificação de números primos,
 # pois um número primo não pode ser dividido por nenhum número maior que sua raiz quadrada.
        if numero_primo % i == 0:
            print(f"O número {numero_primo} não é primo.")
            break
    else:    print(f"O número {numero_primo} é primo.")


#contando o numero de caracteres em uma string
texto = input("Digite um texto: ")
contador = 0
for caractere in texto:
    contador += 1
print(f"O texto '{texto}' tem {contador} caracteres.")
