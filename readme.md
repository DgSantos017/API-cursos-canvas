# KANVAS

## 1 - O que é ?
### 1.1 - um sistema voltado para o ensino. É possível cadastrar estudantes, facilitadores e instrutores(todos com permissões de operação diferenciada de acordo com o tipo do usuário), proporcionar aos estudantes cursos e atividades. Nesse sistema o aluno encontra aulas em formato escrito e por videos proporcionadas pelos instrutores e com auxilio dos facilitadores, atividades para praticar o que aprendeu para assimilar e é possível enviar essas atividades para a correção do time de ensino, recebendo depois todo o feedback sobre seu desempenho.


## 2 - Como rodar o projeto ? segue o passo a passo abaixo:

### 2.1 - Faça o clone do repositório, digite no terminal o seguinte comando:
```json git clone git@gitlab.com:diogo__.py/kanvas.git ``` 
ou 
```json https://gitlab.com/diogo__.py/kanvas.git ``` 

### 2.2 - entre no diretório, digite no terminal o seguinte comando:
```json cd kanvas ``` 

### 2.3 - crie um ambiente virtual
```json python -m venv venv``` 

### 2.4 - ative ambiente virtual (voce sempre vai trabalhar dentro desse ambiente)
```json source venv/bin/activate venv``` 

### 2.5 - uma vez dentro do ambiente virtual, instale as dependências
```json pip install -r requirements.txt venv```

### 2.6 - com os 2 próximos comandos, rode as migrations (para criar as tabelas no banco de dados interno)
```json python manage.py makemigrations ```
```json  python manage.py migrate ```

### 2.7 - por fim, inicie o servidor para rodar o projeto
```json python manage.py runserver ```
#### 2.7.1 - se todos os passos foram bem executados, seu projeto vai rodar localmente no seguinte endereço:
http://127.0.0.1:8000/


## 3 - Consumindo a API, segue abaixo todas as rotas/endpoints da aplicação

### 3.1 - Cadastrar usuário
### 3.2 - Realizar Login do usuário
### 3.3 - Criar curso (somente instrutor )
### 3.4 - Listar cursos e alunos matriculdos
### 3.5 - Exibir curso por ID
### 3.6 - Editar curso (somente instrutor)
### 3.7 - Excluir curso (somente instrutor)
### 3.8 - Vincular os alunos ao curso (somente instrutor)
### 3.9 - Criar atividade (somente instrutor ou facilitador )
### 3.10 - Listar atividades com suas submissões (somente instrutor ou facilitador)
### 3.11 - Editar atividade (somente instrutor ou facilitador)
### 3.12 - Submeter uma atividade (somente estudante)
### 3.13 - Editar nota da atividade (somente instrutor ou facilitador)
### 3.14 - LIstar as submissões (estudante só pode ver as próprias submissões, enquanto facilitador ou instrutor pode ver todas)