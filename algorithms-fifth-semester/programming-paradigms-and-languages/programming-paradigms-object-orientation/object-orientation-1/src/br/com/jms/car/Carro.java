package br.com.jms.car;

public class Carro {
    float quantidadeCombustivel;

    public Carro() {
        this.quantidadeCombustivel = 0.00f;
    }

    public Float getQtdCombustivel() {
        return quantidadeCombustivel;
    }

    public void setQtdCombustivel(float quantidadeCombustivel) {
        this.quantidadeCombustivel = quantidadeCombustivel;
    }

    public void adicionarCombustivel(float qtdCombustivel) {
        setQtdCombustivel(getQtdCombustivel() + qtdCombustivel);
    }

    public Float obterCombustivel() {
        return getQtdCombustivel();
    }

    public void andar(float distanciaKm) {
        setQtdCombustivel((getQtdCombustivel() - (distanciaKm * 0.20f)));
    }
}

class Main {
    public static void main(String[] args) {

        System.out.println("\n* * * * Controla combustível do carro * * * *");

        Carro carro = new Carro();

        carro.adicionarCombustivel(20.00f);

        carro.andar(80.00f);

        System.out.printf("\nLitros de combustível no tanque: \n%.2f", carro.obterCombustivel());
    }
}
