#include <stdio.h>

int fib[99];      // variável global para armazenar os valores de fib

int fibonacci(int numero) {
    if(numero == 1 || numero == 0) {
        return numero;
    }
    if(fib[numero] != -1) {
        return fib[numero];
    }
    fib[numero] = fibonacci(numero - 1) + fibonacci(numero - 2);
    return fib[numero];
}

void memoizacaoNumeros() {
    for (int i = 0; i < 99; ++i) {
        fib[i] = -1;    // valor inicial para posteriormente guardar os valores de fib em cache
    }
}

int main() {
    memoizacaoNumeros(); // aplicando a técnica de memoização

    printf("**** Fibonacci usando a técnica de memoização ****");
    int numero;
    printf("\nDigite um número inteiro para obter o Fibonacci deste número: ");
    scanf("%i", &numero);
    printf("O Fibonacci de %i é: %i", numero, fibonacci(numero));
}