"""
Tic-tac-toe is played on a three-by-three grid by two players, who alternately place the marks X and O in one of
the nine spaces in the grid.

Here, in this Game played between two players [Player_1, Player_2] Player_1 is always 'X' and Player_2 is always
'Y'.Since, there is no universally-agreed rule as to who plays first, but in this game the convention that X plays
first is used.

Win Condition:  The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is
the winner.
Draw Condition: It is a solved game, with a forced draw assuming best play from both players.

Create Board -> Create a game board [Why? -> Tic Tac Toe is totally based on X and O, we can represent them in arrays
like 'X' -> [1,0], 'O' -> [1,1] but it will be easier if we represent this in as a actual game for better understanding]
Properties of Board:
1) At first, empty game board with columns and rows named from 1 to 9

2) Display the board

3) Update cells -> To enter X choice and O choice [Note: if already X choice or choice in updated cells, it should ask
another input from person who entered wrong input]

4) Check Win -> There are 8 win conditions:
    Condition 1 to 3 -> All rows with same player, that is Cells[1, 2, 3] == 'X'|'O' -> X|O Wins
    Cells[4, 5, 6] == 'X'|'O' -> X|O Wins, Cells[7, 8, 9] == 'X'|'O' -> X|O Wins
    Condition 4 to 6 -> All columns with same player, that is Cells[1, 4, 7] == 'X'|'O' -> X|O Wins
    Cells[2, 5, 8] == 'X'|'O' -> X|O Wins, Cells[3, 6, 9] == 'X'|'O' -> X|O Wins
    Condition  7 and 8 -> Two diagonals with same player, that is Cells[1, 5, 9] == 'X'|'O' -> X|O Wins
    Cells[3, 5, 7] == 'X'|'O' -> X|O Wins.

5) Check Tie -> if all the cells are filled and there is no way to continue the game then it is a Tie Game.

**************************** Very Simple Game for basic OOP concept ****************************************
"""