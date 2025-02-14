#Gtech versao 1.0.0

#Alunos:
#Ana Cristina;
#Gustavo Henrique;
#Luisa Clara;

#Professor:
#Geugres Carvalho.

#Vetores
nome = []
cpf = []
telefone = []
email = []
endereco = []
cidade = []
# Contador
s = 0
i = 0
j = 0
contlista = 0
# Opçoes
p = 0
editar = 0
editar1 = 0

while True:
    try:
        while True:
            print("1-Cadastrar o usuario")
            print("2-listar")
            print("3-Editar")
            print("4-Excluir")
            print("0-sair")
            p = int(input('Escolha 1,2,3,4 ou 0: '))
            
            #essa variavel p acima pescisa resolver o erro:
            
        #     Escolha 1,2,3,4 ou 0: Traceback (most recent call last):
        #   File "c:\Users\gusta\Documents\Geugres\Gtech\gtech1.0.0.py", line 36, in <module>
        #       p = int(input('Escolha 1,2,3,4 ou 0: '))
        #               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        #   KeyboardInterrupt
        #   PS C:\Users\gusta\Documents\Geugres\Gtech>
        
        #em todas as entradas corrigir o erro acima
        
            if p == 1:
             try:
                while True:
                    nome1 = input('Cadastre o Nome: ')
                    if nome1.replace(" ", "").isalpha():
                        nome.append(nome1)
                        break
                    else:
                        print("Erro! O nome deve conter somente letras.")
                while True:
                    cpf1 = input("Cadastre o CPF: ")
                    if cpf1.isdigit() and len(cpf1) == 11:
                        cpf.append(cpf1)
                        break
                    else:
                        print("Erro! O CPF deve conter exatamente 11 digitos númericos.")
                while True:
                    telefone1 = input("Cadastre o Telefone: ")
                    if telefone1.isdigit():
                        telefone.append(telefone1)
                        break
                    else:
                        print("Erro! O telefone deve conter somente números.")
                email.append(input("Cadastre o Email: "))
                endereco.append(input("Cadastre o endereço: "))
                while True:
                    cidade1 = input("Cadastre a cidade: ")
                    if cidade1.replace(" ", "").isalpha():
                        cidade.append(cidade1)
                        break
                    else:
                        print("Erro! A cidade deve conter somente letras.")
                s += 1
             except KeyboardInterrupt:
                 print("\n erro! o cadastro foi interrompido!")
            elif p == 3:
                if len(nome) == 0:
                    print("Não a nada na lista.")
                else:
                    try:
                        contlista = 0
                        for i in range(len(nome)):
                            contlista += 1
                            print("Cadastro", contlista, " :")
                            print(nome[i])
                        editar = int(input("Digite o número referente ao cadastro a ser editado")) - 1
                        #if editar>s:
                        #     print("Erro! A opção escolhida a ser editada não existe. Tente novamente ")
                        #else:
                        #     print("Qual informação você deseja editar")
                        editar1 = int(input("Qual informação deseja editar?\n 1 nome\n 2 cpf\n 3 telefone\n 4 email \n 5 endereço \n 6 cidade\nDigite um número referente ao que você quer editar\n"))
                        if editar1 == 1:
                             while True:
                                nome1 = input('Nome: ')
                                if nome1.replace(" ", "").isalpha():
                                    nome[editar]=nome1
                                    break
                                else:
                                    print("Erro! O nome deve conter somente letras.")
                        elif editar1 == 2:
                            cpf[editar] = input("Novo CPF: ")
                        elif editar1 == 3:
                            telefone[editar] = input("Novo Telefone: ")
                        elif editar1 == 4:
                            email[editar] = input("Novo Email: ")
                        elif editar1 == 5:
                            endereco[editar] = input("Novo Endereço: ")
                        elif editar1 == 6:
                            cidade[editar] = input("Nova Cidade: ")
                        else:
                            print("Erro! Digite somente um número referente à informação que deseja editar.")
                    except (ValueError, IndexError):
                        print("Erro! Por favor, digite um número e um número referente a um cadastro existente.\n\n")
            elif p == 0:
                break
            elif p == 2:
                contlista = 0
                if len(nome) == 0:
                    print("Não a nada na lista.")
                for i in range(len(nome)):
                    contlista += 1
                    print("Cadastro", contlista, " :")
                    print("Nome: ", nome[i])
                    print("CPF: ", cpf[i])
                    print("Telefone: ", telefone[i])
                    print("Email: ", email[i])
                    print("Endereço: ", endereco[i])
                    print("Cidade: ", cidade[i])
            elif p == 4:
                j = 0
                if len(nome) == 0:
                    print("Não a nada na lista para ser excluido.")
                else:
                    print("\n\nDigite um desses números à frente do nome do cadastro para ser excluido.")
                    for j in range(s):
                        print("Cadastro", j, nome[j])
                    try:
                        excl = int(input("Digite o número do cadastro a ser excluido\n"))
                        del nome[excl]
                        del cpf[excl]
                        del cidade[excl]
                        del endereco[excl]
                        del email[excl]
                        del telefone[excl]
                        print("Excluido com sucesso.\n\n")
                        s -= 1
                    except (ValueError, IndexError):
                        print("Erro! A opção escolhida a ser excluida não existe. Tente novamente com o número de cadastros fornecido.\n\n")
            else:
                print("Digite o número 1,2,3,4 ou 0.")
        break
    except ValueError:
        print("Digite somente uma das opções a seguir: 1,2,3,4 ou 0.")
