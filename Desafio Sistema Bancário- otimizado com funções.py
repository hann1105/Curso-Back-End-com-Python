def menu():
    titulo=("Banco PH")
    print(titulo.center(40,"*"))
    print("Bem vindo ao Banco PH")
    print("[d] depositar")
    print("[s] sacar")
    print("[e] extrato")
    print("[nc] Nova conta")
    print("[lc] Listar contas")
    print("[nu] Novo usuário")
    print("[a] sair")


def saque(*,saldo,valor,extrato,limite,numero_saques,limite_saque):
    print("IMPORTANTE: Você só pode realizar 3 saques e o limite para saque é R$500,00")
    if valor <= 0:
        print("Valor inválido, tente novamente.")
    elif valor >= saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("O valor do saque é maior que o limite de R$500,00.")
    elif numero_saques >= limite_saque:
        print("Você já atingiu o limite diário de saques (3).")
    else:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques


def deposito(saldo,valor,extrato,/):
    if valor>0:
        saldo+=valor
        print("Operação realizada com sucesso")
        extrato+=(f"Depósito: R${valor:.2f}")
    else:
        print("Valor inválido, tente novamente")
    return saldo,extrato

def mostrar_extrato(saldo,/,*,extrato):
    print("************** EXTRATO **************")
    print(f"Saldo: R${saldo:.2f}")
    print("*************************************")



def criar_conta(agencia,numero_conta,usuarios):
    senhas=[]
    print("Crie sua conta")
    usuario=str(input("Insira o nome do usuário: "))
    cpf=str(input("Insira o CPF do usuário: "))
    senha_usuario=str(input("Insira uma senha de segurança: "))
    senhas.append(senha_usuario)
    for usuario_dict in usuarios:
        if usuario_dict["cpf"] == cpf:
            print("Conta criada com sucesso!")
        return {"Agência": agencia, "Numero_conta": numero_conta, "Usuario": usuario}
    print("CPF não encontrado. Crie um usuário antes de criar a conta.")
    return None
    
def criar_usuario(usuarios):
    print("Criar usuário:")
    nome_usuario=str(input("Insira seu nome: "))
    cpf_usuario=str(input("Insira seu CPF (Apenas Números): "))
    data_nascimento=str(input("Insira sua data de nascimento [**/**/****]: "))
    endereco_usuario=str(input("Insira seu endereço [logradouro,nro- bairro- cidade-estado]: "))
    usuarios.append({"nome":nome_usuario,"cpf":cpf_usuario,"data_nascimento":data_nascimento,"endereço":endereco_usuario})
    print("Usuário criado com sucesso! ")

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['Agência']}")
        print(f"C/C: {conta['Numero_conta']}")
        print(f"Titular: {conta['Usuario']}")
        print("=========================================")


def main():
    saldo=0
    limite=500
    extrato=""
    numero_saques=0
    limite_saque=3
    AGENCIA="0001"
    usuarios=[]
    contas=[]

    while True:
        menu()
        escolha=str(input("Escolha a opção que você deseja: "))
        if escolha =="d":
            valor=float(input("Digite o valor que deseja depositar na sua conta: "))
            saldo,extrato=deposito(saldo,valor,extrato)
        elif escolha=="s":
           valor=float(input("Digite o valor que deseja sacar: "))
           saldo,extrato,numero_saques=saque(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saque=limite_saque)
        elif escolha== "e":
            mostrar_extrato(saldo,extrato=extrato)
        elif escolha=="nc":
            numero_conta=len(contas)+1
            conta=criar_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)
        elif escolha=="lc":
            listar_contas(contas)
        elif escolha=="nu":
            criar_usuario(usuarios)
        elif escolha =="a":
            break
        else:
            print("Escolha inválida, tente novamente [d],[s],[e],[nc],[lc],[nu],[a] ")
if __name__ == "__main__":
    main()


    
    

