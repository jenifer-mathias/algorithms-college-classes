package br.com.jms.car;

public class Carro {
    double quantidadeCombustivel = 0;

    public Carro() {
    }

    public double getQtdCombustivel() {
        return quantidadeCombustivel;
    }

    public void setQtdCombustivel(double quantidadeCombustivel) {
        this.quantidadeCombustivel = quantidadeCombustivel;
    }

    public void adicionarCombustivel(int qtdCombustivel) {
        setQtdCombustivel(getQtdCombustivel() + qtdCombustivel);
    }

    public Double obterCombustivel() {
        return getQtdCombustivel();
    }

    public void andar(int distanciaKm) {
        setQtdCombustivel(getQtdCombustivel() - (distanciaKm * 0.20));
    }
}

class Main {
    public static void main(String[] args) {

        System.out.println("\n* * * * Controla combustível do carro * * * *");

        Carro carro = new Carro();

        carro.adicionarCombustivel(20);

        carro.andar(80);

        System.out.println("\nLitros de combustível no tanque: \n" + carro.obterCombustivel()); // imprime 4.0
    }
}
