import tkinter as tk
import random

class JogoDasPortas:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo das Portas")
        self.root.geometry("600x400")

        self.nome_jogador = ""
        self.fase_atual = 1
        self.ganhou = False

        self.frame_nome = tk.Frame(root)
        self.frame_nome.pack(pady=20)
        self.lbl_nome = tk.Label(self.frame_nome, text="Digite seu nome:")
        self.lbl_nome.pack(side="left")
        self.entry_nome = tk.Entry(self.frame_nome)
        self.entry_nome.pack(side="left")
        self.btn_nome = tk.Button(self.frame_nome, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.btn_nome.pack(side="left")

        self.frame_status = tk.Frame(root)
        self.frame_status.pack(pady=10)
        self.lbl_status = tk.Label(self.frame_status, text="", font=("Arial", 12))
        self.lbl_status.pack()

        self.btn_proxima_fase = tk.Button(root, text="Próxima Fase", state=tk.DISABLED, command=self.proxima_fase)
        self.btn_proxima_fase.pack(pady=10)

        self.frame_portas = tk.Frame(root)
        self.frame_portas.pack()
        self.portas = [tk.Button(self.frame_portas, text="Porta 1", width=15, height=3, font=("Arial", 12),
                                 command=lambda: self.escolher_porta(1)),
                       tk.Button(self.frame_portas, text="Porta 2", width=15, height=3, font=("Arial", 12),
                                 command=lambda: self.escolher_porta(2)),
                       tk.Button(self.frame_portas, text="Porta 3", width=15, height=3, font=("Arial", 12),
                                 command=lambda: self.escolher_porta(3))]

        for porta in self.portas:
            porta.pack(side="left", padx=10)

        self.historia = [
            "Você de alguma forma morreu e está no purgatório, e precisa passar por portas...",
            "As portas parecem iguais, mas algumas estão mais enferrujadas.",
            "Aqui as portas estão todas diferentes, a primeira parece mais tecnológica, a segunda bem velha e a última rústica."
        ]

        self.fase_info = [
            [
                ["Uma porta antiga com inscrições estranhas.", "Uma porta desgastada com marcas de garras.", "Uma porta reluzente e dourada."],
                ["Uma porta de madeira com entalhes misteriosos.", "Uma porta adornada com joias brilhantes.", "Uma porta com enfeites mágicos."],
                ["Uma porta de ferro maciço com crânios esculpidos.", "Uma porta com runas ancestrais.", "Uma porta selada com símbolos estranhos."]
            ],
            [
                ["Uma porta coberta de musgo e líquen.", "Uma porta com ruídos estranhos vindos de dentro.", "Uma porta com esqueletos à sua frente."],
                ["Uma porta com correntes enferrujadas.", "Uma porta trancada com cadeado.", "Uma porta com inscrições ameaçadoras."],
                ["Uma porta misteriosa com padrões geométricos.", "Uma porta com chamas que dançam.", "Uma porta selada com uma placa de metal."],
            ],
            [
                ["Uma porta com uma luz fraca saindo por baixo.", "Uma porta com inscrições em língua estranha.", "Uma porta trancada com uma corrente."],
                ["Uma porta que range quando tocada.", "Uma porta com olhos esculpidos.", "Uma porta ornamentada com desenhos abstratos."],
                ["Uma porta com entalhes de animais selvagens.", "Uma porta com uma inscrição enigmática.", "Uma porta com padrões intrincados."],
            ],
            [
                ["Uma porta com o som de risos do outro lado.", "Uma porta coberta de teias de aranha.", "Uma porta com um espelho embutido."],
                ["Uma porta com gotas de água caindo.", "Uma porta com símbolos celestiais.", "Uma porta com uma aura de mistério."],
                ["Uma porta com um brilho misterioso.", "Uma porta decorada com ossos.", "Uma porta com um aroma adocicado."]
            ]
        ]

        self.historia_index = 0
        self.mostrar_historia()

    def iniciar_jogo(self):
        self.nome_jogador = self.entry_nome.get()
        if self.nome_jogador:
            self.frame_nome.pack_forget()
            self.btn_proxima_fase.config(state=tk.NORMAL)
            self.mostrar_historia()

    def escolher_porta(self, porta_escolhida):
        if not self.ganhou:
            consequencia = random.randint(1, 4)

            if consequencia == porta_escolhida:
                self.mostrar_game_over()
            else:
                self.lbl_status.config(text=f"Você escolheu a porta {porta_escolhida}.\n{self.nome_jogador}, continue para a próxima fase!")
                self.proxima_fase()

    def proxima_fase(self):
        if self.fase_atual < 5:
            self.fase_atual += 1
            self.historia_index = 0  # Reinicia a história para a nova fase
            self.mostrar_historia()
            self.btn_proxima_fase.config(state=tk.DISABLED)
        else:
            self.lbl_status.config(text=f"Parabéns, {self.nome_jogador}! Você conseguiu superar o desafio!")

    def mostrar_historia(self):
        if self.historia_index < len(self.historia):
            self.lbl_status.config(text=self.historia[self.historia_index])
            self.historia_index += 1
        else:
            self.lbl_status.config(text=f"Fase {self.fase_atual}: Você tem 3 portas à sua frente.")
            self.atualizar_descricoes_portas()

    def atualizar_descricoes_portas(self):
        porta_descricoes = self.fase_info[self.fase_atual - 1]
        for i, porta in enumerate(self.portas):
            descricao = porta_descricoes[self.historia_index - 1][i]
            porta.config(text=f"Porta {i + 1}\n{descricao}")

    def mostrar_game_over(self):
        self.ganhou = False
        self.lbl_status.config(text=f"Você escolheu a porta errada.\n{self.nome_jogador}, o jogo acabou!")
        self.btn_proxima_fase.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDasPortas(root)
    root.mainloop()
