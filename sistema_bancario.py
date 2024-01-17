N = 1
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo = 0
limite_saque = 500
saque = 0
NUMERO_DE_SAQUES_DIARIO = 3
qtde_saque = 0
valor_saque = saque


while N > 0:
    opcao = input(menu)
   
    if opcao == "1":
        print("Insira o valor do depósito:")
        saldo = int(input())
        
        if saldo > 0:
            print("Depósito efetuado com sucesso!")


        elif saldo <= 0:
            print("Não é possível realizar depósito com valor negativo! Insira um novo valor.")


    elif opcao == "2":
        print("Insira o valor do saque:")
        valor_saque = int(input())

        if saldo <= 0:
            print("Saldo insuficiente na conta. Faça um depósito.")

        elif valor_saque > 0 and valor_saque == limite_saque:
            print("Saque efetuado com sucesso!")

            qtde_saque += 1
          #  print(f"limite diário de saques = {qtde_saque} de 3")

        elif valor_saque > limite_saque:
            print("O limite de saque permitido é de R$500. Insira um novo valor.")

        elif valor_saque <= 0:
            print("Não é possível realizar um saque com valor negativo! Insira um novo valor.")

        if qtde_saque >= 4:
            print("Limite de saque excedido! Tente novamente amanhã.")
        
    elif opcao == "3":
        print(f"""
            EXTRATO BANCÁRIO
            ---------------------------------------------
            Saldo atual: R$ {saldo - valor_saque}
            Limite de saque: R$ {limite_saque}
            Saques disponíveis: {qtde_saque} de 3
            ---------------------------------------------
            Obrigado por utilizar nossos serviços.
            =>""")

    elif opcao == "4":
        print("Saindo da sua conta...")
        break
    else:
        print("Operação inválida, por favor selecione a opção desejada!")



