package pji2.self_service;

public class Cliente {
    private String nome;
    private String cpf;
    private String senha;
    private float saldo;

    public Cliente(String nome, String cpf, String senha, float saldo) {
        this.nome = nome;
        this.cpf = cpf;
        this.senha = senha;
        this.saldo = saldo;
    }

    public String getNome() {
        return nome;
    }

    public String getCpf() {
        return cpf;
    }

    public float getSaldo() {
        return saldo;
    }

}
