
def cadastrodicio (lista):
    print("\n")
    nome=input("digite seu nome: ")
    idade= int(input("digite sua idade: "))
    cidade=input("digite o nome da sua cidade: ")
    endereco=input("digite o seu endereço: ")
    dicio = {
        'nome':nome,
        'idade':idade,
        'cidade':cidade,
        'endereco':endereco,
    }
    print('\n')
    return lista.append(dicio)
def mostrarcadastro(lista):
    print('\n')
    for i in range(len(lista)):
        print(f"{i+1} Nome: {lista[i]['nome']}, Idade: {lista[i]['idade']}, Cidade: {lista[i]['cidade']}, Endereço: {lista[i]['endereco']}")
    print("\n")
def exclusao(lista):
    print('\n')
    mostrarcadastro(lista)
    print("\n, digite o numero do cadastro que deseja excluir:")
    excl=int(input())
    if excl < 0 or excl> len(lista):
        print("numero invalido")
    else:
        excl-=1
        print(f"Cadastro {lista[excl]} deletado com sucesso")
        lista.pop(excl)
def editardicio(lista):
    print('\n')
    mostrarcadastro(lista)
    print("\n, digite o numero do cadastro que deseja editar:")
    edit=int(input())
    if edit < 0 or edit> len(lista):
        print("numero invalido")
    else:
        edit-=1
        nome=input("digite seu nome: ")
        idade= int(input("digite sua idade: "))
        cidade=input("digite o nome da sua cidade: ")
        endereco=input("digite o seu endereço: ")
        lista[edit]['nome'] = nome
        lista[edit]['idade'] = idade
        lista[edit]['cidade'] = cidade
        lista[edit]['endereco'] = endereco
def main():
    lista=[]
    while True:
        op= int(input('digite uma opção: 1-cadastrar 2-mostrar dicionario 3- excluir 4-editar '))
        if op == 1:
            cadastrodicio(lista)
        if op== 2:
            mostrarcadastro(lista)
        if op == 3:
            exclusao(lista)
        if op == 4:
            editardicio(lista)
main()