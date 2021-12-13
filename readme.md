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
https://dkanvas.herokuapp.com/


# deseja consumir a API ? segue abaixo todos os endpoints:

## 2 - USUÁRIO

### 2.1 - Cadastrar

#### 2.1.1 - Aluno

#### POST - ```https://dkanvas.herokuapp.com/api/accounts/```
```json
// BODY REQUEST
{
    "username": "Student",
    "password": "1234",
    "is_superuser": false, 
    "is_staff": false 
}
    
```
#### 2.1.2 - Facilitador

#### POST - ```https://dkanvas.herokuapp.com/api/accounts/```
```json
// BODY REQUEST
{
    "username": "Facilitator",
    "password": "1234",
    "is_superuser": false, 
    "is_staff": true 
}
    
```

#### 2.1.3 - Instructor

#### POST - ```https://dkanvas.herokuapp.com/api/accounts/```
```json
// BODY REQUEST
{
    "username": "Instructor",
    "password": "1234",
    "is_superuser": true, 
    "is_staff": true 
}
    
```

```json
// RESPONSE STATUS -> HTTP 201
{
    "id": 1,
    "username": "Student",
    "is_superuser": false,
    "is_staff": false
}
```

### 2.2 - Login

#### POST - ```https://dkanvas.herokuapp.com/api/login/```
```json
// BODY REQUEST
{
    "username": "Student",
    "password": "1234"
}
    
```

```json
// RESPONSE STATUS -> HTTP 200
{
    "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```

## 3 - CURSO

### 3.1 - Cadastrar (somente instrutor )

#### POST - ```https://dkanvas.herokuapp.com/api/courses/```
```json
// BODY REQUEST
{
    "name": "Node"
}
    
```

```json
// RESPONSE STATUS -> HTTP 201
{
    "id": 1,
    "name": "Node",
    "users": []
}
```

### 3.2 - Listar cursos e alunos matriculdos
#### GET - ```https://dkanvas.herokuapp.com/api/courses/```

```json
// RESPONSE STATUS -> HTTP 200
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


### 3.3 - Exibir curso por ID

#### GET - ```https://dkanvas.herokuapp.com/api/courses/<int:course_id>/```

```json
// RESPONSE STATUS -> HTTP 200
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

### 3.4 - Editar (somente instrutor)

#### PUT - ```https://dkanvas.herokuapp.com/api/courses/<int:course_id>/```
```json
// BODY REQUEST
{
    "name": "Python Django"
}
    
```

```json
// RESPONSE STATUS -> HTTP 200
{
    "id": 1,
    "name": "Python Django",
    "users": []
}
```

### 3.5 - Excluir (somente instrutor)

#### DELETE - ```https://dkanvas.herokuapp.com/api/courses/<int:course_id>/```
```json
 // RESPONSE STATUS -> HTTP 204 NO CONTENT
```

### 3.6 - Vincular os alunos ao curso (somente instrutor)

#### PUT - ```https://dkanvas.herokuapp.com/api/courses/<int:course_id>/registrations/```
```json
// BODY REQUEST
{
    "user_ids": [3, 4, 5]
}
    
```


```json
// RESPONSE STATUS -> HTTP 200
{
    "id": 1,
    "name": "Node",
    "users": [
        {
        "id": 3,
        "username": "student1"
        },
        {
        "id": 4,
        "username": "student2"
        },
        {
        "id": 5,
        "username": "student3"
        }
    ]
}
```

## 4 - ATIVIDADES

### 4.1 - Criar atividade (somente instrutor ou facilitador )

#### POST - ```https://dkanvas.herokuapp.com/api/activities/```
```json
// BODY REQUEST
{
    "title": "Kenzie Pet",
    "points": 10
}
    
```


```json
// RESPONSE STATUS -> HTTP 201
{
    "id": 1,
    "title": "Kenzie Pet",
    "points": 10,
    "submissions": []
}
```

### 4.2 - Listar atividades com suas submissões (somente instrutor ou facilitador)

#### GET - ```https://dkanvas.herokuapp.com/api/activities/```

```json
// RESPONSE STATUS -> HTTP 200
[
    {
        "id": 1,
        "title": "Kenzie Pet",
        "points": 10,
        "submissions": [
            {
                "id": 1,
                "grade": 10,
                "repo": "http://gitlab.com/kenzie_pet",
                "user_id": 3,
                "activity_id": 1
            }
        ]
    },
    {
        "id": 2,
        "title": "Kanvas",
        "points": 10,
        "submissions": [
            {
                "id": 2,
                "grade": 8,
                "repo": "http://gitlab.com/kanvas",
                "user_id": 4,
                "activity_id": 2
            }
        ]
    }
]
```


### 4.3 - Editar atividade (somente instrutor ou facilitador)

