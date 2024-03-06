import random

def representacao_binaria(numero):
    if numero > 1:
        representacao_binaria(numero // 2)
    print(numero % 2, end='')

def busca_binaria_recursiva(lista, x, inicio, fim):
    if inicio > fim:
        return False

    meio = (inicio + fim) // 2

    if lista[meio] == x:
        return True
    elif lista[meio] < x:
        return busca_binaria_recursiva(lista, x, meio + 1, fim)
    else:
        return busca_binaria_recursiva(lista, x, inicio, meio - 1)

def main():
    lista = [random.randint(1, 100) for _ in range(100)]
    lista.sort()
    print(lista)  # Para verificar se está correto
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Representação binária de um número")
        print("2. Verificar se um número está na lista")
        print("3. Sair")
        escolha = input("Opção: ")

        if escolha == '1':
            numero = int(input("Digite um número: "))
            print("A representação binária de", numero, "é: ", end='')
            representacao_binaria(numero)
        elif escolha == '2':
            x = int(input("Qual valor deseja buscar? "))
            if busca_binaria_recursiva(lista, x, 0, len(lista) - 1):
                print(f"{x} foi encontrado na lista.")
            else:
                print(f"{x} não foi encontrado na lista.")
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
