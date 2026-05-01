import tkinter as tk
def adicionar_numero(numero):

    conteudo_atual= entry.get()
    novo_conteudo= conteudo_atual + str(numero)
    entry.delete(0, tk.END)
    entry.insert(0, novo_conteudo)
def limpar():
    entry.delete(0,tk.END)

def calcular():
    expressao = entry.get()
    resultado = eval(expressao)
    entry.delete(0, tk.END)
    entry.insert(0, resultado)

janela = tk.Tk()

janela.geometry("700x600")
janela.title("Calculadora")
janela.grid_columnconfigure(0, weight = 1)
janela.grid_columnconfigure(1, weight = 1)
janela.grid_columnconfigure(2, weight = 1)
janela.grid_rowconfigure(1, weight = 1)
janela.grid_rowconfigure(2, weight = 1)
janela.grid_rowconfigure(3, weight = 1)
janela.grid_rowconfigure(4, weight = 1)

entry = tk.Entry(janela)
entry.grid(row = 0, column = 0, columnspan = 3)

botao1 = tk.Button(janela, text ="1", command=lambda: adicionar_numero(1))
botao1.grid(row = 3, column = 0, sticky = "nsew", padx=5, pady=5)

botao2 = tk.Button(janela, text ="2", command=lambda: adicionar_numero(2))
botao2.grid(row = 3, column = 1, sticky = "nsew",padx=5, pady=5)

botao3 = tk.Button(janela, text ="3", command=lambda: adicionar_numero(3))
botao3.grid(row = 3, column = 2, sticky = "nsew", padx=5, pady=5)

botao4 = tk.Button(janela, text ="4", command=lambda: adicionar_numero (4))
botao4.grid(row = 2, column = 0, sticky = "nsew", padx=5, pady=5)

botao5 = tk.Button(janela, text = "5",command=lambda: adicionar_numero (5))
botao5.grid(row = 2, column = 1, sticky = "nsew", padx=5, pady=5)

botao6 = tk.Button(janela, text = "6", command=lambda: adicionar_numero (6))
botao6.grid(row = 2, column = 2, sticky = "nsew", padx=5, pady=5)

botao7 = tk.Button(janela, text = "7", command=lambda: adicionar_numero (7))
botao7.grid(row = 1, column = 0, sticky = "nsew", padx=5, pady=5)

botao8 = tk.Button(janela, text = "8", command=lambda: adicionar_numero (8))
botao8.grid(row = 1, column = 1, sticky = "nsew", padx=5, pady=5)

botao9 = tk.Button(janela, text = "9", command=lambda: adicionar_numero (9))
botao9.grid(row = 1, column = 2, sticky = "nsew", padx=5, pady=5)

botao0 = tk.Button(janela, text = "0", command=lambda: adicionar_numero (0))
botao0.grid(row = 4, column = 1, sticky = "nsew", padx=5, pady=5)

botaomais = tk.Button(janela, text = "+", command=lambda: adicionar_numero ("+"))
botaomais.grid(row = 1, column = 3, sticky = "nsew", padx=5, pady=5)

botaomenos = tk.Button(janela, text = "-", command=lambda: adicionar_numero ("-"))
botaomenos.grid(row = 2, column = 3, sticky = "nsew", padx=5, pady=5)

botaovezes = tk.Button(janela, text = "*", command=lambda: adicionar_numero ("*"))
botaovezes.grid(row = 3, column = 3, sticky = "nsew", padx=5, pady=5)

botaodividir = tk.Button(janela, text = "/", command=lambda: adicionar_numero ("/"))
botaodividir.grid (row = 4, column = 3, sticky = "nsew", padx=5, pady=5)

botaolimpar = tk.Button(janela, text = "C", command=limpar)
botaolimpar.grid (row = 0, column = 3, sticky = "nsew", padx=5, pady=5)

botaoigual = tk.Button(janela, text = "=", command=calcular)
botaoigual.grid (row = 4, columnspan = 3, sticky = "nsew", padx=5, pady=5)

janela.mainloop()
