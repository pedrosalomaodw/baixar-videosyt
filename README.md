<h1>
    Baixar vídeos
</h1>

<br>
<p>Esse é um programa criado em python, utilizando a interface do Tkinter e Pytube que é uma API para baixar os vídeos do YouTube.</p>
<p>Esse foi um projeto um pouco simples e de grande aprendizado, com esse projeto acabei pesquisando e estudando um pouco sobre <a href="https://www.techtudo.com.br/noticias/2019/01/o-que-sao-threads-e-para-que-servem-em-um-processador.ghtml">Threads</a> e melhorando a cada momento a lógica de programação.</p>

## Baixando o programa:

```
git clone https://github.com/pedrosalomaodw/baixar-videosyt
```
<p>Pretendo adicionar mais funcionalidades ao programa, como escolher se vai ser apenas áudio ou vídeos, a qualidade dos vídeos e entre outros, tudo isso será feito a paritir de interações com o Tkinter.
(os Downloads dos vídeos são mandados para a pasta Downloads em seu computador.</p>

<br>

<h2>Como transformei em executável?</h2>
<br>
<p>Meu tio me desafiou em transformar esse pequeno programa em execultável para que ele não precise baixar o Python e as bibliotecas no computador, então acabei aceitando o desafiou
    e descobrindo coisas novas ao decorrer do caminho como o <a href="https://pyinstaller.org/en/stable/">Pyinstaller</a> e entre outros.
</p>

<p>COMO UTILIZEI O PYINSTALLER?</p>
<p>baixando:</p>

```py
pip install pyinstaller
```
<p>transfomrar o programa .py em execultável do seu sistema operacional:</p>

<p>um arquivo</p>

```py
pyinstaller --onefile  nomedoseuarquivo.py
```