#### PUT - ```https://dkanvas.herokuapp.com/api/activities/<int:activity_id>/```
```json
// BODY REQUEST
{
    "title": "Kenzie DOGS",
    "points": 30
}
    
```

```json
// RESPONSE STATUS -> HTTP 200
{
    "id": 1,
    "title": "Kenzie DOGS",
    "points": 30,
    "submissions": []
}
```

## 5 - SUBMISSÃO

### 5.1 - Aluno entregar atividade(somente aluno)

#### POST - ```https://dkanvas.herokuapp.com/api/activities/<int:activity_id>/submissions/```
```json
// BODY REQUEST
{ 
    "repo": "http://gitlab.com/kenzie_pet"
}
    
```

```json
// RESPONSE STATUS -> HTTP 201
{
    "id": 7,
    "grade": null,
    "repo": "http://gitlab.com/kenzie_pet",
    "user_id": 3,
    "activity_id": 1
}
```

### 5.2 - Editar nota da atividade (somente instrutor ou facilitador)

#### PUT - ```https://dkanvas.herokuapp.com/api/submissions/<int:submission_id>/```
```json
// BODY REQUEST
{
    "grade": 10
}
    
```


```json
// RESPONSE STATUS -> HTTP 200
{
    "id": 3,
    "grade": 10,
    "repo": "http://gitlab.com/kenzie_pet",
    "user_id": 3,
    "activity_id": 1
}
```


### 5.3 - Listar as submissões (estudante só pode ver as próprias submissões, enquanto facilitador ou instrutor pode ver todas) 

#### GET - ```https://dkanvas.herokuapp.com/api/submissions/```

#### 5.3.1 - COMO ESTUDANTES PARA VER APENAS SUAS SUBMISSÕES:

```json
// RESPONSE STATUS -> HTTP 200
[
    {
        "id": 2,
        "grade": 8,
        "repo": "http://gitlab.com/kanvas",
        "user_id": 4,
        "activity_id": 2
    },
    {
        "id": 5,
        "grade": null,
        "repo": "http://gitlab.com/kmdb2",
        "user_id": 4,
        "activity_id": 1
    }
]
```

#### 5.3.2 - COMO INSTRUTORES OU FACILITADORES PARA VER TODAS AS SUBMISSÕES:

#### GET - ```https://dkanvas.herokuapp.com/api/submissions/```
```json
// RESPONSE STATUS -> HTTP 200
[
    {
        "id": 1,
        "grade": 10,
        "repo": "http://gitlab.com/kenzie_pet",
        "user_id": 3,
        "activity_id": 1
    },
    {
        "id": 2,
        "grade": 8,
        "repo": "http://gitlab.com/kanvas",
        "user_id": 4,
        "activity_id": 2
    },
    {
        "id": 3,
        "grade": 4,
        "repo": "http://gitlab.com/kmdb",
        "user_id": 5,
        "activity_id": 3
    },
    {
        "id": 4,
        "grade": null,
        "repo": "http://gitlab.com/kmdb2",
        "user_id": 5,
        "activity_id": 3
    }
]
```

## 6 - EXCEÇÕES

### 6.1 - Recursos especificos que pedem ID (Ex: foi solicitado um curso que não existe)
```json
// RESPONSE STATUS -> HTTP 404 Not Found
{
   "error": "course does not exist"
}
```
### 6.2 - Cadastrar um recurso que já existe (Ex: tentativa de cadastrar usuário já cadastrado)
```json
// RESPONSE STATUS -> HTTP 409 - Conflict
{
    "error": "user already exists"
}
```

### 6.3 - Autorização, baseado no tipo de usuário 

#### 6.3.1 - Realizar login em uma conta ainda não criada
```json
// RESPONSE STATUS -> HTTP 401 - Unauthorized
{
    "error": "Incorrect login or password"
}
```
#### 6.3.2  - Token inexistente
```json
// RESPONSE STATUS -> HTTP 401 - Unauthorized
{
  "detail": "Authentication credentials were not provided."
}
```

#### 6.3.3  - Token inválido
```json
// RESPONSE STATUS -> HTTP 401 - Unauthorized
{
    "detail": "Invalid token."
}
```
#### 6.3.4 - Token válido, porém não atende os requisitos mínimos de permissão(ex: aluno tentando criar curso)
```json
// RESPONSE STATUS -> HTTP 403
{
    "detail": "You do not have permission to perform this action."
}
```

### 6.4 - Formato de requisição incorreta (ex: ao tentar realizar o login, o usuário não informou o username)
```json
// RESPONSE STATUS -> HTTP 400 - Bad Request
{
    "error": "is missing 'username'"
}
```

### 6.5 - a atividade que algum aluno tenha feito uma submissão não pode sofrer alteração no nome ou na pontuação
```json
// RESPONSE STATUS -> HTTP 400 Bad Request
{
   "error": "You can not change an Activity with submissions"
}
```



