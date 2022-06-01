# pyRPG

## Estrutura

### Mapa

- Caminho predefinido por níveis
- Cada parte do caminho possui uma caixinha que pode ou não conter ITENS
- Cada caixa pode ou não ser guardada por um INIMIGO

### Níveis

### Itens

1. Armas (Nome/Peso/Ataque)
2. Poções (Nome/Peso/Cura)

### Personagens

1. Inimigos (Nome/Ataque/HP)
2. Herói (Nome/HP)

- Cinto de itens para acesso rápido
- Possui limite de itens e peso
- Mochila para outros itens
- Um objeto sobre o outro (aplicação de pilhas)
- Não possui limite de itens e peso

### Regras e Interações

1. Caixinhas

- Com itens: o herói pode decidir em pegar ou não os itens
  - Pegar o item: guardá-lo no cinto ou na mochila
  - Não pegar: o item desaparece do caminho

2. Batalhas

- O herói pode escolher qualquer arma do cinto ou da mochila (desde que possível) para a batalha
- As batalhas funcionam por turnos, ou seja, um ataque de cada um por vez
- Caso o herói morra o jogo termina, caso contrário, ele pode seguir no mapa
- O uso de poções pode ser feito para a recuperação de HP, de acordo com o nível de cura do item, caso seja atingida o nível máximo de HP a poção desaparece

3. Movimentação

- Caixinhas vazias
  - O jogador pode "organizar seu inventário", ou seja, manipular o conteúdo do cinto e/ou da mochila
- Caixinhas com itens
  - O jogador pode "organizar o inventário" e manipular o item descoberto
  - Avança para a próxima caixinha
- Caixinhas com inimigos
  - Começa uma batalha
  - Avança para a próxima caixinha

### Interface

1. Herói

- No início do jogo o nome do herói deve ser escolhido

2. Cinto e Mochila

- Devem ser mostrados o tempo todo em tela

3. HP

- Deve ser mostrado junto do cinto e da mochila

4. Opções de Interação

- Devem aparecer de acordo com as necessidades de ações no jogo

## Enredo
