class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.cols = [0] * n
        self.rows = [0] * n
        self.diagonal = 0
        self.a_diagonal = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        curr_player = 1 if player == 1 else -1

        self.cols[col] += curr_player
        self.rows[row] += curr_player
        
        if row == col:
            self.diagonal += curr_player
        
        if row + col == self.n - 1:
            self.a_diagonal += curr_player

        if (abs(self.cols[col]) == self.n or
            abs(self.rows[row]) == self.n or 
            abs(self.diagonal) == self.n or
            abs(self.a_diagonal) == self.n):
            return player

        return 0
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
