#tic-tac-toe 

#procedual implimentaion


winning_combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

board = ["-"] * 9

def display_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

def winner(player):
    for combo in winning_combos:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def take_turn(player):
    print("It's player " + player + "'s turn")
    move = int(input("Enter move index (1-9): "))
    board[move-1] = player
    
def game_loop():
    for player in ["o","x","o","x","o","x","o","x","o"]:
#   for i in ["o"] + ["x","o"] * 4 
        display_board()
        take_turn(player)
        if winner(player):
            display_board()
            print("Player " + player + " wins")
            break

def main():
    game_loop()

if __name__ == "__main__":
    main()


