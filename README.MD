# Bear-Api

## Sobre a Aplicação WEB

Para o `front-end`, foram utilizadas as tecnologias `HTML, CSS e JavaScript.` A integração do front-end com o modelo de visão computacional está sendo feita `inteiramente com Flask`.

## Imagens da Aplicação

Página de Seleção de Imagem:

![Imagem da Aplicação](/imagens/api-0.png)

Após selecionar a imagem que deseja classificar entre os `8 tipos de urso disponíveis`, a aplicação retornará para o usuário o nome da espécie (ou se é de pelúcia) e uma breve descrição sobre a espécie. Todas as descrições podem ser encontradas na pasta `“descriptions”`, mas recomendo explorá-las manualmente pela aplicação. 😊

![Imagem da Aplicação](/imagens/api-1.png)

## Como usar

### Clonando o Repositório

Para começar, clone o repositório para a sua máquina utilizando o seguinte comando:
`git clone https://github.com/ErickBonruque/bear-api`

### Configurando uma Máquina Virtual (Opcional)
Recomendo o uso de uma máquina virtual para isolar o ambiente da aplicação. Siga os passos abaixo para configurar uma máquina virtual utilizando o venv:

- Navegue até o diretório do projeto:
`cd bear-api`

- Crie uma máquina virtual (venv):
`python -m venv venv`

- Ative a máquina virtual (Linux/Mac):
`source venv/bin/activate`

- Ative a máquina virtual (Windows):
`venv\Scripts\activate`

### Instalando as Dependências

Dentro da máquina virtual (caso tenha configurado), instale as dependências da aplicação utilizando o comando:
`pip install -r requirements.txt`

### Executando a Aplicação

Agora que as dependências estão instaladas, você pode iniciar a aplicação. Utilize o seguinte comando: 
`python app.py`