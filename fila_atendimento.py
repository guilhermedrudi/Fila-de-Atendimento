import tkinter as tk
from tkinter import messagebox
from collections import deque


def nome_valido(nome):
    sem_extras = nome.replace(" ", "").replace("-", "").replace("'", "")
    return sem_extras.isalpha()

class FilaAtendimento:
    """Lógica do programa (sem nada de interface)."""

    def __init__(self):
        self.fila = deque()
        self.em_atendimento = None

    def entrar(self, nome):
        self.fila.append(nome)

    def chamar_proximo(self):
        if not self.fila:
            return False
        self.em_atendimento = self.fila.popleft()
        return True


class App:
    """Interface gráfica."""

    def __init__(self, janela):
        self.fila = FilaAtendimento()

        janela.title("Fila de Atendimento")
        janela.geometry("360x420")

        tk.Label(janela, text="Nome do cliente:").pack(pady=(15, 0))
        self.entrada = tk.Entry(janela, width=30)
        self.entrada.pack(pady=5)
        self.entrada.bind("<Return>", lambda e: self.adicionar())  # Enter também adiciona

        tk.Button(janela, text="Entrar na fila", command=self.adicionar).pack(pady=5)

        tk.Label(janela, text="Aguardando:").pack(pady=(15, 0))
        self.lista = tk.Listbox(janela, width=35, height=10)
        self.lista.pack(pady=5)

        tk.Button(janela, text="Chamar próximo", command=self.chamar).pack(pady=10)

        self.label_atendimento = tk.Label(
            janela, text="Em atendimento: ninguém", font=("Arial", 12, "bold")
        )
        self.label_atendimento.pack(pady=10)

    def adicionar(self):
        nome = self.entrada.get().strip()
        if not nome:
            messagebox.showwarning("Atenção", "Digite um nome.")
            return
        if not nome_valido(nome):
            messagebox.showwarning("Atenção", "Use apenas letras no nome.")
            return
        self.fila.entrar(nome)
        self.entrada.delete(0, tk.END)
        self.atualizar_tela()

    def chamar(self):
        if not self.fila.chamar_proximo():
            messagebox.showinfo("Fila vazia", "Não há ninguém aguardando.")
            return
        self.atualizar_tela()

    def atualizar_tela(self):
        self.lista.delete(0, tk.END)
        for posicao, nome in enumerate(self.fila.fila, start=1):
            self.lista.insert(tk.END, f"{posicao}. {nome}")
        atual = self.fila.em_atendimento or "ninguém"
        self.label_atendimento.config(text=f"Em atendimento: {atual}")


if __name__ == "__main__":
    janela = tk.Tk()
    App(janela)
    janela.mainloop()
