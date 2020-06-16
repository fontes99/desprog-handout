Algoritmo Needleman-Wunsch para alinhamento de sequências
==========================

Introdução
---

Com a recém descoberta do DNA, formado por cadeias de aminoácidos com bases
nitrogenadas, Saul Needleman e Christian Wunsch, em 1969, foram atrás de 
solucionar o problema de encontrar similaridades entre estas, o que era
uma necessidade para a área de estudo da genética.

De forma geral, o algoritmo consiste em analisar duas palavras e verificar
quantas mudanças seriam necessárias para tornar uma palavra igual a outra.

Exemplo
---
O algoritmo foi projetado para objetos do tipo *String* e, portanto, podemos
começar entendendo com um exemplo utilizando palavras ao invés de bases
nitrogenadas.

Temos duas palavras muito semelhantes porém diferentes:

    >  _COERENCIA
      OCORRENCIA
      
> Considere o "_" como um espaço vazio na palavra!

Desejamos que elas sejam iguais, para isso precisaremos realizar algumas mudanças.
Manteremos a palavra "*COERENCIA*" como nosso padrão e alteraremos a palavra "*OCORRENCIA*".

Há 2 diferenças nestas palavras:

* Número de caracteres diferentes
* Pelo menos 1 caractere diferente da outra

Também é importante saber que existem 3 ações possíveis que podemos realizar para
alcançar nosso objetivo:

* **Alinhar** um caractere de uma palavra na outra, sinônimo de copiar
* **Inserir** um caractere novo em uma das palavras
* **Remover** um caractere de uma das palavras.

>Observação:

>O alinhamento só conta efetivamente como "ação" se os caracteres forem *diferentes*. 
>Se forem iguais, Alinhar pode ser interpretado como "pular uma ação" já que os caracteres 
>estão devidamente *alinhados*. ***(lembre-se disso, pois usaremos na lógica)***

Dessa forma podemos realizar pequenas e pontuais mudanças. Começaremos deletando o primeiro
caractere de "*OCORRENCIA*", pois como vemos em nossa base, ele não existe, assim temos:

    >  COERENCIA
      CORRENCIA 

Agora percebemos que temos duas palavras muito próximas porém ainda há uma diferença: 
o 3º caractere delas são diferentes. 

Para resolver isto devemos tomar mais uma medida: devemos alinhar, ou "copiar", o "*R*" de "*CORRENCIA*" 
com o "*E*" de "*COERENCIA*". Logo obtemos:

    >  COERENCIA
      COERENCIA

Perceba que as palavras, após 2 alterações, se tornaram iguais.

> Se entendeu minimamente até aqui, pode continuar
> 
> Caso contrário, leia o exemplo novamente.

###

A Lógica do algoritmo
---

Este Algoritmo segue uma lógica em que iremos checar, por meio de uma matriz, 
qual o numero de **ações** que devemos realizar para transformar a substring na 
vertical na substring da horizontal. 

Utilizamos a matriz para checar *TODAS* as **ações** para *TODAS* as substrings 
possiveis.

Vamos ver um exemplo de matriz com duas strings: `'TGCCTAG'` e `'TCCAGT'`

![tabela 1](tabela-1.png)

Você consegue deduzir oque significa cada casa dessa matriz?

###

Numa matriz dessa, cada casa representa quantas ações são 
feitas para transformar a *substring* correspondente da vertical na da horizontal.

Uma substring pode ser vista como toda a string do começo até o caractere da casa que estamos analisando

Nesta tabela temos um exemplo de analise a uma casa da matriz que tem o valor *x*

![substring](substring.png)

As Substrings correspondentes da casa *x* estão pintadas de laranja.

Seguindo o raciocínio, o valor *x* corresponderia a quantas ações são nessessarias para tranformar a substring `'TCCAG'` em `'TGC'`

Agora, como chegamos nesse valor *x*? Vamos entender o preenchimento dessa tabela...

> Só continue se tiver entendido o conceito do valor de cada casa e de substrings

###

Os dois primeiros `'-'` antes de cada string representa... nada!! Isso mesmo, nada.

Tratamos esse primeiro espaço como a substrig `' '` (vazia) e, antes de explicar algo, 
você consegue deduzir quantas ações realizamos para tranformar *nada* em *nada*?

###

Para tranformar nada em nada faremos..... 0 ações!   

Começaremos nossa matriz com primeiro elemento 0.

![tabela 2](tabela-2.png)

