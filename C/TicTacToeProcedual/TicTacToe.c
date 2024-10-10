#include <stdio.h>
#include <stdlib.h>
// Tic-tac-toe (procedural paradigm)

//  0 1 2
//  3 4 5
//  6 7 8

int winningCombos[8][3] = {{0,1,2},{3,4,5},{6,7,8},
                            {0,3,6},{1,4,7},{2,5,8},
                            {0,4,8},{2,4,6}};

char board[9] = {' ',' ',' ',' ',' ',' ',' ',' ',' '};

void displayBoard()
{
    printf("-------\n");
    printf("|%c|%c|%c|\n",board[0],board[1],board[2]);
    printf("-------\n");
    printf("|%c|%c|%c|\n",board[3],board[4],board[5]);
    printf("-------\n");
    printf("|%c|%c|%c|\n",board[6],board[7],board[8]);
    printf("-------\n");
}

int winner(char player)
{
    for(int i = 0; i < 8; i++)
        if(board[winningCombos[i][0]] == player && 
           board[winningCombos[i][1]] == player && 
           board[winningCombos[i][2]] == player)
            return 1;
    return 0;
}

    
void takeTurn(char player)
{
    printf("it's player %c's turn\n", player);
    printf("Enter move index (1-9): ");
    char * input[10]; // It uses fgets to read the user's input from the standard input stream (stdin) and stores it in the input array.
    fgets(input,10,stdin);
    int move = atoi(input); // It converts the input string to an integer using atoi and stores it in the move variable.
    board[move - 1] = player;// It updates the board array at the index corresponding to the player's move by assigning the player's symbol to the array element.
    printf("\n");
}

            
void tictactoe()
{
    char players[2] = {'O','X'};
    int playerIndex = 0;
    for(int i = 0; i < 9; i++)
    {
        char player = players[playerIndex];
        displayBoard();
        takeTurn(player);
        if(winner(player))
        {
            displayBoard();
            printf("Player %c wins!", player);
            break;
        }
        
        playerIndex = ! playerIndex;
    }
}

int main()
{    
    tictactoe();
    return 0;
}