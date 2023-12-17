
   """ 1. salários até R$ 280,00 (incluindo) : aumento de 20%
   2. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
   3. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
   4. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento. """


def aumento_20(salario):
    percentual = 20
    valor_aumento = salario * (percentual / 100)
    novo_salario = salario + valor_aumento
    return percentual, valor_aumento, novo_salario

def aumento_15(salario):
    percentual = 15
    valor_aumento = salario * (percentual / 100)
    novo_salario = salario + valor_aumento
    return percentual, valor_aumento, novo_salario

def aumento_10(salario):
    percentual = 10
    valor_aumento = salario * (percentual / 100)
    novo_salario = salario + valor_aumento
    return percentual, valor_aumento, novo_salario

def aumento_5(salario):
    percentual = 5
    valor_aumento = salario * (percentual / 100)
    novo_salario = salario + valor_aumento
    return percentual, valor_aumento, novo_salario

salario = float(input("Digite o salário: "))

if salario <= 280:
    percentual, valor_aumento, novo_salario = aumento_20(salario)
elif salario <= 700:
    percentual, valor_aumento, novo_salario = aumento_15(salario)
elif salario <= 1500:
    percentual, valor_aumento, novo_salario = aumento_10(salario)
else:
    percentual, valor_aumento, novo_salario = aumento_5(salario)

print("Antes do Reajuste:", salario)
print("Percentual de Aumento:", percentual, "%")
print("Valor do Aumento:", valor_aumento)
print("Novo Salário após o Aumento:", novo_salario)