O proximo passo é pensar, antes de qualquer coisa, na primeira linha e na primeira coluna.

Ainda antes de explicar a *manha* do algoritmo, você consegue deduzir as casas da matriz da 
primeira linha e primeira coluna?

>DICA: 

>A primeira linha representa quantas ações faremos para tranformar nada em `'T'`, `'TG'`, `'TGC'`, ...
>E podemos ver a coluna com os mesmos olhos.

###

Na primeira linha, temos que **Inserir** (uma ação) cada caractere da substring em nada. Por exemplo, como dito na dica, para inserir `'T'` em nada precisamos de uma ação, para inserir `'TG'` em nada precisamos de duas, para inserir `'TGC'` em nada precisamos de três e assim por diante.

Podemos então deduzir a primeira linha...

![tabela 3](tabela-3.png)

Na primeira coluna, temos que **Deletar** (uma ação) cada caractere da substring para se tornar nada. Por exemplo, para deletar `'T'` para nada precisamos de uma ação, para deletar `'TC'` para nada precisamos de duas, para deletar `'TCC'` para nada precisamos de três e assim por diante.

![tabela 4](tabela-4.png)

Estamos com o terreno arado para começar, de verdade, a lógica do algoritimo!

>Só avance se você entendeu as deduções de linhas e colunas...

###

A *manha* do algoritimo é o seguinte:

Olhando para a a tabela, vamos calcular o valor de uma casa. Representaremos esta casa com *x*.

![abc-gande](abc-grande.png)

Agora, vamos olhar para as casas vizinhas de *x*, representado por *a*, *b* e *c*.

![abc-pequeno](abc-pequeno.png)

Em suma, x vai ser igual a algum dos valores *a*, *b* ou *c* acrescentando o custo de uma ação (1). 
Portanto, x = a+1 ou b+1 ou c+1. 

*Está lembrado das ações que podemos realizar?*

* A escolha de *a* equivale a uma Remoção
* A escolha de *b* equivale a um Alinhamento
* A escolha de *c* equivale a uma Inserção

Ou seja..

* Se escolhermos *a* iremos **remover** o caractére equivalente na horizontal
* Se escolhermos *b* iremos **alinhar** o caractére equivalente na horizontal
* Se escolhermos *c* iremos **inserir** o caractére equivalente na horizontal

*Ressaltando, ao escolher um desses valores, você esta realizando a ação que eles representam também!* Por isso que quando completamos a primeira coluna nós deletamos e para a primeira linha inserimos.

Agora... Qual escolher?

Tente deduzir qual seria o melhor.

>DICA:

>Tente lembrar do significado dos numeros das casas...

###

Queremos seguir uma linha que representa o menor numero de ações que faremos não é mesmo? então o melhor 
valor para se escolher é o *MENOR* valor

Para ficar mais facil, vamos representar em *pseudo-código*

    var x = min(a, b, c) + 1

Mas ainda não acabou! temos mais um passo para ser feito... (lembra da observação acima?)

Para que possamos adicionar uma ação (+1), teremos que, efetivamente, realizar uma ação, certo? Portanto, 
no caso da escolha de *alinhamento*, antes de somar 1, devemos comparar os caractéres equivalentes e ver se são iguais! 
Se não forem, não realizaremos nenhuma ação e o numero que somaremos não será um, mas sim 0!

corrigindo o *pseudo-código* acima:

    var x = min(a, b, c) + (min(a, b, c) == b ? (char1 == char2 ? 0 : 1) : 1)                


Vamos agora completar nossa tabela!

