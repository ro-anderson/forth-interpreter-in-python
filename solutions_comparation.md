## Comparação das implementações do Interpretador Para a Linguagem Forth em Python: `dsardelic_solution` vs. `tugrul_solution`

Este documento realiza uma comparação entre duas abordagens para o [problema proposto](https://exercism.org/tracks/python/exercises/forth) pela plataforma [Exercism](https://exercism.org/). O primeiro, enviado por um usuário chamado [`dsardelic`](https://exercism.org/tracks/python/exercises/forth/solutions/dsardelic), utilizou a estrutura `pattern matching` do Python, um recurso [introduzido no Python 3.10](https://docs.python.org/3/whatsnew/3.10.html), para lidar com operações com elegância. O segundo, fornecido por [`tugrul`](https://exercism.org/tracks/python/exercises/forth/solutions/tugrul), está mais aderente a um paradigma de programação funcional, utilizando funções lambda e métodos utilitários para quebrar as tarefas de interpretação. Esta comparação visa esclarecer os pontos fortes, potenciais pontos fracos e características únicas de cada solução, oferecendo insights sobre diferentes estilos e metodologias de programação.



Para obter uma perspectiva mais aprofundada (apesar de não ter sido solicitado no desafio), antes de iniciar a comparação, foi elaborada uma solução que pode ser explorada [neste repositório GitHub](https://github.com/ro-anderson/forth-interpreter-in-python). Esta solução foi construída utilizando o paradigma de Programação Orientada a Objetos (OOP), com estruturas de classes claras representando comandos distintos. Também foram escolhidos alguns design patterns para garantir modularidade, extensibilidade e facilidade de manutenção.


### Abordagem:

- **dsardelic** usa pattern matching e funções aninhadas dentro de uma função de avaliação principal. Essa abordagem moderna torna o código estruturado e fácil de ler.
- **tugrul** utiliza um estilo mais aderente ao paradigma funcional, usando funções lambda e funções utilitárias para lidar com tarefas específicas. Isso fornece um fluxo de dados claro e minimiza os efeitos colaterais.

### Modularidade:

- **dsardelic** lida com operações por meio de correspondência de padrões dentro da função principal. Embora isso forneça uma estrutura clara para cada operação, pode dificultar a extensão ou modificação de partes específicas do código. A lógica para definições de palavras personalizadas também está incorporada na função principal, que pode se beneficiar de uma abordagem mais modular.
- **tugrul** fornece um design modular com funções utilitárias distintas como `is_number`, `apply` e `substitute`. Essas funções dividem tarefas específicas, melhorando a legibilidade e a manutenção do código.

### Tratamento personalizado de palavras:

- Na solução de **dsardelic**, a lógica de palavras customizadas é processada em linha durante a avaliação. Isso pode representar desafios para definições de palavras personalizadas profundamente aninhadas ou recursivas.
- **tugrul** pré-processa palavras personalizadas usando a função `substitute`. Isso garante que as palavras personalizadas sejam expandidas para suas operações básicas antes da execução, oferecendo potencialmente benefícios de desempenho para definições personalizadas extensas.

### Manipulação de Erros:
- **dsardelic**:

Pontos Fortes: Esta solução utiliza exceções personalizadas para lidar com cenários específicos, como a tentativa de dividir por zero ou quando uma operação não está definida. Isso oferece feedback detalhado ao usuário e torna o código mais robusto.
Áreas de Melhoria: Uma maior variedade de exceções personalizadas para tratar cenários mais específicos, como tentativas de realizar operações de pilha sem elementos suficientes ou definições inválidas de palavras personalizadas.

- **tugrul**:

Pontos Fortes: Assim como a solução de dsardelic, tugrul também faz bom uso de exceções personalizadas para tratar situações como divisão por zero ou operações não definidas.

Áreas de Melhoria: Seria interessante adicionar tratamentos para situações em que palavras personalizadas são definidas de forma recursiva, o que poderia causar loops infinitos. Também poderia beneficiar-se de exceções para casos onde palavras personalizadas sobrescrevem comandos padrão.


### Desempenho:

- A correspondência de padrões de **dsardelic** pode oferecer pequenos benefícios de desempenho em relação às verificações condicionais tradicionais. No entanto, o tratamento em linha de palavras personalizadas pode representar desafios para definições profundamente aninhadas ou recursivas.
- **tugrul** pré-processa palavras personalizadas, garantindo eficiência no ciclo de avaliação principal. No entanto, substituições extensas de palavras personalizadas podem gerar sobrecarga.

Sugestões de Melhorias:
- **dsardelic**:

Modularidade: A lógica de tratamento de palavras personalizadas poderia ser extraída para uma função separada ou método para melhor clareza e manutenção.
Extensibilidade: Considerando futuras extensões, seria útil ter uma estrutura mais modular para adicionar novas operações ou funcionalidades.
- **tugrul**:

Verificação de Palavras Personalizadas: Implementar verificações para garantir que palavras personalizadas não sobrescrevam comandos padrão.

Refatoração:

Ao analisar a solução do `tugrul`, notamos que a função `evaluate` é responsável por várias tarefas, incluindo a substituição de palavras personalizadas e a execução de operações. Uma refatoração poderia se concentrar em separar essas responsabilidades para melhorar a legibilidade e a modularidade do código.

Por exemplo, a lógica de substituição das palavras personalizadas atualmente reside na função `substitute`. Esta função é chamada repetidamente até que não haja mais substituições a serem feitas. Uma refatoração potencial seria transformar essa lógica em uma função separada que garante que todas as palavras personalizadas sejam substituídas de uma vez:

```python
def expand_custom_words(tokens, definitions):
    has_substitution = True
    while has_substitution:
        has_substitution = False
        expanded_tokens = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in definitions:
                expanded_tokens.extend(definitions[token])
                has_substitution = True
            else:
                expanded_tokens.append(token)
            i += 1
        tokens = expanded_tokens
    return tokens
```

E então, na função `evaluate`, antes de processar os tokens, você faria:

```python
tokens = expand_custom_words(tokens, definitions)
```

Isso torna a função `evaluate` um pouco mais concisa, pois agora ela pode se concentrar principalmente na avaliação dos tokens, enquanto a lógica de expansão das palavras personalizadas é claramente separada em sua própria função.

### Conclusão:

Tanto `dsardelic` quanto `tugrul` fornecem implementações eficazes de um interpretador Forth em Python, cada um com seus pontos fortes exclusivos e áreas de melhoria. O uso de correspondência de padrões por `dsardelic` oferece uma abordagem moderna e estruturada, enquanto o estilo funcional de `tugrul` enfatiza clareza e previsibilidade. Dependendo dos requisitos específicos, como necessidades de desempenho, extensibilidade ou familiaridade do desenvolvedor, um pode ser escolhido em vez do outro. Independentemente da escolha, ambas as soluções estabelecem uma base sólida para maior desenvolvimento e refinamento.
