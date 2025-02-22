import tkinter as tk
import random
import subprocess
from tkinter import messagebox

def homePage():
    # Jalankan program Python lain yang bernama 'other_program.py'
    root.destroy()
    subprocess.run(["python", "homePage.py"])

# Ukuran papan NxN untuk N-Knight Problem
N = 4

# Solusi valid yang diberikan
valid_solutions = [
    [0, 1, 11, 14], [9, 11, 12, 14], [0, 2, 5, 15], [0, 5, 10, 15], [5, 8, 10, 15], 
    [0, 1, 2, 15], [1, 4, 6, 11], [1, 6, 11, 12], [0, 2, 3, 13], [4, 5, 6, 7], 
    [0, 1, 2, 3], [4, 9, 11, 14], [1, 4, 14, 15], [0, 1, 3, 14], [1, 12, 14, 15], 
    [2, 12, 13, 15], [1, 3, 4, 6], [0, 1, 14, 15], [12, 13, 14, 15], [0, 2, 5, 7], 
    [1, 3, 6, 12], [2, 3, 8, 13], [2, 8, 13, 15], [2, 3, 12, 13], [3, 6, 9, 12], 
    [8, 9, 10, 11], [1, 2, 3, 12], [0, 3, 7, 13], [2, 7, 8, 13], [1, 2, 12, 15], 
    [2, 5, 7, 8], [0, 3, 13, 14]
]

def get_conflicts(board):
    """Function to calculate the number of conflicts on the board."""
    conflicts = 0
    
    # All possible moves a knight can make
    knight_moves = [
        (-2, -1), (-2, 1),  # Two up, one left or right
        (-1, -2), (-1, 2),  # One up, two left or right
        (1, -2), (1, 2),    # One down, two left or right
        (2, -1), (2, 1)     # Two down, one left or right
    ]
    
    # Check for every knight on the board
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:  # There's a knight at this position
                for move in knight_moves:
                    new_row, new_col = row + move[0], col + move[1]
                    if 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] == 1:
                        conflicts += 1

    return conflicts // 2  # Dividing by 2 to avoid double counting

