titulo=("Banco PH")
print(titulo.center(40,"*"))
print("Bem vindo ao Banco PH")
print("[d] depositar")
print("[s] sacar")
print("[e] extrato")
print("[a] sair")

saldo=0
limite=500
extrato=""
numero_saques=0
limite_saques=3

while True:
    escolha=str(input("Escolha a opção que você deseja: "))
    if escolha =="d":
        deposito=float(input("Digite o valor que deseja depositar na sua conta: "))
        saldo+=deposito
        print("Operação realizada com sucesso")
    elif escolha=="s":
        print("IMPORTANTE: Você só pode realizar 3 saques e o limite para saque é R$500,00")
        if saldo>0:
            saque=float(input("Digite o valor que deseja sacar: "))
            numero_saques+=1
            saldo-=saque
            if saque>limite:
                print("O valor do saque é maior que o valor limite de R$500,00, tente novamente")
            elif numero_saques>3:
                print("Você ja utilizou o limite diários de saques permitidos (3)")
        else:
                print("Saldo Zerado, você não tem dinheiro para Sacar")
    elif escolha== "e":
        print("************** EXTRATO **************")
        print(f"Saldo: R${saldo:.2f}")
        print("*************************************")
    elif escolha =="a":
        break
    else:
        print("Escolha inválida, tente novamente [d],[s],[e],[a] ")
