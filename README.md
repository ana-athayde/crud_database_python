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

![1](https://user-images.githubusercontent.com/74029052/180779159-409f6d85-d403-4a94-8c1e-541c08cd8042.png)
![2](https://user-images.githubusercontent.com/74029052/180779196-a61889b1-11bf-4d55-b05c-97a7fad7be16.png)
![3](https://user-images.githubusercontent.com/74029052/180779210-6d0b8d25-8b3b-49f6-96e8-4ba55dc0d6a7.png)
![4](https://user-images.githubusercontent.com/74029052/180779220-f45093d1-d527-4560-984c-544494756b6e.png)
![5](https://user-images.githubusercontent.com/74029052/180779284-7f32c2b4-dfa0-4bde-a88a-ed1bce5a8364.png)
![6](https://user-images.githubusercontent.com/74029052/180779299-d93cd045-5953-4d6d-834a-e9e231e8f1d9.png)
![7](https://user-images.githubusercontent.com/74029052/180779311-85d78407-5ed3-4148-85a4-e9941320425b.png)
![8 1](https://user-images.githubusercontent.com/74029052/180779329-9e707abd-861f-48d5-9d03-8f0f3fe4c3a5.png)
![8 2](https://user-images.githubusercontent.com/74029052/180779347-e67de159-7b76-4330-945f-43a331e505eb.png)
![9](https://user-images.githubusercontent.com/74029052/180779365-9def0dc7-0394-440d-82e9-ba893b70ab12.png)
![10](https://user-images.githubusercontent.com/74029052/180779380-227845fd-6af7-4ee1-afe0-8c8e6cf36140.png)
![11](https://user-images.githubusercontent.com/74029052/180779394-fa515999-8a4a-4120-9d03-7b04082d4546.png)