def random_board():
    """Generates a random board configuration."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # Place one knight randomly in each column
    for col in range(N):
        row = random.randint(0, N-1)
        board[row][col] = 1
    
    return board

def hill_climbing(board):
    """Hill Climbing algorithm to minimize the number of conflicts."""
    current_board = board
    current_conflicts = get_conflicts(current_board)
    
    steps = [(current_board, current_conflicts)]  # Track steps for visualization

    while True:
        # Jika tidak ada konflik lagi, selesai
        if current_conflicts == 0:
            return steps  # Return all steps for visualization

        neighbors = []
        
        # Generate all possible neighbors by moving knights
        for col in range(N):
            for row in range(N):
                if current_board[row][col] == 0:  # Move knight to new position
                    new_board = [r[:] for r in current_board]
                    for r in range(N):
                        new_board[r][col] = 0  # Clear current knight in the column
                    new_board[row][col] = 1  # Place knight in new row
                    neighbors.append((new_board, get_conflicts(new_board)))

        # Cari tetangga dengan konflik paling sedikit
        neighbors.sort(key=lambda x: x[1])
        best_neighbor, best_conflicts = neighbors[0]

        # Jika tidak ada perbaikan, berhenti (local optima)
        if best_conflicts >= current_conflicts:
            return steps  # Return all steps for visualization

        # Update current state ke neighbor terbaik
        current_board = best_neighbor
        current_conflicts = best_conflicts
        steps.append((current_board, current_conflicts))  # Track steps

class FullScreenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("N-Knight Problem")
        self.root.attributes("-fullscreen", True)  # Fullscreen mode
        self.root.resizable(True, True)  # Resizable sesuai layar
        self.clicked_buttons = []

        # Tambahkan padding untuk label atas
        self.label = tk.Label(root, text="N-Knight Problem", font=("Lucida Console", 32, "bold"), fg="black")
        self.label.pack(pady=(60, 0))  # Lebih banyak padding di atas

        self.grid_frame = tk.Frame(root, bg="#B7B7B7")  # Warna latar grid hitam
        self.grid_frame.pack(expand=True, pady=(50, 10))  # Padding tambahan untuk grid

        self.buttons = []
        self.create_grid()

        # Button dengan lebar yang sama dan warna yang diminta
        button_width = 20

        self.submit_button = tk.Button(root, text="Check", command=self.check_answer, font=("verdana", 18), bg="#0D92F4", fg="white", width=button_width)
        self.submit_button.pack(pady=(10, 10), padx=20)  # Padding dan lebar seragam

        self.ai_button = tk.Button(root, text="See AI Solve", command=self.solve_with_ai, font=("verdana", 18), bg="#77CDFF", fg="white", width=button_width)
        self.ai_button.pack(pady=(10, 10), padx=20)  # Padding dan lebar seragam

        self.reset_button = tk.Button(root, text="Reset Board", command=self.reset_game, font=("verdana", 18), bg="#F95454", fg="white", width=20)
        self.reset_button.pack(pady=(10, 80), padx=20)  # Padding bawah diperbesar menjadi 50 agar lebih jauh dari bawah layar

        # Pindahkan tombol Home Page ke atas tombol The Rules
        button_width = 12  # Atur lebar tombol agar sama
        
        self.home_button = tk.Button(root, text="Home Page", command=homePage, font=("verdana", 12), bg="#B7B7B7", fg="white", width=button_width)
        self.home_button.place(relx=0.02, rely=0.05, anchor="nw")  # Atur jarak ke kiri dan posisi

        self.rules_button = tk.Button(root, text="The Rules", command=self.show_rules, font=("verdana", 12), bg="#B7B7B7", fg="white", width=button_width)
        self.rules_button.place(relx=0.02, rely=0.1, anchor="nw")  # Tempatkan di bawah Home Page dengan lebar sama

        # Panggil messagebox untuk menampilkan peraturan saat aplikasi dimulai
        self.show_rules()

        self.randomize_buttons()

    def create_grid(self):
        """Create 4x4 grid of buttons."""
        for row in range(N):
            for col in range(N):
                button = tk.Button(self.grid_frame, width=10, height=3, font=("arial", 12),
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons.append(button)

    def randomize_buttons(self):
        """Randomly place 4 knights on different columns."""
        self.clicked_buttons.clear()
        for button in self.buttons:
            button.config(bg="SystemButtonFace", text="")

        # Generate random knight positions
        initial_board = random_board()
        for row in range(N):  # FIXED: Iterate by rows, then columns
            for col in range(N):
                if initial_board[row][col] == 1:
                    index = row * 4 + col  # FIXED: Row * N + col
                    self.buttons[index].config(bg="#1E201E", text="K", font=("arial"), fg = "white")
                    self.clicked_buttons.append(index)

    def on_button_click(self, row, col):
        """Handle button click, toggle color between red and default, and store/remove index."""
        index = row * 4 + col
        button = self.buttons[index]

        if index in self.clicked_buttons:
            button.config(bg="SystemButtonFace", text="")
            self.clicked_buttons.remove(index)
        elif len(self.clicked_buttons) < 4:
            button.config(bg="#1E201E", text="K", font=("arial"), fg = "white")
            self.clicked_buttons.append(index)
        else:
            messagebox.showwarning("Limit Reached", "You can only select up to 4 knights. Remove one to add another.")

    def check_answer(self):
        """Check if player's selected buttons match one of the correct solutions."""
        current_board = self.get_current_board()
        clicked_positions = sorted(self.clicked_buttons)

        if clicked_positions in valid_solutions:
            messagebox.showinfo("Success!", "Congratulations! You solved the N-Knight problem with a correct solution!")
            self.reset_game()
        else:
            conflicts = get_conflicts(current_board)
            if conflicts == 0:
                messagebox.showinfo("Correct but Unverified", "You found a valid solution with no conflicts!")
            else:
                messagebox.showerror("Conflicts", f"There are {conflicts} conflicts. Try again!")

    def reset_game(self):
        """Reset the buttons' colors, clear clicked buttons list, and randomize buttons again."""
        self.randomize_buttons()

    def go_home(self):
        """Simulate going back to the home page (implement logic as needed)."""
        messagebox.showinfo("Home Page", "Returning to the home page!")

    def show_rules(self):
        rules_text = (
                "1. Make sure that there is only 1 chess piece in each column\n"
                "2. Place 4 knights without them attacking each other.\n"
                "3. Knights attack with an 'L' shaped move:\n"
                "   - Two squares in one direction and one square in a perpendicular direction.\n"
            )
        """Show message box with the game rules."""
        messagebox.showinfo("Game Rules", rules_text)

    def get_current_board(self):
        """Mendapatkan representasi papan saat ini dari grid GUI."""
        board = [[0 for _ in range(N)] for _ in range(N)]
        for index in self.clicked_buttons:
            row = index // 4
            col = index % 4
            board[row][col] = 1
        return board

    def solve_with_ai(self):
        """Solve the N-Knight problem using AI and display the steps."""
        current_board = self.get_current_board()
        
        # Solve using the hill climbing algorithm and return steps
        steps = hill_climbing(current_board)
        
        # Display the solved board step by step
        if steps[-1][1] == 0:
            self.show_steps(steps)
            # Update clicked_buttons sesuai dengan solusi AI
            self.clicked_buttons.clear()
            final_board = steps[-1][0]
            for row in range(N):
                for col in range(N):
                    if final_board[row][col] == 1:
                        index = row * N + col
                        self.clicked_buttons.append(index)
        else:
            messagebox.showinfo("Restart", "Current board can't be solved, restarting with a new random board.")
            self.reset_game()

    def show_steps(self, steps):
        """Menampilkan langkah-langkah penyelesaian pada grid."""
        for i, (step_board, conflicts) in enumerate(steps):
            self.root.after(i * 1000, self.update_grid, step_board)

    def update_grid(self, board):
        """Memperbarui warna tombol sesuai dengan langkah saat ini."""
        for col in range(N):
            for row in range(N):  # FIXED: Correct row/col iteration
                index = row * 4 + col
                if board[row][col] == 1:
                    self.buttons[index].config(bg="#0D92F4", text="K", font=("arial"), fg="black")
                else:
                    self.buttons[index].config(bg="SystemButtonFace", text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = FullScreenApp(root)
    root.mainloop()
