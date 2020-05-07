Algoritmo Needleman-Wunsch para alinhamento de sequências
==========================

To do: (cada item é um break)
---

* Explicar oq é (pra que serve)
* Explicar a lógica
* Implementação
* Conclusão

>começo do handout

Introdução
---

Com a recém descoberta do DNA, formado por cadeias de aminoácidos com bases
nitrogenadas, Saul Needleman e Christian Wunsch, em 1969, foram atrás de 
solucionar o problema de encontrar similaridades entre as estas, o que era
uma necessidade para a área de estudo da genética.

De forma geral, o algoritmo consiste em analisar duas palavras e verificar
quantas mudanças seriam necessárias para tornar uma palavra igual a outra.

Exemplo
---
O algoritmo foi projetado para objetos do tipo *String* e, portanto, podemos
começar entendendo com um exemplo utilizando palavras ao invés de bases
nitrogenadas.

Temos duas palavras muito semelhantes porém diferentes:

    >   COERENCIA
      OCORRENCIA
      

Desejamos que elas sejam iguais, para isso precisaremos realizar algumas mudanças.
Manteremos a palavra "*COERENCIA*" como nosso padrão e alteraremos a palavra "*OCORRENCIA*".

Há 2 diferenças nestas palavras:

* Número de caracteres diferentes
* Pelo menos 1 caractere diferente da outra


Dessa forma podemos realizar pequenas e pontuais mudanças. Começaremos deletando o primeiro
caractere de "*OCORRENCIA*", pois como vemos em nossa base, ele não existe, assim temos:

    >  COERENCIA
      CORRENCIA 

Agora percebemos que temos duas palavras muito próximas porém ainda há uma diferença: 
o 3º caractere delas são diferentes

> Se entendeu minimamente até aqui, pode continuar
> 
> Caso contrário, leia o exemplo novamente.

Lógica
---

Este Algorítimo segue uma lógica em que iremos checar, por meio de uma matriz, 
qual o numero de *alterações* que deve ser feita para tranformar a substring na 
vertical na substring da horizontal


![tabela 1](tabela-1.png)

Na tabela acima, podemos ver que cada casa da matriz representa quantas ações são 
feitas para transformar a substring correspondente da vertical na da horizontal.

Vamos agora tentar preencher essa tabela 

>rascunhos

agora vai
  
    print('Fala hélio')

| Tables   |      Are      |  Cool |
|----------|:-------------:|------:|
| col 1 is |  left-aligned | $1600 |
| col 2 is |    centered   |   $12 |
| col 3 is | right-aligned |    $1 |

aaa
| titulo  | 2 titulo  |
|---------|-----------|
| valor   |  valor 2  |

aaaaa


Isto é texto normal. Para mudar de parágrafo, pule uma linha.

Em texto normal, você pode usar *itálico*, **negrito**, `código` e `>comando`.
Como você pode ver nesse exemplo, o modo de código é para ser usado em texto de
código-fonte. Quando você tenta escrever texto normal, efeitos estranhos podem
acontecer, como essa cor diferente no "o" com acento agudo.

Você também pode usar $$\LaTeX$$, se souber. Tanto no meio ($$\sum^n_{i=1}i$$)
de parágrafos, quanto em parágrafos próprios centralizados:

$$$\sum^n_{i=1}i.$$$

Adicionalmente, também pode criar

* listas

* não-ordenadas,

assim como

1. listas

2. ordenadas.

Finalmente, também pode criar

    print('código em parágrafo destacado,')

assim como

    >comando em parágrafo destacado.

Nesses dois casos, espaços em branco e quebras de linha serão respeitados.


Exemplo de subtítulo
--------------------

A notação para criar [um link](https://www.insper.edu.br/) é bem simples.

A notação para criar

![uma imagem](exemplo.png)

é bem parecida. Espera-se que todas as imagens estejam na pasta *img*.

A notação para criar

>um aviso

é mais simples ainda.

Para terminar, só falta mostrar como criar uma pausa.

>Não continue sem vir validar no canal geral.

###

That's all Folks!
