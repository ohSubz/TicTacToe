###TIC TAC TOE ###
print("Herzlich Willkommen zu einer Runde Tic Tac Toe.")
#Erstellen des nummerierten Spielbretts#
def create_numbered_board():
    return [str(i) for i in range(1, 10)]
# Das Spielbrett darstellen #
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))                                         #Erstellt jede Zeile des Spielfelds.
        if i < 6:
            print("-" * 9)
#Erstellen des Spielzugs der Spieler#
def make_move(board, player):
    while True:
        try:
            move = int(input(f"Spieler {player}, wähle ein Feld (1-9): ")) - 1  #Hier wird die Eingabe erstellt, -1 für die Pythonsyntax.
            if 0 <= move <= 8 and board[move] not in ["X", "O"]:
                board[move] = player                                            #Aktualisierung des Spielbrettes nach Eingabe.
                return
            else:
                print("Ungültiges Feld, bitte wähle ein anderes.")              #Fehlermeldung bei belegtem Feld oder zu hoher Zahl.
        except ValueError:
            print("Bitte gib eine Zahl ein.")                                   #Fehlermeldung wenn keine Zahl eingegeben wurde.

### Die Gewinnmöglichkeiten erschaffen ###
            
def check_win(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertikal
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]                                          #Gewinnausgabe bei erfüllter Gewinnbedingung.
    return None                                                                 #None bei keinem Gewinner.

###Spielablauf###

def play_game():
    board = create_numbered_board()                                             #Initialisierung des Spielfeldes
    current_player = "X"                                                        #Startspieler ist automatisch Spieler X
    move_count = 0                                                              #Zählt die Züge um ein Unentschieden fest stellen zu können.

    while True:
        print_board(board)                                                      #Zeigt das aktuelle Spielbrett.
        make_move(board, current_player)                                        #Verarbeitung des Spielzuges.
        move_count += 1                                                         
        
        if move_count >= 5:                                                     #Ein Gewinn ist erst ab 5 Zügen möglich.
            winner = check_win(board)
            if winner:
                print_board(board)
                print(f"Spieler {winner} hat gewonnen!")                        #Gewinner wird verkündet.
                break
            elif move_count == 9:                                               #Bei 9 Zügen gibt es keinen Gewinner.
                print("Unentschieden!")
                break

        current_player = "O" if current_player == "X" else "X"                  #Wechsel der Spieler.


if __name__ == "__main__":                                                      #Startet das Tic Tac Toe Spiel.
    play_game()