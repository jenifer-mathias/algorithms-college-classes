package br.com.jms.television;

class Televisao {
    int canal;
    int volume;

    public Televisao() {
        this.volume = 0;
    }

    public int getVolume() {
        return volume;
    }

    public int getCanal() {
        return canal;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }

    public void setCanal(int canal) {
        this.canal = canal;
    }

    public void aumentarVolume() {
        setVolume(getVolume() + 1);
    }

    public void diminuirVolume() {
        setVolume(getVolume() - 1);
    }

    public void alterarCanal(int canal) {
        setCanal(canal);
    }
}

class Main {
    public static void main(String[] args) {

        Televisao tv = new Televisao();

        tv.alterarCanal(6);
        tv.aumentarVolume();
        tv.aumentarVolume();
        tv.aumentarVolume();
        tv.diminuirVolume();

        System.out.println("\n* * * * Controla TV * * * *");

        System.out.printf("\nA TV está no canal %d\n", tv.canal); // A tv está no canal 6

        System.out.printf("\nA TV está no volume %d\n", tv.volume); // A tv está no volume 2
    }
}
