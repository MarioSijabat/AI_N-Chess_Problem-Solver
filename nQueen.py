import tkinter as tk
import random
import subprocess
from tkinter import messagebox

def homePage():
    # Jalankan program Python lain yang bernama 'other_program.py'
    root.destroy()
    subprocess.run(["python", "homePage.py"])

# Ukuran papan NxN
N = 4

def printSolution(board):
    """Menampilkan solusi papan dengan Q sebagai ratu."""
    return [" ".join("Q" if i == row else "." for i in range(N)) for row in board]

def get_conflicts(board):
    """Menghitung total konflik (ratu yang saling menyerang)."""
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def generate_neighbors(board):
    """Menghasilkan tetangga dengan memindahkan satu ratu ke baris yang berbeda di kolom yang sama."""
    neighbors = []
    for col in range(N):
        for row in range(N):
            if board[col] != row:  # Jika ratu tidak berada di baris yang sama
                new_board = board[:]
                new_board[col] = row  # Pindahkan ratu ke baris baru
                neighbors.append(new_board)
    return neighbors

def hill_climbing(board):
    """Hill Climbing untuk mengurangi konflik pada papan."""
    current_board = board
    current_conflicts = get_conflicts(current_board)
    steps = [current_board[:]]  # Untuk menyimpan langkah-langkah

    while True:
        if current_conflicts == 0:
            return steps  # Kembalikan langkah-langkah ketika solusi ditemukan

        neighbors = generate_neighbors(current_board)
        # Pilih tetangga dengan konflik paling sedikit
        best_neighbor = min(neighbors, key=get_conflicts)
        best_conflicts = get_conflicts(best_neighbor)

        if best_conflicts >= current_conflicts:
            return steps  # Berhenti jika tidak ada perbaikan

        current_board = best_neighbor
        current_conflicts = best_conflicts
        steps.append(current_board[:])  # Simpan langkah saat ini

def random_board():
    """Menghasilkan papan acak dengan satu ratu di setiap kolom."""
    return [random.randint(0, N - 1) for _ in range(N)]

def solveNQ_with_restart():
    """Hill Climbing dengan Random Restart untuk mengurangi konflik pada papan."""
    for _ in range(1000):  # Batasi jumlah restart
        board = random_board()
        result = hill_climbing(board)
        last_step = result[-1]
        if get_conflicts(last_step) == 0:
            return result  # Jika solusi ditemukan, kembalikan langkah-langkahnya
    return None

class FullScreenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("N-Queens Game")
        self.root.attributes("-fullscreen", True)  # Fullscreen mode
        self.root.resizable(True, True)  # Resizable sesuai layar
        self.clicked_buttons = []

        # Variabel-variabel solusi yang benar
        self.var1 = [1, 4, 10, 15]
        self.var2 = [2, 4, 11, 13]  # Solusi optimal
        self.var3 = [2, 5, 11, 12]
        self.var4 = [1, 7, 8, 14]  # Solusi optimal
        self.var5 = [1, 6, 8, 15]
        self.var6 = [1, 7, 8, 14]
        self.var7 = [1, 7, 10, 12]
        self.var8 = [0, 6, 11, 13]
        self.var9 = [0, 5, 11, 14]
        self.var10 = [3, 4, 10, 13]
        self.var11 = [3, 5, 8, 14]
        self.var12 = [0, 6, 9, 15]
        self.var13 = [2, 7, 9, 12]
        self.var14 = [3, 5, 10, 12]
        self.var15 = [2, 4, 9, 15]
        self.var16 = [3, 6, 8, 13]
        self.var17 = [0, 7, 9, 14]

        # Tambahkan padding untuk label atas
        self.label = tk.Label(root, text="N-Queens Problem", font=("Lucida Console", 32, "bold"), fg="black")
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

        self.reset_button = tk.Button(root, text="Reset Board", command=self.reset_game, font=("verdana", 18), bg="#F95454", fg="white", width=button_width)
        self.reset_button.pack(pady=(10, 80), padx=20)  # Padding bawah diperbesar menjadi 50 agar lebih jauh dari bawah layar


        # Pindahkan tombol Home Page ke atas tombol The Rules
        button_width = 12  # Atur lebar tombol agar sama
        
        self.home_button = tk.Button(root, text="Home Page", command=homePage, font=("verdana", 12), bg="gray", fg="white", width=button_width)
        self.home_button.place(relx=0.02, rely=0.05, anchor="nw")  # Atur jarak ke kiri dan posisi

        self.rules_button = tk.Button(root, text="The Rules", command=self.show_rules, font=("verdana", 12), bg="gray", fg="white", width=button_width)
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
        """Randomly place 4 queens on different columns."""
        self.clicked_buttons.clear()
        for button in self.buttons:
            button.config(bg="SystemButtonFace", text="")

        positions = random.sample(range(4), 4)
        for col in range(4):
            row = positions[col]
            index = row * 4 + col
            self.buttons[index].config(bg="#1E201E", text="Q", font=("arial"), fg = "white")
            self.clicked_buttons.append(index)

    def on_button_click(self, row, col):
        """Handle button click, toggle color between red and default, and store/remove index."""
        index = row * 4 + col
        button = self.buttons[index]

        if index in self.clicked_buttons:
            button.config(bg="SystemButtonFace", text="")
            self.clicked_buttons.remove(index)
        elif len(self.clicked_buttons) < 4:
            button.config(bg="#1E201E", text="Q", font=("arial"), fg = "white")
            self.clicked_buttons.append(index)
        else:
            messagebox.showwarning("Limit Reached", "You can only select up to 4 queens. Remove one to add another.")

    def check_answer(self):
        """Check if player's selected buttons match one of the correct solutions."""
        if len(self.clicked_buttons) == 4:
            result = self.is_solution_valid()
            if result == "optimal":
                messagebox.showinfo("Optimal Solution!", "Congratulations! You solved the problem with the most optimal solution!")
                self.reset_game()
            elif result == "less_optimal":
                # Opsi bagi pemain untuk melanjutkan atau lanjut ke board lain
                continue_play = messagebox.askyesno("Less Optimal Solution", "Good job! You solved the problem, but there's a more optimal solution. Do you want to continue to find the optimal solution?")
                if continue_play:
                    messagebox.showinfo("Continue", "Try to find the optimal solution on this board!")
                else:
                    self.reset_game()  # Reset papan untuk tantangan baru
            else:
                messagebox.showerror("Incorrect", "Incorrect solution! Try again.")
        else:
            messagebox.showerror("Incomplete", "You must place exactly 4 queens!")

    def is_solution_valid(self):
        """Periksa apakah posisi yang dipilih pemain sesuai dengan salah satu variabel yang benar dan cek apakah optimal."""
        optimal_solutions = [self.var2, self.var4]
        other_solutions = [
            self.var1, self.var3, self.var5, self.var6, self.var7, self.var8, self.var9, 
            self.var10, self.var11, self.var12, self.var13, self.var14, self.var15, 
            self.var16, self.var17
        ]
        
        # Urutkan clicked_buttons untuk memastikan urutan tidak mempengaruhi pengecekan
        clicked_buttons_sorted = sorted(self.clicked_buttons)

        # Bandingkan dengan solusi optimal
        for solution in optimal_solutions:
            if clicked_buttons_sorted == sorted(solution):
                return "optimal"  # Solusi optimal

        # Bandingkan dengan solusi lain
        for solution in other_solutions:
            if clicked_buttons_sorted == sorted(solution):
                return "less_optimal"  # Solusi kurang optimal

        return "incorrect"  # Jika tidak ada yang cocok

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
                "3. Queens can attack in rows, columns, and diagonals.\n"
            )
        """Show message box with the game rules."""
        messagebox.showinfo("Game Rules", rules_text)
        
    def get_current_board(self):
        """Mendapatkan representasi papan saat ini dari grid GUI."""
        board = [-1] * N
        for index in self.clicked_buttons:
            row = index // 4
            col = index % 4
            board[row] = col
        return board

    def solve_with_ai(self):
        """Solve the N-Queens problem using AI and display the steps."""
        # Ambil papan saat ini dari grid GUI
        current_board = self.get_current_board()
        
        # Coba pecahkan papan saat ini dengan Hill Climbing
        steps = hill_climbing(current_board)
        last_step = steps[-1]

        if get_conflicts(last_step) == 0:
            # Jika papan saat ini bisa diselesaikan, tampilkan langkah-langkah penyelesaian
            self.show_steps(steps)
            
            # Update clicked_buttons sesuai dengan solusi AI
            self.clicked_buttons.clear()  # Bersihkan clicked_buttons sebelumnya
            for col in range(N):
                row = last_step[col]
                index = row * N + col  # Hitung indeks yang sesuai dengan posisi ratu AI
                self.clicked_buttons.append(index)  # Simpan ke clicked_buttons
        
        else:
            # Jika tidak bisa diselesaikan, lakukan random restart
            messagebox.showinfo("Restart", "Current board can't be solved, restarting with a new random board.")
            steps = solveNQ_with_restart()
            if steps:
                self.show_steps(steps)
                
                # Update clicked_buttons sesuai dengan solusi AI
                last_step = steps[-1]
                self.clicked_buttons.clear()
                for col in range(N):
                    row = last_step[col]
                    index = row * N + col
                    self.clicked_buttons.append(index)
            else:
                messagebox.showinfo("No Solution", "No solution found within the search limits.")

    def show_steps(self, steps):
        """Menampilkan langkah-langkah penyelesaian pada grid."""
        for step_index, step in enumerate(steps):
            self.root.after(step_index * 1000, self.update_grid, step)
        self.root.after(len(steps) * 1000, self.finalize_solution, steps[-1])

    def update_grid(self, board):
        """Memperbarui warna tombol sesuai dengan langkah saat ini."""
        for col in range(N):
            index = col * 4 + board[col]
            self.buttons[index].config(bg="#0D92F4", text="Q", font=("arial"), fg = "black")

        for col in range(N):
            for row in range(N):
                if board[col] != row:
                    index = col * 4 + row
                    self.buttons[index].config(bg="SystemButtonFace", text="")

    def finalize_solution(self, last_board):
        """Tinggalkan solusi akhir berwarna hijau dan reset yang lain."""
        for col in range(N):
            index = col * 4 + last_board[col]
            self.buttons[index].config(bg="#0D92F4", text="Q", font=("arial"), fg = "black")

        for col in range(N):
            for row in range(N):
                if last_board[col] != row:
                    index = col * 4 + row
                    self.buttons[index].config(bg="SystemButtonFace", text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = FullScreenApp(root)
    root.mainloop()
