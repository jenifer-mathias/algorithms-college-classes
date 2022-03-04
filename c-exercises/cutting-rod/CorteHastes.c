/** Solução ingênua para o problema da haste */

#include <stdio.h>
#include <limits.h>

#define HASTE_SEM_CORTES 0

int max;

int cortaHaste(int preco[], int tamanhoCorteHaste) {
    if (tamanhoCorteHaste == HASTE_SEM_CORTES) {                 /** Não houve cortes na haste */
        return HASTE_SEM_CORTES;
    } else {
        int maiorPreco = INT_MIN;                                /** Representação de menos infinito */
        for (int i = 0; i < tamanhoCorteHaste; i++) {
            int novoPreco = (preco[i] + cortaHaste(preco, tamanhoCorteHaste - i - 1));
            if (maiorPreco > novoPreco) {
                max = maiorPreco;
            } else max = novoPreco;
        }
        return max;
    }
}

int main() {
    int preco[] = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};           /** Exemplo da aula */
    printf("\n**** Corte da haste - solução ingênua ****\n");
    printf("\nMelhor preço de acordo com o corte da haste: R$ %.2f\n", (float) cortaHaste(preco, 10));
}