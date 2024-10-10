#tic-tac-toe-Object-Oriented

#  0 1 2
#  3 4 5
#  6 7 8

class Board:
    winning_combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    board = ["-"] * 9

    def display(self):
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])

    def winner(self,player):
        for combo in self.winning_combos:
            if self.board[combo[0]] == player and self.board[combo[1]] == player and self.board[combo[2]] == player:
                print(combo)
                return True
        return False
        
    def add(self,move,player):
        self.board[move-1] = player

class Game:
    
    def __init__(self, board):
        self.board = board
        self.turns = ["o","x","o","x","o","x","o","x","o"]

    def take_turn(self,player):
        print("It's player " + player + "'s turn")
        move = int(input("Enter move index (1-9): "))
        self.board.add(move,player)
        
    def play(self):
        player = self.turns.pop()
        self.board.display()
        self.take_turn(player)
        
    def ended(self):
        return len(self.turns) == 0

def main():
    board = Board() #create new instance of board object
    game = Game(board)
    
    while not game.ended():
        game.play()
        if board.winner("x"):
            board.display()
            print("Player X is the winner")
            break
        if board.winner("o"):
            board.display()
            print("Player O is the winner")
            break

if __name__ == "__main__":
    main()