package pji2.self_service;

import android.text.format.Time;

import java.util.ArrayList;
import java.util.Date;

public class Venda {
    private Cliente cliente;
    private ArrayList<Produto> produtos;
    private Date data;
    private float total;

    public Venda(Date data) {
        this.data = data;
    }

    public void addProduto(Produto produto){
        produtos.add(produto);
        total = this.total + produto.getValor();
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public float getTotal() {
        return total;
    }
}
