---
marp: true
theme: uncover
_class: invert
---

## Sistemas Especialistas :robot:

Prof. Me. Alexandre Henrick

Sistemas de Informação - 8º P

---

### Sistemas Especialistas

- Agentes baseados em **lógica**, também conhecidos como **Sistemas Especialistas (SEs)**
- Resolvem problemas com base na lógica matemática
- Utilizam regras pré-definidas e constroem conhecimento inferindo regras

---

### Sistemas Especialistas

- Como resolvemos problemas?
- Representando conhecimento disponível em uma Base de Conhecimento (BC)
- Busca solução para o problema a partir de novos conhecimentos extraídos dessa BC

---

### Sistemas Especialistas

- São utilizados em automação de diversos tipos de tarefas que, normalmente, são executadas com limitações por humanos
- São usados como ***conelheiros especialistas**
- Alguns domínios de aplicação:
    - Área médica;
    - Área de investimentos;
    - Comércio eletrônico

---

### Representação do Conhecimento

- Os SEs representam o conhecimento por meio de fórmulas de **cálculo de predicados (afirmação sobre sujeito)**
- Essas fórmulas são **armazenadas em uma Base de Conhecimento**
- Elas exprimem regras (implicações lógicas) ou fatos (verdades incondicionais)

---

### Métodos de resolução

- Encadeamento Progressivo: SE processa toda a BC para extrair novos conhecimentos inferidos a partir dela. Checa na BC todos os literais dos antecedentes de cada regra que são verdadeiros. Se todos os literais da regra forem verdadeiros, o SE infere seu literal consequente como novo conhecimento e o insere como fato na BC.

---

### Estrutura de uma regra

$(Rex \ É \ UM  \ cachorro \ \land \ Rex \ É \ PAI \ DE \ Bozo) \to$

$Bozo \ É \ UM \ cachorro$

---

### Estrutura de uma regra

![height:4in](../imgs/regra1.png)

---

### Base de Conhecimento

- A BC é composta pela **Base de Fatos** e pela **Base de Regras**
- A Base de Fatos são conhecimentos pré-determinados. Verdades já conhecidas
- Já a Base de Regras armazena as regras utilizadas para fazer inferências e verificar se um novo fato foi gerado

---
### Base de Fatos

- $Bozo \ É \ UM \ cachorro$
- $Pegasos \ É \ UM \ cavalo$
- $Pegasos \ É \ PAI \ DE \ Pe \ de \ pano$
- $Pegasos \ É \ PAI \ DE \ Spirit$

---

### Base de Regras

$(x\_animal \ É \ UM \ z\_especie \ \land$
$x\_animal \ É \ PAI \ DE \ y\_filhote)\to$
$y\_filhote \ É \ UM \ z\_especie$


Onde:

- $É \ UM$ e $É \ PAI \ DE$ são predicados;
- $x\_animal$, $y\_filhote$ e $z\_especie$ são variáveis
- Bozo, Pegasos, Pé de pano e Spirit são constantes

---

### Processamento feito pelo SE

- Itera sobre as regras na BC.
- A cada iteração fixa uma regra  $R_i$ da base de regras e checa na base de fatos se cada um dos literais do antecedente é verdadeiro
- Se todos forem, insere o literal expresso no consequente da regra $R_i$ como novo fato na base de fatos

---

### Processando primeiro literal

Após o processamento do primeiro literal da regra, as variáveis $x\_animal$ e $z\_especie$ podem assumir EXCLUSIVAMENTE UM dos seguintes pares de valores:

- $x\_animal = Bozo$; $z\_especie = cachorro$;
- $x\_animal = Pegasos$; $z\_especie = cavalo$

---

### Processando segundo literal

Após o processamento do segundo literal da regra, as variáveis envolvidas podem assumir QUALQUER UM dos seguintes pares de valores:

- $x\_animal = Pegasos$; $y\_filhote = Pe \ de \ pano$; $z\_especie = cavalo$;
- $x\_animal = Pegasos$; $y\_filhote = Spirit$; $z\_especie = cavalo$;

---

### Novos fatos para a Base de Fatos

- $Pe \ de \ pano \ É \ UM \ cavalo$ <- novo
- $Spirit \ É \ UM \ cavalo$ <- novo
- $Bozo \ É \ UM \ cachorro$
- $Pegasos \ É \ UM \ cavalo$
- $Pegasos \ É \ PAI \ DE \ Pe \ de \ pano$
- $Pegasos \ É \ PAI \ DE \ Spirit$

---

### Referências

- Baseado nos materiais disponibilizados pela professora Drª Rita Maria da Silva Julia. Disciplina de Machine Learning - UFU-FACOM
- Russell, S. J. 1., & Norvig, P. (1995). Artificial intelligence: a modern approach. Englewood Cliffs, N.J., Prentice Hall.