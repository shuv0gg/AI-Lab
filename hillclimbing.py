import random

class EightQueens:
    def __init__(self):
        # Initialize the board with one queen in each row, placed randomly in one of the columns.
        self.board = [random.randint(0, 7) for _ in range(8)]

    def print_board(self):
        # Print the board for visualization
        for row in range(8):
            line = ""
            for col in range(8):
                if self.board[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()

    def calculate_conflicts(self, board):
        # Calculate the number of conflicts (queens attacking each other) for a given board state.
        conflicts = 0
        for row1 in range(8):
            for row2 in range(row1 + 1, 8):
                if board[row1] == board[row2]:  # Same column
                    conflicts += 1
                if abs(board[row1] - board[row2]) == abs(row1 - row2):  # Same diagonal
                    conflicts += 1
        return conflicts

    def hill_climb(self):
        # Perform simple hill climbing until we reach a solution or a local maxima.
        current_conflicts = self.calculate_conflicts(self.board)

        while True:
            # Flag to check if we find a better neighbor
            found_better = False

            # Try moving each queen (in each row) to a different column
            for row in range(8):
                original_col = self.board[row]  # Remember the original column of the queen
                for col in range(8):
                    if col != original_col:  # Move to a different column
                        new_board = self.board[:]  # Copy the current board
                        new_board[row] = col  # Move the queen to the new column
                        new_conflicts = self.calculate_conflicts(new_board)  # Calculate conflicts for the new board

                        if new_conflicts < current_conflicts:  # If we find a better board
                            self.board = new_board  # Accept the new board
                            current_conflicts = new_conflicts  # Update current conflicts
                            found_better = True  # Set the flag to true
                            break  # Move on without checking further neighbors

                if found_better:
                    break  # Move to the next iteration with the new board

            if not found_better:  # If no better neighbor was found, we are stuck
                break

        return current_conflicts == 0  # Return True if no conflicts remain (solution found)

# Example usage:
solver = EightQueens()  # Create an 8-Queens solver object
print("Initial board:")
solver.print_board()  # Print the initial random board

if solver.hill_climb():  # Run the hill climbing algorithm
    print("Solution found:")
else:
    print("Local maximum reached, no solution found:")
solver.print_board()  # Print the final board (solution or local maximum)
