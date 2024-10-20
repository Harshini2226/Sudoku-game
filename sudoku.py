import tkinter as tk
from tkinter import messagebox


class Sudoku:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")

        self.cells = [[None for _ in range(9)] for _ in range(9)]

        # Sample sudoku grid (0 represents empty cells)
        self.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        self.create_board()
        self.create_buttons()

    def create_board(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    cell = tk.Entry(self.root, width=2, font=("Arial", 18), justify="center")
                    cell.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)
                    self.cells[i][j] = cell
                else:
                    label = tk.Label(self.root, text=str(self.grid[i][j]), width=2, font=("Arial", 18), bg="light gray")
                    label.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)

    def create_buttons(self):
        check_button = tk.Button(self.root, text="Check", command=self.check_solution)
        check_button.grid(row=9, column=0, columnspan=4, pady=20)

        reset_button = tk.Button(self.root, text="Reset", command=self.reset_board)
        reset_button.grid(row=9, column=5, columnspan=4, pady=20)

    def check_solution(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    try:
                        value = int(self.cells[i][j].get())
                        if not (1 <= value <= 9):
                            raise ValueError
                        self.grid[i][j] = value
                    except ValueError:
                        messagebox.showerror("Error", f"Invalid entry at row {i+1}, column {j+1}. Enter a number between 1 and 9.")
                        return

        if self.is_valid_sudoku():
            messagebox.showinfo("Success", "Congratulations! You solved the Sudoku correctly.")
        else:
            messagebox.showerror("Error", "Incorrect solution. Try again!")

    def reset_board(self):
        self.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.cells[i][j].delete(0, tk.END)

    def is_valid_sudoku(self):
        # Check rows, columns, and 3x3 boxes for duplicate numbers
        def check_unit(unit):
            unit = [num for num in unit if num != 0]
            return len(unit) == len(set(unit))

        for row in self.grid:
            if not check_unit(row):
                return False

        for col in zip(*self.grid):
            if not check_unit(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [self.grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not check_unit(box):
                    return False

        return True


if __name__ == "__main__":
    root = tk.Tk()
    game = Sudoku(root)
    root.mainloop()
