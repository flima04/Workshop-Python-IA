n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))

def soma(a, b, c):
    soma = a + b + c
    return soma

print(f"A soma dos números é igual a {soma(n1, n2, n3)}.")