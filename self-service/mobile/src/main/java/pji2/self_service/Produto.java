package pji2.self_service;

public class Produto {
    private String nome;
    private int codigo;
    private int quantidade;
    private float valor;

    public Produto(String nome, int codigo, int quantidade, float valor) {
        this.nome = nome;
        this.codigo = codigo;
        this.quantidade = quantidade;
        this.valor = valor;
    }

    public String getNome() {
        return nome;
    }

    public int getCodigo() {
        return codigo;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public float getValor() {
        return valor;
    }

}
