import tkinter as tk
from tkinter import messagebox


class Sudoku:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku")
        self.window.config(bg='white')
        self.entries = {}
        self.board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        for i in range(9):
            for j in range(9):
                value = self.board[i][j]
                e = tk.Entry(self.window, width=5,font=("arial", 24), borderwidth=5)
                e.grid(row=i, column=j)
                if value != 0:
                    e.insert(tk.END, str(value))
                    e.configure(state="disabled")
                self.entries[(i, j)] = e

        tk.Button(self.window,height=3,width=10, font=("arial", 13), text="Check", command=self.check_solution).grid(row=9, column=0, columnspan=9, pady=10)

    def check_solution(self):
        board = [[self.entries[(i, j)].get() for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == "":
                    messagebox.showerror("Error", "Please fill all cells")
                    return
                if board[i][j].isalpha():
                    messagebox.showerror("Error", f"Invalid Number at Row:{i + 1} Column:{j + 1}")
                    return
                if not board[i][j].isdigit() or int(board[i][j]) < 1 or int(board[i][j]) > 9:
                    messagebox.showerror("Error", "Invalid input. Please enter a number between 1 and 9")
                    return

        for i in range(9):
            row = [board[i][j] for j in range(9)]
            column = [board[j][i] for j in range(9)]
            if not self.is_valid(row) or not self.is_valid(column):
                messagebox.showerror("Failed", "Wrong Solution!. You Failed. Duplicate number in row or column")
                return

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid(box):
                    messagebox.showerror("Failed", "Wrong Solution!. You Failed")
                    return

        messagebox.showinfo("Congratulations", "You solved the Sudoku!")

    def is_valid(self, numbers):
        return len(set(numbers)) == 9

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.run()
