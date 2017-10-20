# jobs
protótipo de um sistema de vagas de empregos


Versão do python: 2.7
Versão Django: 1.8


Procedimentos para subir em desenvolvimento
-------------------------------------------

1 - git clone https://github.com/ronaldojr/jobs.git  && cd jobs

2 - pip install -r requirements.txt

3 - ./manage.py runserver

4 - Abra o navegador e insira a url: http://127.0.0.1:8000/

Para que o procedimento acima funcione corretamente, é preciso que a versão do python
seja a 2.7. Aconselha-se o uso do virtualenvwrapper para a criação de ambientes
isolados.


Sobre os usuários
-----------------

Existem dois perfis de usuário: Candidato e Empresa.

Para poder utilizar o sistema, o usuário deve primeiro realizar o cadastro,
escolhendo o perfil desejado e em seguida efetuar o login.


Sobre o menu:

- existem links comuns aos dois perfis: início, vagas e logout.

- usuário com perfíl de candidato possui um link "candidaturas", para 
visualizar uma lista com todas as candidaturas realizadas por ele.

- usuário com perfíl de empresa possuí dois links: gerenciar vagas e relatorios. 
Em gerenciar vagas ele cadastra, atualiza e deleta suas vagas. Em relatorios pode
visualizar dados sobre suas vagas em relação as candidaturas.


Candidatura:

- Para o usuario se candidatar a uma vaga, deve acessar a lista de vagas clicando
em "vagas" no menu. Ao selecionar a vaga desejada basta clicar em candidatar-se
e preencher um formulário com as informações necessárias.

- O usuário pode pesquisar por um termo em busca de vagas específicas. Ao acessar
as vagas através do menu "vagas" basta preencher o campo "pesquisar" com
o termo desejado e clicar no botão "pesquisar".








