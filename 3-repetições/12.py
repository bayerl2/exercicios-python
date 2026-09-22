soma = 0 

numero = float(input("Digite um número (0 para parar): "))

while numero != 0:
    soma += numero 
    numero = float(input("Digite um numero (0 para parar): "))

print("Soma: ", soma)