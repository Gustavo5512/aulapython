import re
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
# Opç0es
p = 0
editar = 0
editar1 = 0

email_regex = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'

while True:
    try:
        while True:
            print("1-Cadastrar o usuario")
            print("2-listar")
            print("3-Editar")
            print("4-Excluir")
            print("0-sair")
            p = int(input('Escolha 1,2,3,4 ou 0: '))
#------------------------------------------- Cadastro            
            if p == 1: 
                try:
                    while True:
                        nome1 = input('Nome: ')
                        partes_nome = nome1.split()
                        if len(partes_nome) >= 2 and all(p.isalpha() for p in partes_nome):
                            nome.append(nome1)
                            break
                        else:
                            print("Erro! O nome deve conter pelo menos duas palavras e somente letras.")

                    while True:
                        cpf1 = input("CPF: ")
                        if cpf1.isdigit() and len(cpf1) == 11:
                            if cpf1 in cpf:
                                print("Erro! Este CPF já está cadastrado.") 
                            else:
                                soma1 = sum(int(cpf1[i]) * (10 - i) for i in range(9))
                                resto1 = (soma1 * 10) % 11
                                if resto1 == 10:
                                    resto1 = 0
                                soma2 = sum(int(cpf1[i]) * (11 - i) for i in range(10))
                                resto2 = (soma2 * 10) % 11
                                if resto2 == 10:
                                    resto2 = 0
                                if int(cpf1[9]) == resto1 and int(cpf1[10]) == resto2:
                                    cpf.append(cpf1)
                                    break
                                else:
                                    print("Erro! CPF inválido.") 
                        else:
                            print("Erro! O CPF deve ter exatamente 11 dígitos numéricos.")

                    while True:
                        telefone1 = input("Telefone: ")
                        if telefone1.isdigit():
                            telefone.append(telefone1)
                            break
                        else:
                            print("Erro! O telefone deve conter somente números.")

                        email_regex = r'^(?=.[a-z])(?=.[A-Z])(?=.*\d)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                    while True:
                        email1 = input("Email: ")
                        if re.match(email_regex, email1):
                            email.append(email1)
                            break
                        else:
                            print("Erro! O e-mail deve conter pelo menos uma letra maiúscula, uma minúscula e um número.")
                    endereco.append(input("Endereço/Rua: "))

                    while True:
                        cidade1 = input("Cidade: ")
                        if cidade1.replace(" ", "").isalpha():
                            cidade.append(cidade1)
                            break
                        else:
                            print("Erro! A cidade deve conter somente letras.")
                    
                    s += 1 
                except KeyboardInterrupt:
                    print("\nErro! O cadastro foi interrompido!")
#-------------------------------EDitar
            elif p == 3:
                
                if len(nome) == 0:
                    print("Não há nada na lista.")
                else:
                    try:
                        contlista = 0
                        for i in range(len(nome)): 
                            contlista += 1
                            print("Cadastro", contlista, " :")
                            print(nome[i])
                        editar = int(input("Digite o número referente ao cadastro a ser editado: ")) - 1
                        if editar >= s:
                            print("Erro! A opção escolhida a ser editada não existe. Tente novamente.")
                        else:
                            print("Qual informação você deseja editar?")
                            editar1 = int(input("1 Nome\n2 CPF\n3 Telefone\n4 Email\n5 Endereço\n6 Cidade\nDigite um número referente ao que você quer editar: "))

                            if editar1 == 1:
                                while True:
                                    nome1 = input('Novo Nome: ')
                                    partes_nome = nome1.split()
                                    if len(partes_nome) >= 2 and all(p.isalpha() for p in partes_nome):
                                        nome[editar] = nome1
                                        break
                                    else:
                                        print("Erro! O nome deve conter pelo menos duas palavras e somente letras.")
                            elif editar1 == 2:
                                while True:
                                    cpf1 = input("Novo CPF: ")
                                    if cpf1.isdigit() and len(cpf1) == 11:
                                        soma1 = sum(int(cpf1[i]) * (10 - i) for i in range(9))
                                        resto1 = (soma1 * 10) % 11
                                        if resto1 == 10:
                                            resto1 = 0
                                        soma2 = sum(int(cpf1[i]) * (11 - i) for i in range(10))
                                        resto2 = (soma2 * 10) % 11
                                        if resto2 == 10:
                                            resto2 = 0
                                        if int(cpf1[9]) == resto1 and int(cpf1[10]) == resto2:
                                            cpf[editar] = cpf1
                                            break
                                        else:
                                            print("Erro! CPF inválido.")
                                    else:
                                        print("Erro! O CPF deve ter exatamente 11 dígitos numéricos.")
                            elif editar1 == 3:
                                while True:
                                    telefone1 = input("Novo Telefone: ")
                                    if telefone1.isdigit():
                                        telefone[editar] = telefone1
                                        break
                                    else:
                                        print("Erro! O telefone deve conter somente números.")
                            elif editar1 == 4:
                                email[editar] = input("Novo Email: ")
                            elif editar1 == 5:
                                endereco[editar] = input("Novo Endereço: ")
                            elif editar1 == 6:
                                while True:
                                    cidade1 = input("Cidade: ")
                                    if cidade1.replace(" ", "").isalpha():
                                        cidade[editar] = cidade1
                                        break
                                    else:
                                        print("Erro! A cidade deve conter somente letras.")
                            else:
                                print("Erro! Digite somente um número referente à informação que deseja editar.")
                    except (ValueError, IndexError):
                        print("Erro! Por favor, digite um número e um número referente a um cadastro existente.\n\n")
            elif p == 0:
                break
 #----------------------------------------------------Listar
            elif p == 2:
                contlista = 0
                if len(nome) == 0:
                    print("Não há nada na lista.")
                for i in range(len(nome)):
                    contlista += 1
                    print("\nCadastro", contlista, " :")
                    print("Nome: ", nome[i])
                    print("CPF: ", cpf[i])
                    print("Telefone: ", telefone[i])
                    print("Email: ", email[i])
                    print("Endereço: ", endereco[i])
                    print("Cidade: ", cidade[i])
# -----------------------------------------------Excluir
            elif p == 4: 
                j = 0
                if len(nome) == 0:
                    print("Não há nada na lista para ser excluído.")
                else:
                    print("\n\nDigite um desses números à frente do nome do cadastro para ser excluído.")
                    for j in range(s):
                        print("Cadastro", j, nome[j])
                    try:
                        excl = int(input("Digite o número do cadastro a ser excluído\n"))
                        del nome[excl]
                        del cpf[excl]
                        del cidade[excl]
                        del endereco[excl]
                        del email[excl]
                        del telefone[excl]
                        print("Excluído com sucesso.\n\n")
                        s -= 1
                    except (ValueError, IndexError):
                        print("Erro! A opção escolhida a ser excluída não existe. Tente novamente com o número de cadastros fornecido.\n\n")
            else:
                print("Digite o número 1,2,3,4 ou 0.")
        break
    except ValueError:
        print("Digite somente uma das opções a seguir: 1,2,3,4 ou 0.")