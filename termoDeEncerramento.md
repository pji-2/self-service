# TERMO DE ENCERRAMENTO
Termo de Encerramento do Projeto |     |
:--------------: |:------------:
|Serviço de autoatendimento para lojas de varejo |    |


## **Objetivos do projeto** <br />
Implementar serviço de autoatendimento em lojas de varejo utilizando a tecnologia RFID para identificação dos produtos.

## **Planejado x Realizado**
Inicialmente a proposta era que um módulo RFID fizesse a leitra de diversas tags simultaneamente e que um processo executando em um microcontroladr contabilizasse os produtos obtendo as informações necessárias a partir de um banco de dados. <br />

Nesse cenário o cliente passaria uma cesta contendo todos os produtos, 
se autenticaria no sistema e realizaria o pagamento via um sistema pré pago. <br />

Contudo a implementaçao da leitura de diversas tags simultaneamente não ocorreu devido inviabilidade da tecnologia
das tags utilizadas, sendo assim as tags são lidas separadamente o que descaracterizou 
a proposta inicial de um atendimento mais ágil. <br />

Todavia, a computação é realizada em um microcontrolador e os dados de autenticação e produtos foram alocados 
em um sistema em nuvem mantendo a proposta inicial. <br />

### **Objetivos atingidos** <br />
Os objetivos foram parcialmente atingidos. O sistema entregue é funcional, 
entretanto a leitura das tags não é realizada em conjunto. <br />

### **Entregue no prazo** <br />
O projeto foi entregue no dia 05/12/19 e dentro do prazo previsto. <br />

## **Projeto** <br />
O projeto dispõe um código RFID para cada produto e estes são computados por um sistema que calcula a quantia e o valor de cada produto apresentando em tela a lista de produtos e o valor final da compra. O pagamento final é realizado através de um processo de validação do usuário, que conta com um sistema pré-pago. <br />

### **Pontos fortes** <br />
- Realiza a leitura das tags em distâncias médias.
- O sistema é descentralizado com o banco de dados implementado em nuvem.
- Possui interface gráfica.
- Possui backup do banco de dados em nuvem.

### **Pontos fracos** <br />
- Realiza a leitura de uma tag por vez.
- A alimentação do sistema não é portátil.
- É necessário a reinicialização do sistema após a finalização da venda.

## **Recomendações a serem adotadas para os próximos projeto** <br />
- Pesquisar sobre a compatibilidade entre as tecnologias utilizadas no projeto.
- Restringir o projeto apenas a conteúdos já estudados anteriormente.
- Melhor definição das diretrizes do projeto.


