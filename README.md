# Fila de Atendimento

Aplicativo desktop com interface gráfica, feito em **Python** com **Tkinter**, para controlar uma fila de atendimento (clínica, barbearia, academia, etc.). Os clientes entram na fila e são chamados na ordem de chegada.

## Funcionalidades

- Cadastro de clientes na fila pelo botão **Entrar na fila** ou pela tecla **Enter**.
- Lista de espera com a posição de cada cliente.
- Botão **Chamar próximo**, que tira o primeiro da fila e o exibe como "Em atendimento".
- Validação do nome digitado:
  - campo vazio exibe o aviso "Digite um nome.";
  - nomes com números ou símbolos exibem o aviso "Use apenas letras no nome." (letras com acento, espaços, hífens e apóstrofos são aceitos, como em `José Silva`, `Ana-Clara` e `D'Ávila`);
- Aviso de "Fila vazia" ao tentar chamar o próximo sem ninguém aguardando.

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

## Estrutura do código

O projeto fica em um único arquivo, `fila_atendimento.py`, dividido em três partes:

| Parte | Responsabilidade |
|---|---|
| `nome_valido(nome)` | Função que valida o nome digitado. |
| `FilaAtendimento` | Lógica do programa: guarda a fila e quem está em atendimento. Não tem nenhum código de interface. |
| `App` | Interface gráfica: monta a janela, lê o que foi digitado, mostra avisos e atualiza a tela. |

### Principais métodos

**`FilaAtendimento`**

- `entrar(nome)`: coloca o cliente no final da fila.
- `chamar_proximo()`: remove o primeiro da fila e o define como em atendimento. Devolve `False` se a fila estiver vazia e `True` caso contrário.

**`App`**

- `adicionar()`: lê o campo, valida o nome, coloca o cliente na fila e atualiza a tela.
- `chamar()`: chama o próximo cliente e mostra o aviso de fila vazia, se for o caso.
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

## Possíveis melhorias

- Padronizar as iniciais em maiúsculo (por exemplo, `maria silva` virar `Maria Silva`).
- Registrar o horário de entrada e mostrar o tempo de espera.
- Adicionar um botão para limpar a fila.
- Impedir nomes repetidos.
- Modernizar o visual com CustomTkinter.
