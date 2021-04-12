"""

3º Problema - Conjectura de Collatz
A conjectura de Collatz, também conhecida como problema 3N + 1 é uma sequência de números,
como a sequência de Fibonacci. Considera-se um número inteiro positivo N superior a 1. Se N for par
divide-se por dois (2/N), se N for ímpar multiplica-se por três e soma-se mais um (3*N+1). Ao novo
número assim obtido faz-se o mesmo, e assim sucessivamente, até que se chegue a 1.
Por exemplo:
Se N = 5, teríamos 5 números gerados:
5, 16, 8, 4, 2, 1
Se N = 7, teríamos 16 números gerados:
7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
Agora escreva uma função que recebe o valor N e retorna quantos números são gerados até N chegar
a 1, para testar sua função escreva um programa que lê um número inteiro e chama sua função e no
final imprime o resultado gerado pela função que calcula a sequência de números da conjectura de
Collatz. """


def createConjecturaDeCollatzy(numero):
    listaNumeros = [numero]
    if numero <= 1:
        return listaNumeros
    while numero != 1:
        if numero % 2 == 0:
            numero = numero // 2
            listaNumeros.append(numero)
        elif numero % 2 == 1:
            numero = 3 * numero + 1
            listaNumeros.append(numero)
        else:
            print('Erro! Número inserido não é viável para o cálculo da Conjectura de Collatzy')
    return listaNumeros


def main():
    print("\n*** Conjectura de Collatzy *** \n")
    print("Digite um número inteiro para ser calculado de acordo com aa Conjectura de Collatzy: ")
    numero = int(input("N: "))
    print(createConjecturaDeCollatzy(numero))


if __name__ == "__main__":
    main()
