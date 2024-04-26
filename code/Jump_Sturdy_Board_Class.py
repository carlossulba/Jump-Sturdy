class JumpSturdyBoard:
    def __init__(self):
        # initialisiere leeres board
        # leere BitBoards die zum Board gehören
        #Array mit allen Bit Boards der Figuren aus Jump-Sturdy bestehen
        self.pieceBB = [0b0, 0b0, 0b0, 0b0, 0b0, 0b0]
        #Repräsentation von leeren Feldern in einem BB
        self.emptyBB = 0b0
        #Repräsentation von besetzten Feldern in einem BB
        self.occupiedBB = 0b0
        # move-History einfüge
        self.move_history = ["123"] 
        
    def turn_counter(self):
        # zähle die Anzahl an Zügen
        self.turn_counter += 1

    def fen_notation_into_bb(self, notation):
        #Auslesen der vorgegebenen String Notation vom Server in unsere BitBoards für Pieces
        binary = ""
        boardPos = 59
        i = 0
        #Gehe die String Notation bis zum Schluss durch.
        while i < len(notation):
            #Setze den String in eine Binäre Darstellung und befülle ihn 60 mal mit der "0", weil unsere BitBoards nur 60 Felder haben.
            binary = "0"*60
            #Teile den String an der Board Position in der wir uns gerade gefinden und setze eine 1 dazwischen. 
            binary = binary[boardPos+1:] + "1" + binary[0:boardPos]
            #Schaue ob das Zeichen aus der Notation ein "r" ist.
            if notation[i] == "r":
                #Schaue, ob das nächste Zeichen aus der Notation ebenfalls ein "r" ist, denn daraus Ergibt sich ein Pferd.
                if notation[i] == notation[i + 1]:
                    #Wandle den String in ein binäres int um und addiere es auf das aktuelle BitBoard für rote Pferde. 
                    self.pieceBB[2]+=int(binary,2)
                #Schaue, ob das nächste Zeichen aus der Notation ein "b" ist, denn daraus Ergibt sich ein captured red pawn(Mir fällt der deutsche Name nicht ein).
                elif notation[i+1] == "b":
                    #Wandle den String in ein binäres int um und addiere es auf das aktuelle BitBoard für captured red pawn.
                    self.pieceBB[4] += int(binary, 2)
                else:
                    #Wandle den String in ein binäres int um und addiere es auf das aktuelle BitBoard für rote Bauern.
                    self.pieceBB[0] += int(binary, 2)
            #Falls das Zeichen ein "/" soll dieser Schleifendurchlauf überprüfen werden, da es kein Zeichen ist, welches im Board notwendig ist.
            elif notation[i] == "/":
                i += 1
                continue
            #Falls das Zeichen aus der Notation ein "b" ist.
            elif notation[i] == "b":
                if notation[i] == notation[i + 1]:
                    #Wandle den String in ein binäres int um und addiere es auf das aktuelle BitBoard für blaue Pferde. 
                    self.pieceBB[3] += int(binary, 2)
                elif notation[i+1] == "r":
                    #Wandle den String in ein binäres int um und addiere es auf das aktuelle BitBoard für captured blue pawn.
                    self.pieceBB[5] += int(binary, 2)
                else:
                    #Wandle den String in ein binäres int um und addiere es auf das aktuelle BitBoard für blaue Bauern.
                    self.pieceBB[1] += int(binary, 2)
            #Falls das Zeichen aus der Notation eine Zahl ist.
            else:
                #Reduziere die Board Position um die angegebene Zahl für die leeren Felder. 
                boardPos -= int(notation[i])
                i += 1
                continue
            #Reduziere die Board Position um 1 und erhöhe die nächste Iteration für die Schleife um 2.
            boardPos -= 1
            i += 2
    
    def put_pieces_on_board(self):
        # setze die Steine auf das Board
        # in dem fall 12 weiße und 12 schwarze Steine
        # viellecht sollten wir das auch in der __init__ Methode machen
        # hier soll der code mit bitboards sein. 
        # vielleicht kann man move_piece und put_pieces lieber als 
        # als nur eine methode schreiebn und nicht als zwei
        pass

    def move_piece(self, move):
        # nimmt die move variable aus der pick_move Methode aus der Jump_Sturdy_Player_Agent Klasse und macht den Zug der JumpSturdyPlayerAgent Klasse und 
        # aktualisiert das Board
        pass

    def game_end_check(self):
        # checke ob Spiel vorbei ist
        # also ob alle gegnerischen Steine geschlagen wurden, oder ob keine Züge mehr möglich sind, oder ob ein Stein die andere Seite erreicht hat
        # return 1, wenn spiel vorbei ist, sonst return 0
        pass

    def print_board(self):
        #Printe das Board der Übersicht halber
        for i in range(59, -1, -1):
            #Shifte dabei immer die jeweiligen BitBoards um i stellen und schaue ob dieses Zeichen eine 1 ist.
            #Falls ja Printe den Buchstaben des jeweiligen Pieces vom BitBoard
            if (self.pieceBB[0]>>i)&1==1:
                print("r", end='')
            elif (self.pieceBB[1]>>i)&1==1:
                print("b", end='')
            elif (self.pieceBB[2]>>i)&1==1:
                print("R", end='')
            elif (self.pieceBB[3]>>i)&1==1:
                print("B", end='')
            elif (self.pieceBB[4]>>i)&1==1:
                print("c", end='')
            elif (self.pieceBB[5]>>i)&1==1:
                print("C", end='')
            else:
                print("0", end='')
            if i%8==6:
                print()
        
