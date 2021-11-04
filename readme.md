# KANVAS
um sistema voltado para o ensino. É possível cadastrar estudantes, facilitadores e instrutores, proporcionando aos estudantes cursos e atividades. Nesse sistema o aluno encontra aulas em formato escrito e por videos proporcionadas pelos instrutores e com auxilio dos facilitadores, atividades para praticar o que aprendeu para assimilar e é possível enviar essas atividades para a correção do time de ensino, recebendo depois todo o feedback sobre seu desempenho.


## 1 - Como rodar o projeto ? entre no terminal e siga o passo a passo abaixo:

#### 1.1 - Faça o clone do repositório:
``` git clone git@gitlab.com:diogo__.py/kanvas.git ``` <br />
ou <br />
``` https://gitlab.com/diogo__.py/kanvas.git ``` 

#### 1.2 - entre no diretório do repositório clonado:
``` cd kanvas ``` 

#### 1.3 - crie um ambiente virtual:
``` python -m venv venv``` 

#### 1.4 - ative ambiente virtual (você sempre vai trabalhar nesse ambiente):
``` source venv/bin/activate``` 

#### 1.5 - uma vez dentro do ambiente virtual, instale as dependências:
``` pip install -r requirements.txt```

#### 1.6 - com os 2 próximos comandos, rode as migrations (para criar as tabelas no banco de dados interno):
``` python manage.py makemigrations ``` <br /><br />
```  python manage.py migrate ```

#### 1.7 - por fim, inicie o servidor para rodar o projeto:
``` python manage.py runserver ```
##### 1.7.1 - se todos os passos foram bem executados, seu projeto vai rodar localmente no seguinte endereço:
http://127.0.0.1:8000/


## 2 - Consumindo a API, segue abaixo todas as rotas/endpoints da aplicação

### 2.1 - Cadastrar usuário

#### POST /api/accounts/
```json
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
    
```
RESPONSE STATUS -> HTTP 201

```json
{
    "id": 1,
    "username": "student",
    "is_superuser": false,
    "is_staff": false
}
```


### 2.2 - Realizar Login do usuário

#### POST /api/login/
```json
{
    "username": "student",
    "password": "1234"
}
    
```
RESPONSE STATUS -> HTTP 200

```json
{
    "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```


### 2.3 - Criar curso (somente instrutor )

#### POST /api/courses/
```json
{
    "name": "Node"
}
    
```
RESPONSE STATUS -> HTTP 201

```json
{
    "id": 1,
    "name": "Node",
    "users": []
}
```


### 2.4 - Listar cursos e alunos matriculdos
#### GET /api/courses/

RESPONSE STATUS -> HTTP 200

```json
[
    {
        "id": 1,
        "name": "Node",
        "users": [
            {
                "id": 3,
                "username": "student1"
            }
        ]
    },
    {
        "id": 2,
        "name": "Django",
        "users": []
    },
    {
        "id": 3,
        "name": "React",
        "users": []
    }
]
```


### 2.5 - Exibir curso por ID

#### GET /api/courses/<int:course_id>/

RESPONSE STATUS -> HTTP 200

```json
{
    "id": 1,
    "name": "Node",
    "users": [
        {
            "id": 3,
            "username": "student1"
        }
    ]
}
```


### 2.6 - Editar curso (somente instrutor)

#### PUT /api/courses/<int:course_id>/
```json
{
    "name": "Python Django"
}
    
```
RESPONSE STATUS -> HTTP 200

```json
{
    "id": 1,
    "name": "Python Django",
    "users": []
}
```


### 2.7 - Excluir curso (somente instrutor)

#### POST /api/accounts/
```json
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
    
```
RESPONSE STATUS -> HTTP 201

```json
{
    "id": 1,
    "username": "student",
    "is_superuser": false,
    "is_staff": false
}
```


### 2.8 - Vincular os alunos ao curso (somente instrutor)

#### POST /api/accounts/
```json
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
    
```
RESPONSE STATUS -> HTTP 201

```json
{
    "id": 1,
    "username": "student",
    "is_superuser": false,
    "is_staff": false
}
```


### 2.9 - Criar atividade (somente instrutor ou facilitador )

#### POST /api/accounts/
```json
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
    
```
RESPONSE STATUS -> HTTP 201

```json
{
    "id": 1,
    "username": "student",
    "is_superuser": false,
    "is_staff": false
}
```


### 2.10 - Listar atividades com suas submissões (somente instrutor ou facilitador)

#### POST /api/accounts/
```json
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
    
```
RESPONSE STATUS -> HTTP 201

```json
{
    "id": 1,
    "username": "student",
    "is_superuser": false,
    "is_staff": false
}
```


### 2.11 - Editar atividade (somente instrutor ou facilitador)

#### POST /api/accounts/
```json
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
    
```
RESPONSE STATUS -> HTTP 201

```json
{
    "id": 1,
    "username": "student",
    "is_superuser": false,
    "is_staff": false
}
```


### 2.12 - Submeter uma atividade (somente estudante)

#### POST /api/accounts/
```json
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
    
```
RESPONSE STATUS -> HTTP 201

```json
{
    "id": 1,
    "username": "student",
    "is_superuser": false,
    "is_staff": false
}
```


### 2.13 - Editar nota da atividade (somente instrutor ou facilitador)

#### POST /api/accounts/
```json
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
    
```
RESPONSE STATUS -> HTTP 201

```json
{
    "id": 1,
    "username": "student",
    "is_superuser": false,
    "is_staff": false
}
```


### 2.14 - LIstar as submissões (estudante só pode ver as próprias submissões, enquanto facilitador ou instrutor pode ver todas)

#### POST /api/accounts/
```json
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
    
```
RESPONSE STATUS -> HTTP 201

```json
{
    "id": 1,
    "username": "student",
    "is_superuser": false,
    "is_staff": false
}
```