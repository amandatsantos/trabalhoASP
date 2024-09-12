# Trabalho ASP - Sistema de Locação de Carros

## Descrição do Projeto

O **Trabalho ASP** é um sistema de locação de carros desenvolvido para gerenciar o processo de reserva e locação de veículos. O sistema oferece funcionalidades para cadastro e login de usuários, reserva de carros, visualização de reservas e confirmação de reservas. A aplicação é baseada em Django e utiliza MySQL para o armazenamento de dados.

## Funcionalidades

- **Cadastro de Usuários**: Permite que novos usuários se registrem no sistema.
- **Login e Logout**: Funcionalidades para autenticação de usuários.
- **Reserva de Carros**: Usuários podem reservar carros disponíveis para um período específico.
- **Visualização de Reservas**: Usuários podem visualizar suas reservas realizadas.
- **Confirmação de Reserva**: Após a reserva, um aviso é mostrado ao usuário sobre a necessidade de comparecer à locadora com os documentos necessários.

## Tecnologias Utilizadas

- **Django**: Framework web para desenvolvimento do backend.
- **MySQL**: Sistema de gerenciamento de banco de dados.
- **Bootstrap**: Framework para desenvolvimento de front-end responsivo.
- **jQuery**: Biblioteca JavaScript para manipulação do DOM e realização de requisições AJAX.

## Estrutura do Projeto

O projeto segue a arquitetura Model-View-Controller (MVC) e está organizado da seguinte forma:

- **models.py**: Define os modelos de dados para Carro e Reserva.
- **views.py**: Contém as funções que manipulam as requisições e renderizam os templates.
- **urls.py**: Define as rotas da aplicação.
- **templates/**: Contém os arquivos HTML para a interface do usuário.
- **static/**: Contém arquivos estáticos como CSS e JavaScript.

## Instalação

Para configurar o projeto em sua máquina local, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/usuario/trabalhoASP.git
    ```

2. Navegue para o diretório do projeto:
    ```bash
    cd trabalhoASP
    ```

3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv env
    source env/bin/activate  # No Windows: env\Scripts\activate
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Configure o banco de dados no arquivo `settings.py` e execute as migrações:
    ```bash
    python manage.py migrate
    ```

6. Crie um superusuário para acessar o admin do Django:
    ```bash
    python manage.py createsuperuser
    ```

7. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Uso

1. Acesse a aplicação através do navegador em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
2. Navegue para as páginas de cadastro, login, reserva e visualização de reservas conforme necessário.

## Contribuições

Se você deseja contribuir para o projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção:
    ```bash
    git checkout -b minha-feature
    ```
3. Faça suas alterações e commit:
    ```bash
    git commit -am 'Adiciona nova funcionalidade'
    ```
4. Envie suas alterações:
    ```bash
    git push origin minha-feature
    ```
5. Abra um pull request para a branch principal do repositório.

## Contato

- **E-mail**: [tavaresamandasantos@hotmail.com](mailto:tavaresamandasantos@hotmail.com)

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
