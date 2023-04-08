# OnColo - API

_Substitua esse parágrafo por uma breve  descrição do produto a ser desenvolvido, destacando quais problemas resolve ou quais vantagens apresenta_.

### Autoria
* __Professor(a) Correspondente__: Ricardo Salgueiro
* Tiago Plácido (PO)
* Debora (professora)
* Edilaynee (professora) 
* Any Caroliny Sousa Silva
* Arthur
* Marcel
* Leticia Cena
* Paulo Ricardo
* Rafael Vinicius Sousa
### Arquitetura

* Linguagem: Python
* Framework: Django e Django reste framework

### MVP

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

Para instalação do software é necessário:
* Python 3.10
* Django 4.1.7
* django cors headers 3.14.0
* djangorestframework 3.14.0
* pytz 2022.7.1
* sqlparse 0.4.3
* tzdata 2022.7
* django filter 22.1
* validate docbr 1.10.0


### 🔧 Instalação

1. Clone o repositório:
```
> git clone https://github.com/DCOMP-UFS/2022-2-praticas-projetoinca.git
```

2. Crie um ambiente virtual:
```
> python -m venv venv
```

3. Ative o ambiente virtual:
```
> venv/Scripts/activate
```

4. Instale as dependências:
```
> pip install -r requisitos.txt
```

6. Execute as migrações:
```
> python manage.py makemigrations
> python manage.py migrate
```

5. Execute o servidor:
```
> python manage.py runserver
```

## ⚙️ Executando os testes

Para executar os testes automatizados deste sistema, você pode seguir os seguintes passos:

1. Ative o ambiente virtual:
```
> venv/Scripts/activate
```

2. Execute o seguinte comando para executar todos os testes automatizados:
```
python manage.py test
```

### 🔩 Analise os testes de ponta a ponta

Os testes de ponta a ponta (end-to-end) são testes que verificam se todo o sistema funciona corretamente, do início ao fim. Eles testam a interação de diferentes partes do sistema, incluindo a API, banco de dados e interface do usuário. Alguns exemplos de testes de ponta a ponta incluir:

* Testes para verificar se a API retorna os resultados corretos com base em diferentes entradas de usuário
* Testes para verificar se a integração com o banco de dados funciona corretamente
* Testes para verificar se a interface do usuário se comporta corretamente quando interagindo com a API

### ⌨️ E testes de estilo de codificação

Os testes de estilo de codificação (code style tests) verificam se o código segue as convenções de estilo e formatação de código definidas pela equipe de desenvolvimento. Eles ajudam a garantir que o código seja legível e consistente em todo o projeto. Alguns exemplos de testes de estilo de codificação para o seu projeto podem incluir:

* Testes para verificar se a indentação do código está correta
* Testes para verificar se a nomenclatura de variáveis e funções está em conformidade com as diretrizes do projeto
* Testes para verificar se a documentação do código está completa e precisa

## 📦 Implantação

Adicione notas adicionais sobre como implantar isso em um sistema ativo

## 🛠️ Construído com

* [Django](https://docs.djangoproject.com/en/4.1/) - O framework web usado
* [MySQL](https://dev.mysql.com/doc/) - Banco de dados usado


## 📌 Versão

Nós usamos [Git](https://git-scm.com//) para controle de versão.

## API

#### Visão Geral
Esta API permite aos usuários fazerem CRUD (Create, Retrieve, Update e Delete) de pacientes, fisioterapeutas, instituições e administradores.

#### Endpoints
##### GET /paciente
Retorna uma lista de todas as pacientes.

Exemplo de resposta:
~~~JSON
[
    {
        "id": 4,
        "matricula": "98239",
        "nome": "Cintia",
        "sobrenome": "Ferreira",
        "altura": 1.6,
        "peso": 70.0,
        "imc": 23.0
    },
    {
        "id": 5,
        "matricula": "645445",
        "nome": "Fulana",
        "sobrenome": "Detal",
        "altura": 1.7,
        "peso": 80.0,
        "imc": 21.0
    },
    {
        "id": 6,
        "matricula": "94239",
        "nome": "Maria",
        "sobrenome": "José",
        "altura": 1.65,
        "peso": 50.0,
        "imc": 20.0
    }
]
~~~
##### POST paciente/
Cria uma nova paciente.

Parâmetros de requisição:

matricula - matricula da paciente,
nome - Nome da paciente,
sobrenome - Sobrenome da paciente,
altura - Altura da paciente,
peso - Peso da paciente,
imc - IMC da paciente

Exemplo de corpo da requisição:
~~~JSON
{
    "matricula": "98239",
    "nome": "Cintia",
    "sobrenome": "Ferreira",
    "altura": 1.6,
    "peso": 70.0,
    "imc": 23.0
}
~~~
Exemplo de resposta:
~~~JSON
{
    "id": 3,
    "matricula": "98239",
    "nome": "Cintia",
    "sobrenome": "Ferreira",
    "altura": 1.6,
    "peso": 70.0,
    "imc": 23.0
}
~~~

##### PUT paciente/{id}/
Atualiza uma paciente existente.

Parâmetros de requisição
matricula - matricula da paciente
nome - Nome da paciente.
sobrenome - Sobrenome da paciente
altura - Altura da paciente.
peso - Peso da paciente.
imc - IMC da paciente

Exemplo de corpo da requisição:

~~~JSON
{
    "matricula": "98239",
    "nome": "Cintia",
    "sobrenome": "Ferreira",
    "altura": 1.6,
    "peso": 78.0,
    "imc": 23.0
}
~~~

##### DELETE paciente/{id}/
Deleta uma paciente existente.

Exemplo de resposta:

HTTP 202 Accepted

Erros

A API pode retornar os seguintes erros:

400 Bad Request - O corpo da requisição está mal formado ou faltando algum parâmetro obrigatório.
401 Unauthorized - O usuário não está autenticado.
404 Not Found - O recurso solicitado não foi encontrado.
405 Method Not Allowed - O método HTTP não é suportado pelo endpoint solicitado.
500 Internal Server Error - Ocorreu um erro interno no servidor.



