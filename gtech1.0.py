#Alunos:
#Ana Cristina;
#Gustavo Henrique;
#Luisa Clara;

#Professor:
#Geugres Carvalho.

#Vetores
nome= []
cpf= []
telefone= []
email= []
endereço=[]
cidade= []
#contador
s=0
i=0
j=0
contlista=0
#selecionar opção do menu
p=0
#edição
editar=0
#o 1 while repete se responder com uma letra no menu e o segundo o codigo todo
while True:
    try:
        while True:

            print("1-Cadastrar o usuario")
            print("2-listar")
            print("3-Editar")
            print("4-Excluir")
            print("0-sair")
            p=int(input('Escolha 1,2,3,4 ou 0: ')) 
#Cadastro.......................................................................................................................
            if p==1:
#os vetores aceitam tudo, ainda precisa corrigir:
               nome.append(input('Cadastre o Nome:'))
               cpf.append(input("Cadastre o CPF"))
               telefone.append(input("Cadastre o Telefone"))
               email.append(input("Cadastre o Email"))
               endereço.append(input("Cadastre o endereço"))
               cidade.append(input("Cadastre a cidade"))
               s+=1
#---------------------Editar-------------------------------------------------------------------------------------------------------
            elif p==3:
                if(len(nome)==0):
                    print("não a nada na lista")
                else:
                    try:
                        contlista=0
                        for i in range(0,len(nome)):
                            contlista= contlista+1
                            print("Cadastro",contlista," :")
                            print(nome[i])
                        editar=int(input("Digite o numero Referente ao cadastro a ser editado"))
                        if editar>s:
                            print("Erro! A opção escolhida a ser editada não existe. Tente novamente ")
                        else:
                            print("Qual informação você deseja editar")
                    except (ValueError,IndexError):
                        print("Erro! porfavor Digite um numero E um numero referente a um cadastro existente \n\n")
                        
            elif p==0:
                break
#------------Listar-----------------------------------------------------------------------------------------------------------------------------------
            elif p==2:
                contlista=0
                if(len(nome)==0):
                    print("não a nada na lista")
                for i in range(0,len(nome)):
                    contlista= contlista+1
                    print("Cadastro",contlista," :")
                    print(nome[i])
#-----------------------Excluir----------------------------------------------------------------------------------------------------------------------
            elif p==4:
                if(len(nome)==0):
                    print("não a nada na lista Para ser excluido")
                else:
                    print("\n\nDigite um desses numeros a frente do nome cadastro pra ser excluido")
                    for j in range(0,s):
                        print( "cadastro",j,nome[j])
                    try:
                        excl=int(input("Digite o numero do cadastro a ser excluido"))-1
                        del nome[excl]
                        print("Excluido com sucesso")
                    except ValueError:
                        print("Numero invalido! insira o numero correto correspondente a lista de cadastro fornecido")

            else:
                print("Digite o numero 1,2 ou 3")
        break
    except ValueError:
        print('Digite somente uma das opções a seguir:  a opção 1,2,3,4 ou 0')