# Fila de Atendimento

Aplicativo desktop com interface gráfica, feito em **Python** com **Tkinter**, para controlar uma fila de atendimento (clínica, barbearia, academia, etc.). Os clientes entram na fila e são chamados na ordem de chegada.

## Funcionalidades

- Cadastro de clientes na fila pelo botão **Entrar na fila** ou pela tecla **Enter**.
- Lista de espera com a posição de cada cliente.
- Botão **Chamar próximo**, que tira o primeiro da fila e o exibe como "Em atendimento".
- Validação do nome digitado:
  - campo vazio exibe o aviso "Digite um nome.";
  - nomes com números ou símbolos exibem o aviso "Use apenas letras no nome." (letras com acento, espaços, hífens e apóstrofos são aceitos, como em `José Silva`, `Ana-Clara` e `D'Ávila`);
  - nomes já presentes na fila exibem o aviso "Esse nome já está na fila.";
- Aviso de "Fila vazia" ao tentar chamar o próximo sem ninguém aguardando.
- Formatação automática dos nomes: cada palavra começa com letra maiúscula, exceto "da", "de", "do", "das", "dos" e "e" (por exemplo, `joão da silva` vira `João da Silva`).
- Bloqueio de nomes repetidos na fila, sem diferenciar maiúsculas de minúsculas (`maria` é considerado igual a `Maria`).
- Botão **Limpar fila**, que remove todos os clientes aguardando, com confirmação antes de apagar.

## Tecnologias

- Python 3
- Tkinter (biblioteca de interface gráfica que já vem com o Python)
- `collections.deque` para a estrutura de fila

Nenhuma instalação adicional é necessária.

## Como executar

1. Instale o [Python 3](https://www.python.org/downloads/). No Windows, marque a opção **Add Python to PATH** durante a instalação.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto e execute:

```bash
python fila_atendimento.py
```

No Windows, se `python` não funcionar, use:

```bash
py fila_atendimento.py
```

Para confirmar que o Tkinter está funcionando na sua máquina, rode `python -m tkinter`. Uma janela de teste deve abrir.

## Como usar

1. Digite o nome do cliente no campo **Nome do cliente**.
2. Clique em **Entrar na fila** ou aperte **Enter**. O nome aparece na lista **Aguardando**.
3. Clique em **Chamar próximo** para atender o primeiro da fila. O nome passa a aparecer em **Em atendimento**.
4. Para remover todos os clientes que estão aguardando, clique em **Limpar fila** e confirme. Quem já está em atendimento continua na tela.

## Estrutura do código

O projeto fica em um único arquivo, `fila_atendimento.py`, dividido em três partes:

| Parte | Responsabilidade |
|---|---|
| `nome_valido(nome)` | Função que valida o nome digitado. |
| `FilaAtendimento` | Lógica do programa: guarda a fila e quem está em atendimento. Não tem nenhum código de interface. |
| `App` | Interface gráfica: monta a janela, lê o que foi digitado, mostra avisos e atualiza a tela. |

### Principais métodos

**`FilaAtendimento`**

- `entrar(nome)`: formata o nome (iniciais maiúsculas, exceto partículas como "da" e "de") e o coloca no final da fila.
- `chamar_proximo()`: remove o primeiro da fila e o define como em atendimento. Devolve `False` se a fila estiver vazia e `True` caso contrário.
- `ja_esta_na_fila(nome)`: devolve `True` se o nome já estiver na fila, ignorando maiúsculas e espaços repetidos.
- `limpar()`: remove todos os clientes da fila.

**`App`**

- `adicionar()`: lê o campo, valida o nome (vazio, só letras e repetido), coloca o cliente na fila e atualiza a tela.
- `chamar()`: chama o próximo cliente e mostra o aviso de fila vazia, se for o caso.
- `limpar()`: pede confirmação e esvazia a fila.
- `atualizar_tela()`: redesenha a lista de espera e o texto de "Em atendimento".

## Conceitos praticados

- Estrutura de dados **fila (FIFO)**, com `deque`, `append` e `popleft`.
- Orientação a objetos: classes, construtor `__init__` e composição (o `App` usa um objeto `FilaAtendimento`).
- Separação entre lógica e interface.
- Widgets do Tkinter (`Label`, `Entry`, `Button`, `Listbox`) e posicionamento com `pack()`.
- Eventos (`bind`) e funções de clique (`command`).
- Event loop com `mainloop()`.
- Validação de entrada com `strip()` e `isalpha()`.
- Caixas de mensagem com `messagebox`.
- Manipulação de texto com `split()`, `join()` e `title()`.
- Caixa de confirmação com `askyesno`.

## Possíveis melhorias

- Adicionar máximo de caracteres no campo de entrada.
- Fila preferencial.
- Registrar o horário de entrada e mostrar o tempo de espera.
- Modernizar o visual com CustomTkinter.
- Adicionar botão para remover uma pessoa especifica da fila. 
- Adicionar um botão para salvar a fila em um arquivo e outro para carregar um arquivo que contenha fila