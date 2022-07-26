# crud_database_python

### História do trabalho:

Nossa empresa foi contratada para modelar um banco de dados para uma companhia de reciclagem de lixo com várias filiais responsáveis por uma única cidade, embora cada cidade possa ser servida por mais de uma filial.  A coleta de material pode ser realizada por meio de um fornecedor ou por caminhões da própria organização. Cada caminhão conta com um motorista e dois garis, e realiza um trecho específico, definido por um ponto de partida e chegada.

Após a coleta e separação, cada tipo de lixo é enviado para uma empresa. Cada empresa é responsável por um único material, contudo cada material pode ser reciclado por mais de uma empresa. Como para cada tipo de lixo existe um processo específico de reciclagem, as empresas operam com diferentes máquinas, para as quais precisamos guardar algumas informações: nome, tipo, valor, descrição, o tipo de material que recicla, ano de compra, e da sua última revisão. O material já reciclado é transportado e vendido como matéria-prima para outras empresas. A organização gostaria de manter as informações dos materiais vendidos nos últimos dez anos.


### Esquema conceitual

![projeto-corrigido](https://user-images.githubusercontent.com/74029052/180698166-da976ec1-5539-4a17-8b08-d7327be274d8.png)

### Esquema lógico relacional

- ColetoresSeparadores(#cpf, nome, fone, nis, rua, bairro, numero, &idfilial,  &placa)
- Maquinas(#idmaq, tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, &idfilial)
- Filiais(#idfilial, nome, fone, rua, numero, bairro, &idcida, &idmate)
- Cidades(#idcida, nome, estado, tam)
- Materiais(#idmate, reciclado, cor, tipo)
- Fornecedores(#cnpjfor, fone, nome, rua, numero, bairro)
- Trechos(#idtrec, partida, chegada, &idcida)
- Caminhoes(#placa, tamanhocarga, &idtre , cpf, nome, fone, nis, rua, bairro, numero, cnh, datacoleta, &idfilial, &idmate)
- Clientes(#cnpjcli, fone, nome, rua, numero, bairro)
- Venda(#&idmate, #&cnpjcli, dataven, #qtdmaterial)
- Compra(#&idmate, #&cnpjfor, datacom, #qtdmaterial)
