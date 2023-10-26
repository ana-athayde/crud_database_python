# Projeto de Sistema de Gerenciamento - Reciclagem

Este é um projeto de sistema de gerenciamento de reciclagem com um banco de dados MySQL. O sistema permite a gestão de máquinas, filiais, materiais e cidades relacionadas à reciclagem.

## Arquivos do Projeto

- `Cidades.py`: Contém funções para gerenciar cidades, incluindo criação de tabela, inserção, atualização, exclusão e consulta.

- `Conexao.py`: Estabelece a conexão com o banco de dados MySQL e inclui a função para desconectar.

- `Filiais.py`: Implementa funções para gerenciar filiais, como criação de tabela, inserção, atualização, exclusão e consulta.

- `Maquinas.py`: Contém funções relacionadas à gestão de máquinas, incluindo criação de tabela, inserção, atualização, exclusão e consulta.

- `Materiais.py`: Contém funções para gerenciar materiais, incluindo criação de tabela, inserção, atualização, exclusão e consulta.

- `Principal.py`: Este arquivo contém o código principal do sistema, incluindo um menu interativo que permite ao usuário realizar várias operações no banco de dados.

- `projeto_reciclagem.sql`: Script SQL que define a estrutura do banco de dados, incluindo tabelas, relacionamentos e chaves estrangeiras.

## Esquema Lógico Relacional

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


### História do trabalho:

Nossa empresa foi contratada para modelar um banco de dados para uma companhia de reciclagem de lixo com várias filiais responsáveis por uma única cidade, embora cada cidade possa ser servida por mais de uma filial.  A coleta de material pode ser realizada por meio de um fornecedor ou por caminhões da própria organização. Cada caminhão conta com um motorista e dois garis, e realiza um trecho específico, definido por um ponto de partida e chegada.

Após a coleta e separação, cada tipo de lixo é enviado para uma empresa. Cada empresa é responsável por um único material, contudo cada material pode ser reciclado por mais de uma empresa. Como para cada tipo de lixo existe um processo específico de reciclagem, as empresas operam com diferentes máquinas, para as quais precisamos guardar algumas informações: nome, tipo, valor, descrição, o tipo de material que recicla, ano de compra, e da sua última revisão. O material já reciclado é transportado e vendido como matéria-prima para outras empresas. A organização gostaria de manter as informações dos materiais vendidos nos últimos dez anos.


### Esquema conceitual

![projeto-corrigido](https://user-images.githubusercontent.com/74029052/180698166-da976ec1-5539-4a17-8b08-d7327be274d8.png)

## Documentação das Funções

### Cidades.py:
1. `all_cidades()`: Recupera e imprime todas as cidades da tabela de cidades ordenadas pelo ID.
2. `create_table()`: Cria a tabela de cidades no banco de dados.
3. `insert_into(values)`: Insere uma nova cidade na tabela de cidades. Recebe uma lista de valores que incluem o nome, estado e tamanho da cidade.
4. `selec_by_id(id)`: Recupera e imprime a cidade com base no ID especificado. Retorna o número de cidades recuperadas (0 ou 1).
5. `update_table(coluna, valor, id)`: Atualiza um valor específico na tabela de cidades. Recebe o nome da coluna, o novo valor e o ID da cidade a ser atualizada.
6. `delete_row_by_id(id)`: Exclui uma cidade da tabela de cidades, desde que não haja filiais associadas a ela. Recebe o ID da cidade a ser excluída.

### Conexao.py:
1. `connect()`: Estabelece uma conexão com o banco de dados MySQL usando as credenciais fornecidas.
2. `desconectar(my_db)`: Fecha a conexão com o banco de dados. Recebe a conexão como parâmetro.

### Filiais.py:
1. `all_filiais()`: Recupera e imprime todas as filiais da tabela de filiais ordenadas pelo ID.
2. `create_table()`: Cria a tabela de filiais no banco de dados.
3. `insert_into(values)`: Insere uma nova filial na tabela de filiais. Recebe uma lista de valores que incluem nome, telefone, rua, número, bairro, ID da cidade e ID do material.
4. `selec_by_id(id)`: Recupera e imprime a filial com base no ID especificado. Retorna o número de filiais recuperadas (0 ou 1).
5. `update_table(coluna, valor, id)`: Atualiza um valor específico na tabela de filiais. Recebe o nome da coluna, o novo valor e o ID da filial a ser atualizada.
6. `delete_row_by_id(id)`: Exclui uma filial da tabela de filiais, desde que não haja máquinas associadas a ela. Recebe o ID da filial a ser excluída.

### Maquinas.py:
1. `all_maquinas()`: Recupera e imprime todas as máquinas da tabela de máquinas ordenadas pelo ID.
2. `create_table()`: Cria a tabela de máquinas no banco de dados.
3. `insert_into(values)`: Insere uma nova máquina na tabela de máquinas. Recebe uma lista de valores que incluem tipo de material, ano de compra, ano de última revisão, nome, tipo, valor, descrição e ID da filial.
4. `selec_by_id(id)`: Recupera e imprime a máquina com base no ID especificado. Retorna o número de máquinas recuperadas (0 ou 1).
5. `update_table(coluna, valor, id)`: Atualiza um valor específico na tabela de máquinas. Recebe o nome da coluna, o novo valor e o ID da máquina a ser atualizada.
6. `delete_row_by_id(id)`: Exclui uma máquina da tabela de máquinas.

### Materiais.py:
1. `all_materiais()`: Recupera e imprime todos os materiais da tabela de materiais ordenados pelo ID.
2. `create_table()`: Cria a tabela de materiais no banco de dados.
3. `insert_into(values)`: Insere um novo material na tabela de materiais. Recebe uma lista de valores que incluem se é reciclado, cor e tipo.
4. `selec_by_id(id)`: Recupera e imprime o material com base no ID especificado. Retorna o número de materiais recuperados (0 ou 1).
5. `update_table(coluna, valor, id)`: Atualiza um valor específico na tabela de materiais. Recebe o nome da coluna, o novo valor e o ID do material a ser atualizado.
6. `delete_row_by_id(id)`: Exclui um material da tabela de materiais.

### Principal.py:
Este arquivo contém uma série de funções para interagir com o banco de dados, incluindo inserção, atualização, pesquisa, exclusão e impressão de registros em várias tabelas (maquinas, filiais, materiais e cidades). Também inclui funções para realizar operações de junção e agregação de dados nas tabelas. Além disso, há um menu interativo que permite ao usuário selecionar as operações desejadas.


