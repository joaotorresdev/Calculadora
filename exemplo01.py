import os
sentinela = 1

while(sentinela == 1):
    print("*****Operações disponíveis******")
    print("1 - para Adição                *")
    print("2 - para Subtração             *")
    print("3 - para Multiplicação         *")
    print("4 - para Divisão               *")
    print("********************************")
    
    operacao = int(input("Escolha uma das operações acima: "))
    valor1 = float(input("Digite o primeiro número: "))
    valor2 = float(input("Digite o segundo número: "))

    if(operacao == 1):
        resultado = valor1 + valor2
    elif(operacao == 2):
        resultado = valor1 - valor2
    elif(operacao == 3):
        resultado = valor1 * valor2
    elif(operacao == 4):
        # Dica: É bom verificar se valor2 é zero antes de dividir!
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            resultado = print("Erro (divisão por zero)")
    else:
        resultado = 0
        print("Operação não informada corretamente")

    print("O resultado do cálculo é: ", resultado)

    print("---------------------------------------")
    print("Deseja continuar?\n1-Sim\n2-Não")
    sentinela = int(input("Informe a opção: "))
    
    if (sentinela == 2):
        print("Programa encerrado")
        
    os.system("cls")


    