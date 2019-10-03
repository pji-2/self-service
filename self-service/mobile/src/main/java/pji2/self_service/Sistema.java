package pji2.self_service;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class Sistema extends AppCompatActivity {

    private static final String VERSAO = "1.0";
    private static final String NOMEPROJETO = "Self-Service";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sistema);
    }

    public void atender(){ }

    public boolean autenticar(){ return false; }

    public void concluirVenda() { }

    public void cancelarVenda() { }

}
