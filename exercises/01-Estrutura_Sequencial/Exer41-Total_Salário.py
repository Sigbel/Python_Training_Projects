"""
Exercício 41 - Total do Salário

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

hora_valor = float(input("Digite o valor pela hora trabalhada: "))
hora_trabalhada = float(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = hora_valor * hora_trabalhada
IR = salario_bruto*0.11
INSS = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - IR - INSS - sindicato
print()
print(f"+ Salário Bruto: R$ {salario_bruto:.2f}\n- IR (11%): R$ {IR:.2f}\n- INSS (8%): R$ {INSS:.2f}\n- Sindicato (5%): R$ {sindicato:.2f}\n= Salário Líquido: R$ {salario_liquido:.2f}")