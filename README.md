## Descrição
Este projeto visa a manipulação de dados em formato JSON e a integração com APIs, oferecendo um sistema para gerenciar informações sobre restaurantes. Os usuários podem cadastrar restaurantes, avaliar suas experiências e visualizar o cardápio, que inclui bebidas e pratos.

## Estrutura do Projeto
O projeto é organizado da seguinte forma:
projeto/ │ ├── modelos/ │ ├── pycache/ │ ├── avaliacao.py │ └── cardapio/ │ ├── init.py │ ├── bebida.py │ ├── item_cardapio.py │ └── prato.py │ └── app.py

## Tecnologias Utilizadas
- Python
- Programação Orientada a Objetos
- Estruturas de Dados
- Manipulação de Arquivos JSON
- Integração com APIs

### Componentes Principais

- **restaurante.py**: Define a classe `Restaurante`, que representa um restaurante e suas características, incluindo nome, categoria e avaliações. Permite a adição de itens ao cardápio e a exibição das avaliações.

- **avaliacao.py**: Define a classe `Avaliacao`, que armazena informações sobre o cliente e a nota atribuída ao restaurante.

- **cardapio/**: Contém as classes `Bebida` e `Prato`, que herdam de `ItemCardapio` e representam os itens do cardápio.

  - **item_cardapio.py**: Define a classe abstrata `ItemCardapio`, que serve como base para itens do cardápio, definindo um método para aplicar desconto.

  - **bebida.py**: Implementa a classe `Bebida`, que representa uma bebida no cardápio e permite aplicar um desconto.

  - **prato.py**: Implementa a classe `Prato`, que representa um prato no cardápio e também permite aplicar um desconto.

- **app.py**: O ponto de entrada do aplicativo, onde instâncias de restaurantes, bebidas e pratos são criadas e interagem.

## Como Executar o Projeto

1. Clone o repositório:

git clone https://github.com/eltonJramc/Gestao-de-Dados-JSON-APIs-POO.git

2. Navegue até o diretório do projeto:

cd Manipula-o-de-Dados-JSON-e-APIs

3. Execute o código:

python app.py




