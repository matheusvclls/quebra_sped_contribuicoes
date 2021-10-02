# Parsing SPED-Contribuições

### Índice

1. [Instalação](#installation)
2. [Instrução](#instruction)
3. [Motivação do Projeto](#motivation)
4. [Estrutura dos arquivos](#files)
5. [Resultados](#results)
6. [Licença, Autores e Agradecimentos](#licensing)


## Instalação <a name="installation"></a>

Todas as bibliotecas necessárias para executar o aplicativo estão listadas no arquivo required.txt.
Para instalar essas bibliotecas, execute este comando apenas com Python 3 no caminho raiz:

```
$ pip install -r requirements.txt
```


## Instrução <a name="instruction"></a>

1. Insira os arquivos SPEDs a serem quebrados na pasta data > input

2. Execute a instrução abaixo no diretório app do projeto:

```
python app.py
```


## Motivação do Projeto<a name="motivation"></a>

Esse projeto tem o intuito de exemplificar a utilidade da linguagem python na rotina fiscal. Para isso, foi utilizado o SPED Contribuições para quebrar os blocos F100 e 0000.


## Estrutura dos arquivos <a name="files"></a>
<pre>
<code>.
├── <b>README.md</b>
├── <b>app</b> : Pasta da aplicação para quebrar o SPED
│ ├── <b>app.py</b> : Aplicativo para quebrar a obrigação acessória
├── <b>data</b> : Pasta de com as bases de dados 
│ ├── <b>input</b> :  Pasta para armazenar todos os SPEDs a serem quebrados 
│ ├── <b>output</b> :  Pasta para armazenar o resultado com todos os SPEDs quebrados, em formato .csv
└── <b>requirements.txt</b>
 </code>
</pre>


## Resultados<a name="results"></a>

As principais conclusões do código podem ser encontradas no post disponível [aqui] (https://fugimura.medium.com/quebra-de-speds-com-python-79d9648b3772).


## Licença, Autores e Agradecimentos<a name="licensing"></a>

Projeto desenvolvido por Feliphe Fugimura (@fugimurasa) e Matheus Vasconcellos (@matheusvclls). Código aberto para desenvolvimento e aprimoramento.