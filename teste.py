INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
print("SOMA É DE:", SOMA)

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número: "))
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

import json as js

dados = '''
{
"faturamento": [1000,2000,0,3000,0,4000,5000,0,6000,7000,0,8000,9000,0,10000]
}
'''

faturamento = js.loads(dados)["faturamento"]
faturamento = [valor for valor in faturamento if valor > 0]


menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mes = sum(faturamento)/ len(faturamento)

dias_maiores_media = len([valor for valor in faturamento if valor > media_mes])

print(f"Menor faturamento foi: R${round(menor_faturamento, 2)}")
print(f"Maior faturamento foi: R$ {round(maior_faturamento,2)}")
print(f"Dias com faturamento acima da média: {dias_maiores_media}")

faturamento_regioes= {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_regioes.values())

percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_regioes.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {round(percentual, 2)}%")


# invertendo as strings aqui

def inverter_string(str):
    invertida = ""
    for i in str:
        invertida = i + invertida
    return invertida

string = input("Informe uma string para inverter: ")

resultado = inverter_string(string)
print("String invertida:", resultado)
