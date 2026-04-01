# Sprint3DP

---

## Modelagem do Problema

Um lead pode ser considerado duplicado se houver correspondência em pelo menos um dos seguintes campos:

- E-mail
- Telefone
- CPF

A normalização dos dados é aplicada para garantir consistência (remoção de espaços, padronização de caixa e formatação numérica).

---

## Abordagens Implementadas

### 1. Verificação Recursiva

A função percorre a lista de leads recursivamente comparando cada elemento com o novo lead.

**Características:**
- Complexidade: O(n)
- Simples e direta
- Interrompe ao encontrar duplicidade

---

### 2. Memoização

Foi aplicada memoização para evitar recomputação de subproblemas já resolvidos.

**Características:**
- Armazena resultados intermediários
- Evita chamadas recursivas redundantes
- Neste caso específico, o ganho é limitado devido à natureza linear do problema

---

### 3. Indexação com Hash (Otimização)

Uso de estruturas set para armazenar:

- E-mails
- Telefones
- CPFs

**Características:**
- Complexidade: O(1) por verificação
- Escalável para grandes volumes
- Ideal para uso em produção

---

## Otimização de Agenda (Scheduler)

Implementação de um algoritmo baseado em programação dinâmica para maximizar o número de atendimentos sem conflito de horários.

### Estratégia

- Ordenação dos intervalos
- Uso de busca binária (bisect) para encontrar o próximo intervalo válido
- Memoização para evitar recomputação

**Complexidade:**
- Tempo: O(n log n)
- Espaço: O(n)

---

## Como Executar

### 1. Executar os testes

No terminal da IDE:

python -m unittest discover tests -v


---

### 2. Pré-requisitos

- Python 3.10 ou superior

---

## Testes

Os testes cobrem:

- Casos com duplicidade por e-mail, telefone e CPF
- Casos sem duplicidade
- Cenários com listas vazias e unitárias
- Validação da consistência entre abordagens
- Múltiplos cenários de agendamento (sobreposição, intervalos aninhados, etc.)

---

## Decisões de Projeto

- Uso de normalização no modelo Lead para evitar inconsistências
- Separação entre lógica de negócio e estrutura de dados
- Implementação de múltiplas abordagens para comparação de eficiência
- Priorização de clareza e previsibilidade sobre otimizações prematuras

---

## Conclusão

O problema foi resolvido utilizando diferentes estratégias:

- Recursão para solução básica
- Memoização para evitar recomputações
- Indexação para ganho de performance em escala

A solução final é modular, testável e escalável, permitindo evolução para integração com bancos de dados ou APIs.

---

## Integrantes do grupo

Ícaro Henrique de Souza Calixto - RM560278

Caio Costa Beraldo - RM560775

Victor Kenzo Mikado- RM560057

Pietro Brandalise De Andrade - RM560142