Clique [aqui](https://docs.google.com/document/d/1mMImN8eiCP9Jdz8oxio1HhodbmrJ53stkSBG6Xdfv1Y/edit?usp=sharing) para ter acesso a um *template* da tabela. Baixe-o (ou faça uma cópia em "Arquivo" no canto superior esquerdo) para realizar a próxima parte.

>Só continue se entendeu a lógica

###

Vamos separar nosso preenchimento de cada casa em somente 2 passos:

1. Olhar para a vizinhança a, b e c (como explicado anteriormente) e escolher o menor valor
   
2. No caso de escolher *b*, checar os caractéres equivalentes e adicionar 1 se forem diferentes ou 0 se forem iguais 

Vamos por em pratica a última parte que vimos voltando na matriz pronta para ser preenchida.

![tabela 4](tabela-4.png)

Neste caso, temos 1, 0 e 1 para escolhermos. Vamos escolher o menor (0) e, ja que os caractéres são iguais, adicionar 0.

![tabela 5](tabela-5.png)

Essa proxima linha interia pode ser deduzida rapidamente pois queremos adicionar as substrings somente em `'T'`

![tabela 6](tabela-6.png)

Continuando, temos agora 2, 1, e 0 sendo que o valor escolido foi *c*. Portanto apenas somamos 1

![tabela 7](tabela-7.png)

Aqui temos um caso parecido com o inicial, mas dessa vez com caractéres diferentes. Portanto, somamos 1

![tabela 8](tabela-8.png)

Agora temos um caso de impate! oque faremos agora... 

Basta escolher o que nos resultará em um menor número! Neste caso, temos 1 e 1 no valor a e b com caracteres *iguais*. 
Portanto, o melhor a ser escolido é *b* porque não somaremos 1 no final

![tabela 9](tabela-9.png)

Agora é sua vez! Tente completar a tabela.

>Não continue sem esclarecer suas dúvidas

###

Se tudo deu certo, você chegou em uma tabela igual (ou pelomenos parecida) com essa:

![tabela 0](tabela-0.png)

Com ela preenchida, se repararmos no ultimo valor da matriz...

![tabela 11](tabela-11.png)

... ele representa o numero de ações que tomamos para transformar toda a string da horizontal na string da vertical!

Só nos resta uma coisa! Saber quais foram as ações e onde elas ocorreram.

Para isso, vamos desenhar uma linha guia começando do ultimo elemento e ligando o menor numero subsequente da casa atual. Em suma, estamos apontando para a origem da casa atual e traçando o caminho pelo qual foi percorrido para chegar no resultado.

![tabela 12](tabela-12.png)

Agora... Está lembrando da representação de cada movimento das ações? o que as casas *a*, *b* e *c* representavam? Quando escolhemos o menor numero entre *a*, *b* e *c*, estamos escolhendo a ação que eles representma também.
 
Volte nas listas da *manha* do algoítmo caso não lembre..

Lemos essa linha do primeiro ítem da matriz para o último (sentido contrário do qual desenhamos) e seguimos as representações de cada movimento.

Concluindo:
---

Na string `'TCCAGT'` nós:

* Alinhamos T -> `'TCCAGT'` (continua igual em alinhamentos com caracteres iguais)
* Inserimos G -> `'TGCCAGT'`
* Alinhamos C -> `'TGCCAGT'`
* Alinhamos C -> `'TGCCAGT'` 
* Inserimos T -> `'TGCCTAGT'` 
* Alinhamos A -> `'TGCCTAGT'` 
* Alinhamos G -> `'TGCCTAGT'`
* Removemos T -> `'TGCCTAG'` 
 
Transformamos a string `'TCCAGT'` em `'TGCCTAG'`

Agora é com você! Abra a [Tabela 2](https://docs.google.com/document/d/1JDX5QX84NwbD50oPLMp6Nfql1hNU1o5R30aBSc74IuU/edit?usp=sharing), faça outro download ou cópia e tente completa-la com oque aprendeu.

![tabela-vazia](tabela-ex-vazia.png)

>Qualquer dúvida é só chamar! mas antes, tente voltar nas explicações.


###

Se tudo der certo... você chegou em uma tabela com, mais ou menos, essa cara:

![tabela Resultado](tabela-resultado.png)

Agora tente traçar a linha referente aos passos dados.
###

Algo parecido? Se sim, show! acabamos a teoria. Sinta-se encorajado a tirar qualquer dúvida ainda existente

![tabela linha](tabela-linha.png)

###

Utilização na biotecnologia
---

Com o passar dos anos, cada vez mais, o algoritmo de Needleman e Wunsch foi sendo 
reconhecido como ferramenta fundamental para a análise de proteínas no desenvolvimento 
e sintetização de vacinas para o combate de doenças.

É graças ao que esses caras desenvolveram nessa época que conseguimos hoje ter 
acesso de forma fácil e simples a ferramentas complexas de análise genética só que
do conforto de casa.

Um exemplo dessas ferramentas é o [Blast](https://blast.ncbi.nlm.nih.gov/Blast.cgi).

Chegando no site, você vai se deparar com essa imagem. Clique no botão que a "setinha" aponta.

![Clique em Protein Blast](blast-3.jpg)

Na página seguinte, insira nessa caixa de texto maiorzinha o seguinte código proteico.

![Enter accession number(s), gi(s), or FASTA sequence(s)](blast-1.png)

    BETA-GALACTOSIDASE|BIFIDOBACTERIUM BIFIDUM S17 (883062)
    MSKRRKHSWPQPLKGAESRLWYGGDYNPDQWPEEVWDDDIRLMKKAGVNLVSVGIFSWAKIEPEEGKYDFDWLDRA
    IDKLGKAGIAVDLASATASPPMWLTQAHPEVLWKDERGDTVWPGAREHWRPTSPVFREYALNLCRRMAEHYKGNPY
    VVAWHVSNEYGCHNRFDYSDDAMRAFQKWCKKRYKTIDAVNEAWGTAFWAQHMNDFSEIIPPRYIGDGNFMNPGKL
    LDYKRFSSDALKELYIAERDVLESITPGLPLTTNFMVSAGGSMLDYDDWGAEVDFVSNDHYFTPGEAHFDEVAYAA
    SLMDGISRKEPWFQMEHSTSAVNWRPINYRAEPGSVVRDSLAQVAMGADAICYFQWRQSKAGAEKWHSSMVPHAGE
    DSQIFRDVCELGADLGRLSDEGLMGTKTVKSKVAVVFDYESQWATEYTANPTQQVDHWTEPLDWFRALADNGITAD
    VVPVRSDWDSYEIAVLPCVYLLSEETSRRVREFVANGGKLFVTYYTGLSDENDHIWLGGYPGSIRDVVGVRVEEFA
    PMGNDMPGALDHLDLDNGTVAHDFADVITSTADTSTVLASYKAERWTGMNEVPAIVANGYGDGRTVYVGCRLGRQG
    LAKSLPAMLGSMGLSDLAGDGRVLRVERADAAAASHFEFVFNRTHEPVTVDVEGEAIAASLAHVDDGRATIDPTGV
    VVLRR

Na mesma página, você terá que selecionar o set de busca que deseja no dropdown indicado na imagem
a seguir.

![Database](blast-2.png)

Selecione a opção Protein Data Bank proteins(PDB)

Em seguida clica em BLAST no fim da página.

O programa vai rodar o algoritmo apresentado comparando a sequencia proteica que eu lhe forneci
com as milhares que ele tem no PDB que é um Data Bank Mundial. E na página seguinte no fim dela ele 
vai retornar todas as bases proteicas que foram comparadas com a sua e os percentuais de 
similaridades.

>Vale resaltar que o BLAST é uma das ferramentas que esta sendo utilizadas no combate ao COVID-19
>pois serve como forma de comparacão rápida dos diversos sequenciamentos geneticos ao redor do mundo.

###

Análise da complexidade do algoritimo e conclução
---

Nesse handout trabalhamos um algoritimo sequencial que se mostrou importante para muito do que se tem
desenvolvido na genetica. Em resumo sua implementação consiste em ter duas strings para comparacão
e fazer o uso das tecnicas de construção da matrix que ensinamos para achar a quantidade de modificações
necessárias para transformar uma string na outra, em seguida usamos as ações especiais pra deixar as
strings iguais.

Vimos também durante o handout como fazer a implementação desse algoritmo em Python. Usamos funções para
preparar a matriz pra resolver checando alinhamento dos caracteres e deletando ou inserindo caso
fosse necessário.

Mas acho que falo por vocês quando digo: 
    "Beleza, mas qual a verdadeira complexidade disso?"

Você consegue pensar na complexidade gerada pelo algoritmo só observando o código que você criou?

>Dê um pausa de 2 min e discuta com seus colegas de mesa sobre isso

###

Se formos calcular puramente essa complexidade facilmente você consegue deduzir que ela é feita através
da multiplicação de duas matrizes com n colunas e uma linha. O que nos entrega uma uma complexidade $$n^2$$. Porém esse é um 
dos casos que conseguimos reduzir o número de operações através do uso do método dos 4 Russos. 

Um favor que eu peço é pra que você não abra o link agora, se não você vai me odiar e não é isso que queremos. 
Por isso eu vou resumir pra você. Mas se após o Handout você ficar mais curioso para conhecer melhor esse método, 
dai pra frente é sua conta em risco.

Método 4 russos
---

Esse [método](https://www.youtube.com/watch?v=cYJrMUvJQGc) leva em consideração que operações ja feitos e exatamente iguais não precisam ser repetidos pois ja sabemos 
o resultado delas, só nos basta substituir. Esse simples conceito já é capaz de reduzir nossa complexidade de $$n^2$$ para nm, sendo m um número menor que n o que em termos de processamento já ajuda bastante.

Apesar de ser um algoritimo primordial por ser muito utilizado quando se quer um excelente alinhamento global para o 
desenvolvimento da Bioinformática, era de se esperar que com o passar dos anos ele fosse desbancado pro outros como um
uso melhor do tempo de processamento, assim como é feito no Fast Optimal Global Sequence Alignment Algorithmb (FOGSAA).

Porém, todo esse revés no tempo de execução não impede em nenhum momento o uso em uma aplicação real que retrata o 
quanto essas operações criadas por Needleman e Wunsch foram importantes para o desenvolvimento e aprimoramento da humanidade até 
o estado que vemos ela hoje. Trazendo a capacidade de transmitir e comparar em tempo real descobertas
feitas ao redor do mundo de forma eficiente e prática.

>A ideia do algoritmo é a demonstrada até aqui.
>Para quem quiser entender um pouco mais dele, junto com uma implementação em python,
>clique em continuar, caso contrário, ele termina por aqui! Muito obrigado =)

###

Então você é curioso e quer continuar!?
---

![doge_programmer](doge_programmer.jpg)

Então vamos implementar!
---

Agora que já entendemos a lógica do funcionamento, vamos implementar isto em uma
ferramenta muito conhecido por todos nós: o *Python*!

Para começar vamos criar uma função que recebe duas strings *x* e *y* e prepara a matriz inicial,
preenchida com zeros.

    def prepara_matriz(x, y):
        matriz = []
        for i in range(len(x) + 1):
            linha = []
            for j in range(len(y) + 1):
                linha.append(0)
            matriz.append(linha)
        return matriz

Considerando que temos os valores de *x* e *y*, podemos deduzir como ficaria o código a seguir:

    x = "TCCAGT"
    y = "TGCCTAG"
    z = prepara_matriz(x, y)

    print(z)

###

A saída seria:

    >[[0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]]

>OBSERVAÇÃO: Podemos escrever esse código todo em apenas uma linha, mas esse não é o foco do handout.

    def prepara_matriz(x, y):
        matriz = [[0 for i in range(len(x) + 1)] for j in range(len(y) + 1)]
        return matriz

Com isso seguimos para a segunda etapa que, assim como na explicação da lógica do algoritmo feita neste mesmo handout, iremos preencher a primeira linha e primeira coluna da nossa matriz.

Como a primeira linha e a primeira coluna devem ser preenchidas com uma contagem dos valores, logo podemos melhorar nossa função *prepara_matriz*!

    def prepara_matriz(x, y):
        matriz = []
        for i in range(len(y) + 1):
            linha = []
            for j in range(len(x) + 1):
                linha.append(0)
            matriz.append(linha)

        for l in range(1, len(x) + 1):
            # primeira linha
            matriz[l][0] = l

        for c in range(1, len(y) + 1):
            # primeira coluna
            matriz[0][c] = c
            
        return matriz

Assim, agora teremos a seguinte saída...

    >[[0, 1, 2, 3, 4, 5, 6, 7], 
    [1, 0, 0, 0, 0, 0, 0, 0], 
    [2, 0, 0, 0, 0, 0, 0, 0], 
    [3, 0, 0, 0, 0, 0, 0, 0], 
    [4, 0, 0, 0, 0, 0, 0, 0], 
    [5, 0, 0, 0, 0, 0, 0, 0], 
    [6, 0, 0, 0, 0, 0, 0, 0]

Dessa forma vamos relembrar do início do handout e as três ações possíveis:

* **Alinhar** um caractere de uma palavra na outra, sinônimo de copiar
* **Inserir** um caractere novo em uma das palavras
* **Remover** um caractere de uma das palavras.

Vamos criar uma nova função para resolver a matriz...

    def resolve_matriz(matriz, x, y):
        for k in range(1, len(y) + 1):
            # Percorrendo termo a termo
            for i in range(1, len(x) + 1):
                for j in range(1, len(y) + 1):
                    # A função min() retornará o menor dentre os valores dados como argumentos
                    matriz[i][j] = min(matriz[i-1][j-1] + checa_alinhamento(x, y, i-1, j-1), # Alinhar
                                        matriz[i-1][j] + 1, # Deletar
                                        matriz[i][j-1] + 1) # Inserir

        return matriz

Porém ao ler este recorte de código, você deve ter percebido que não declaramos nenhuma função *"checa_alinhamento"* e... você está certo... por isso vamos ao trabalho!

Sabemos que a função *"checa_alinhamento"* irá comparar dois termos e retornará 1 para caso seja necessário um alinhamento, logo uma cópia do que chamamos aqui de *"valor base"* e 0 caso contrário.

Continue assim que pensar em uma forma de definir esta função.

###

É um código bem simples...

    def checa_alinhamento(x, y, i, j):
        if (x[i] != y[j]):
            return 1
        else:
            return 0

Agora só é necessário rodar tudo e...

    x = "TCCAGT"
    y = "TGCCTAG"
    
    z = prepara_matriz(x, y)
    z = resolve_matriz(z, x, y)
    print(z)

...*voilà*... temos a seguinte saída...

    >[[0, 1, 2, 3, 4, 5, 6, 7], 
    [1, 0, 1, 2, 3, 4, 5, 6], 
    [2, 1, 1, 1, 2, 3, 4, 5], 
    [3, 2, 2, 1, 1, 2, 3, 4], 
    [4, 3, 3, 2, 2, 2, 2, 3], 
    [5, 4, 3, 3, 3, 3, 3, 2], 
    [6, 5, 4, 4, 4, 3, 4, 3]]

Exatamente o que tínhamos previsto quando simulamos o código na mão...

Mas o código não acaba por ai! Devemos ainda descobrir o caminho de ações realizadas para chegar no resultado...

Vamos criar mais uma função que terá como saída este caminho, em sua respectiva ordem de alinhamento.

Para poder traçar o caminho é simples: iremos fazer o caminho da resposta final, logo o ponto *matriz[len(x)][len(y)]*, até o 0 inicial, na posição matriz[0][0] e escolheremos sempre o menor valor dentre a diagonal ao valor atual, o valor que estiver acima do mesmo e o valor a sua esquerda.

Além disso iremos utilizar de um conceito aprendido no início do semestre: recursão.

Pense um pouco sobre como elaborar esta função e somente depois clique em continuar.

###

Não é de se esperar que o código nada mais é do que checar qual o mínimo dentre as 3 opções de caminho possíveis para cada posição e então dar um passo.

    def alinhamento_final(matriz, m, n):
        if (m == 0 or n == 0):
            # base da recursão
            return

        # Faremos o mesmo cálculo feito na função resolve matriz
        alinhar = matriz[m - 1][n - 1] + checa_alinhamento(x, y, m - 1, n - 1)
        inserir = matriz[m][n-1] + 1
        deletar = matriz[m-1][n] + 1

        # Aqui vamos escolher a menor dentre as 3 opções de caminho
        melhor_escolha = min(inserir, alinhar, deletar)
        
        if (melhor_escolha == inserir):
            # Adicionamos o caminho escolhido para a lista de soluções
            solution.append('Inserir_' + str(y[n - 1]))
            # Então realizamos o passo para a direção andada
            return alinhamento_final(matriz[:m+1][:n], m, n - 1)

        elif (melhor_escolha == alinhar):
            # Adicionamos o caminho escolhido para a lista de soluções
            solution.append('Alinhar_' + str(y[n - 1]))
            # Então realizamos o passo para a direção andada
            return alinhamento_final(matriz[:m][:n], m - 1, n - 1)

        elif (melhor_escolha == deletar):
            # Adicionamos o caminho escolhido para a lista de soluções
            solution.append('Remover_' + str(x[m - 1]))
            # Então realizamos o passo para a direção andada
            return alinhamento_final(matriz[:m][:n+1], m - 1, n)

Agora só precisamos criar uma variável global para ser nossa lista de soluções e chamar a função com a matriz resultante da função *resolve_matriz*. É importante lembrar também que precisamos inverter a matriz *solution* para o print na saída ser da forma que esperamos!

    x = "TCCAGT"
    y = "TGCCTAG"
    z = prepara_matriz(x, y)
    z = resolve_matriz(z, x, y)

    solution = []
    alinhamento_final(z, len(x), len(y))
    
    # Por fim podemos printar a lista de soluções ao contrário
    # pois fizemos o caminho inverso na função alinhamento_final
    for i in solution[::-1]:
        print(i)

E assim obtemos a saída...

    >Alinhar_T
    Inserir_G
    Alinhar_C
    Alinhar_C
    Inserir_T
    Alinhar_A
    Alinhar_G
    Remover_T

Exatamente o que havíamos previsto novamente quando simulamos na mão!!!

>Obrigado por ter acompanhado até aqui! =)