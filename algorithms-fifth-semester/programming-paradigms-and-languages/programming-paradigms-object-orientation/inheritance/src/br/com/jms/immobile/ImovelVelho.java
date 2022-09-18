package br.com.jms.immobile;

public class ImovelVelho extends Imovel {
    Double desconto;

    public ImovelVelho(String endereco, Double preco, Double desconto) {
        super(endereco, preco);
        this.desconto = desconto;
    }

    public Double calcularPreco() {
        return preco - desconto;
    }
}
