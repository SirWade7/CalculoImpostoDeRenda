# Este cálculo não leva em consideração os descontos do INSS
# This calculation does not consider INSS discounts

# Dedução de dependentes
def ded_dep(d):
    deducao = d * 189.59
    return deducao

#Faixa 1 do imposto
def faixa1():
    imp_dev = 0
    return imp_dev

#Faixa 2 do imposto
def faixa2(sal_ded):
    imp_dev = sal_ded * 0.075 - 142.8
    return imp_dev

#Faixa 3 do imposto
def faixa3(sal_ded):
    imp_dev = sal_ded * 0.15 - 354.8
    return imp_dev

#Faixa 4 do imposto
def faixa4(sal_ded):
    imp_dev = sal_ded * 0.225 - 636.13
    return imp_dev

#Faixa 5 do imposto
def faixa5(sal_ded):
    imp_dev = sal_ded * 0.275 - 869.36
    return imp_dev

#Menu
def menu():
    opcao = int(input('1 - Calcular imposto\n0 - Sair\n'))
    if opcao == 0:
        print("Saindo . . .")
    elif opcao == 1:
        calc_imp()
        menu()
    else:
        print("Opção inválida!!!\n")
        menu()

#Calculo do imposto
def calc_imp():
    salario = float(input('Digite seu salário:\n'))
    d = float(input('Digite a quantidade de dependentes:\n'))
    deducao = ded_dep(d)
    sal_ded = salario - deducao

    if sal_ded <= 1903.98:
        imp_dev = faixa1()
        imp_dev = round(imp_dev, 2)
        sal_liq = salario - imp_dev
        sal_liq = round(sal_liq, 2)
        print(f"Seu salário liquido: {sal_liq} \nSeu imposto devido: {imp_dev} \nAlíquota do imposto: 0%\n")

    elif sal_ded > 1903.98 and sal_ded <= 2826.65:
        imp_dev = faixa2(sal_ded)
        imp_dev = round(imp_dev, 2)
        sal_liq = salario - imp_dev
        sal_liq = round(sal_liq, 2)
        print(f"Seu salário liquido: {sal_liq} \nSeu imposto devido: {imp_dev} \nAlíquota do imposto: 7,5%\n")

    elif sal_ded > 2826.65 and sal_ded <= 3751.05:
        imp_dev = faixa3(sal_ded)
        imp_dev = round(imp_dev, 2)
        sal_liq = salario - imp_dev
        sal_liq = round(sal_liq, 2)
        print(f"Seu salário liquido: {sal_liq} \nSeu imposto devido: {imp_dev} \nAlíquota do imposto: 15%\n")

    elif sal_ded > 3751.05 and sal_ded <= 4664.68:
        imp_dev = faixa4(sal_ded)
        imp_dev = round(imp_dev, 2)
        sal_liq = salario - imp_dev
        sal_liq = round(sal_liq, 2)
        print(f"Seu salário liquido: {sal_liq} \nSeu imposto devido: {imp_dev} \nAlíquota do imposto: 22,5%\n")

    else:
        imp_dev = faixa5(sal_ded)
        imp_dev = round(imp_dev, 2)
        sal_liq = salario - imp_dev
        sal_liq = round(sal_liq, 2)
        print(f"Seu salário liquido: {sal_liq} \nSeu imposto devido: {imp_dev} \nAlíquota do imposto: 27,5%\n")


menu()