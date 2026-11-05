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
        """Formata o nome antes de guardá-lo"""
        nomes = nome.split()  
        for i in range(len(nomes)):  
            if nomes[i] not in ["da", "de", "do", "das", "dos", "e"]:
                nomes[i] = nomes[i].title()
        nome = " ".join(nomes)

        """Adiciona o nome na fila"""
        self.fila.append(nome)

    def chamar_proximo(self):
        if not self.fila:
            return False
        self.em_atendimento = self.fila.popleft()
        return True

    def limpar(self):
        self.fila.clear()

    def ja_esta_na_fila(self, nome):
        nome = " ".join(nome.split()).lower()
        for cliente in self.fila:
            if cliente.lower() == nome:
                return True
        return False


class App:
    """Interface gráfica."""

    def __init__(self, janela):
        self.fila = FilaAtendimento()

        janela.title("Fila de Atendimento")
        janela.geometry("360x420")

        tk.Label(janela, text="Nome do cliente:").pack(pady=(15, 0))
        self.entrada = tk.Entry(janela, width=30)
        self.entrada.pack(pady=5)
        self.entrada.bind("<Return>", lambda e: self.adicionar()) 

        tk.Button(janela, text="Entrar na fila", command=self.adicionar).pack(pady=5)

        tk.Label(janela, text="Aguardando:").pack(pady=(15, 0))
        self.lista = tk.Listbox(janela, width=35, height=10)
        self.lista.pack(pady=5)

        tk.Button(janela, text="Chamar próximo", command=self.chamar).pack(pady=10)

        tk.Button(janela, text="Limpar fila", command=self.limpar).pack(pady=5)
        janela.geometry("360x470")

        self.label_atendimento = tk.Label(
            janela, text="Em atendimento: ninguém", font=("Arial", 12, "bold")
        )
        self.label_atendimento.pack(pady=10)

    def adicionar(self):
        nome = self.entrada.get().strip()
        if not nome: # Ao tentar adicionar um nome sem digitar nenhum caractere
            messagebox.showwarning("Atenção", "Digite um nome.") # 
            return
        if not nome_valido(nome):
            messagebox.showwarning("Atenção", "Use apenas letras no nome.")
            return
        if self.fila.ja_esta_na_fila(nome):
            messagebox.showwarning("Atenção", "Esse nome já está na fila.")
            return
        self.fila.entrar(nome)
        self.entrada.delete(0, tk.END)
        self.atualizar_tela()

    def chamar(self):
        if not self.fila.chamar_proximo():
            messagebox.showinfo("Fila vazia", "Não há ninguém aguardando.")
            return
        self.atualizar_tela()

    def limpar(self):
        if not self.fila.fila:
            messagebox.showinfo("Fila vazia", "Não há ninguém para remover.")
            return
        if messagebox.askyesno("Confirmar", "Deseja remover todos os clientes da fila?"): # Já inclui a condição de clicar em "Sim"
            self.fila.limpar()
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
