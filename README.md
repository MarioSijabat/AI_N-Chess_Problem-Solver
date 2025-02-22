# 🧩 AI Chess Problem Solver

Welcome to the **AI Chess Problem Solver**! This Python project leverages artificial intelligence algorithms to solve the classic **N-King**, **N-Knight**, and **N-Queen** problems. Through a friendly and interactive GUI built with `tkinter`, users can easily choose chess problems and let AI solve them step by step. Curious about how the algorithm works? Let’s dive into it!

## 🎯 Features

- **N-King Problem**: Place N kings on an NxN chessboard so that no two kings threaten each other. The AI uses **Hill Climbing** to find the solution.
- **N-Knight Problem**: Place N knights on an NxN chessboard such that no knights can attack each other. This is also solved using **Hill Climbing**.
- **N-Queen Problem**: Solve the classic **N-Queens** problem where queens must be placed in a way that no two queens attack each other. This uses **Hill Climbing with Random Restart**.
- **Interactive GUI**: An easy-to-use interface where you can manually place pieces or let the AI solve the problem for you. 
- **Step-by-Step Visualization**: Watch how the AI works through the problem in real-time by showing each step it takes to solve the puzzle!

## 🚀 Installation

Ready to try it out? Here’s how you can get it running locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-chess-problem-solver.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd ai-chess-problem-solver
   ```
3. **Install dependencies** (if needed):
   ```bash
   pip install tkinter
   ```
4. **Run the program**:
   ```bash
   python homePage.py
   ```

## 🧩 How to Play

Once the program is up and running, the fun begins! Here's what you can do:

### 🎮 Choose Your Problem
Select one of the chess problems:
- **N-King Problem**: Place kings on the board without them attacking each other.
- **N-Knight Problem**: Place knights on the board without them attacking each other.
- **N-Queen Problem**: Solve the famous N-Queens puzzle!

### 🤖 Let the AI Solve It!
- Hit **"See AI Solve"** and watch the AI solve the problem step by step.
- Curious about the process? Watch as the AI improves the board with each move!

### ✅ Check Your Solution
- After placing your pieces, press **"Check"** to see if the current configuration is a valid solution.

### 🔄 Reset the Board
- Press **"Reset Board"** to shuffle the pieces around and start fresh.

### 📜 Learn the Rules
- Tap **"The Rules"** to view the rules for the selected problem. It’s like having a chess guide in your pocket!

## 🧐 Example: N-Knight Problem

Here’s a sneak peek at the **N-Knight Problem**:

1. **Choose N-Knight**: Select the **N-Knight** button to begin the challenge.
2. **AI Solving**: Press **"See AI Solve"**, and the AI will place the knights on the board while ensuring no knight can attack another. You'll see it work in real-time!
3. **Check Solution**: If you think you’ve solved the problem, press **"Check"** to verify your solution.
4. **Reset and Try Again**: Want to try a different configuration? Hit **"Reset Board"**.

### 🎯 Example Walkthrough

- **Input**: User places knights on a 4x4 grid, ensuring no knight can attack each other.
- **Output**: The AI automatically solves the N-Knight problem, and you get to see every move!

## 🧠 AI Algorithms

The magic behind the scenes is powered by some cool AI algorithms:

- **Hill Climbing**: This algorithm finds the solution by iteratively moving to the neighbor with the least conflicts. If no improvement is found, the algorithm stops.
- **Random Restart Hill Climbing**: Used for N-Queens, this algorithm restarts the search multiple times if it gets stuck at a local optimum, ensuring the best solution is found.

## 🤝 Contributing

We'd love for you to contribute to the project! Here’s how you can get involved:

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Make your changes** and commit them (`git commit -am 'Add new feature'`).
4. **Push to the branch** (`git push origin feature-branch`).
5. **Open a pull request** and share your improvements with the community!
