import tkinter as tk
from tkinter import messagebox
import pygame

# Inicializar pygame para los sonidos
pygame.mixer.init()

# Cargar sonidos
click_sound = pygame.mixer.Sound("mov.wav")
win_sound = pygame.mixer.Sound("victory.wav")
draw_sound = pygame.mixer.Sound("empate.wav")

# Función para reproducir sonido
def play_sound(sound):
    sound.play()

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya")
        self.player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font='normal 20 bold', width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def on_click(self, index):
        if self.board[index] == "":
            play_sound(click_sound)
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_winner():
                play_sound(win_sound)
                messagebox.showinfo("Ganador", f"El jugador {self.player} ha ganado!")
                self.reset_game()
            elif "" not in self.board:
                play_sound(draw_sound)
                messagebox.showinfo("Empate", "Es un empate!")
                self.reset_game()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
