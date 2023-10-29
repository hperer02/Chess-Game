from copy import copy
import random

def location2index(loc: str) -> tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''
                 
    return (ord(loc[0])-96,int(loc[1:]))

def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
        
    return chr(x+96)+str(y)

class Piece:
    pos_x : int	
    pos_y : int
    side : bool #True for White and False for Black

    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values'''
        self._pos_X = pos_X
        self._pos_Y = pos_Y
        self._side_ = side_

Board = tuple[int, list[Piece]]

def is_piece_at(pos_X : int, pos_Y : int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B''' 
    for i in range (0,len(B[1])):                                #traversing through a for loop to compare _pos_X to pos_X and _pos_Y to pos_Y of each instance of the pieces in the Board
        if B[1][i]._pos_X == pos_X and B[1][i]._pos_Y == pos_Y: #checking whether _pos_X of an instance is equal to pos_X and _pos_Y of the same instance is equal to pos_Y
            return True
        
    return False
	
def piece_at(pos_X : int, pos_Y : int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B 
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    for i in range (0,len(B[1])):                                #traversing through a for loop to compare _pos_X to pos_X and _pos_Y to pos_Y of each instance of the pieces in the Board
        if B[1][i]._pos_X == pos_X and B[1][i]._pos_Y == pos_Y: #checking whether _pos_X of an instance is equal to pos_X and _pos_Y of the same instance is equal to pos_Y
            return B[1][i] 
        
def next_pos(pos_X, new_x, pos_Y, new_y):  
    '''generates the next movement for bishop each time this function is called'''
    if new_x > pos_X and new_y > pos_Y:
        new_x -= 1
        new_y -= 1
    if new_x < pos_X and new_y < pos_Y:
        new_x += 1
        new_y += 1
    if new_x < pos_X and new_y > pos_Y: 
        new_x += 1
        new_y -= 1  
    if new_x > pos_X and new_y < pos_Y:
        new_x -= 1
        new_y += 1
    return new_x, new_y


class Bishop(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_) #calling the constructor of the parent class
        
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this bishop can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule1] and [Rule3] (see section Intro)
        Hint: use is_piece_at
        '''
        new_posx = self._pos_X
        new_posy = self._pos_Y
        piece_check = bool
        piece = Piece

        if abs(self._pos_X - pos_X) == abs(self._pos_Y - pos_Y):      #checking whether the given given position is in the diagonal of the bishop instance

            for i in range (1, abs(self._pos_X - pos_X)):              #traversing through a for loop to generate all board positions from the given piece to the given location
                new_posx, new_posy = next_pos(pos_X, new_posx, pos_Y, new_posy)
                
                piece_check = is_piece_at(new_posx,new_posy,B)          #for each iteration of the for loop, checking whether there is another piece in the path to the location
                
                if piece_check == True:                                  #if there is a piece in between, returning false since bishop can't jump over pieces to get to the desired location
                    return False
                
            piece_check = is_piece_at(pos_X,pos_Y,B)            #checking if there is a piece at the given location
            piece = piece_at(pos_X,pos_Y,B)                     #using piece_at function to find the piece at given location
            
            if piece_check == True and piece._side_ == self._side_: #if the piece at given location is in the same side as the given bishop returning false since it cannot move there
                return False
            else:
                return True                             #if the piece at the given location belongs to the opposite side, returning true because this piece can be captured by the given bishop 
        
        else: 
            return False                      #if the given location can't be reached by the given bishop, returning false because this move is not possible

      
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this bishop can move to coordinates pos_X, pos_Y
        on board B according to all chess rules
        Hints:
        - firstly, check [Rule1] and [Rule3] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule4], use is_check on new board
        '''
        captured_piece = Piece                                 #creating a variable of the type piece to store the captured piece
        current_piece = Piece                                  #creating a variable of the type piece to store the current piece
        New_Board = tuple[int, list[Piece]]                    #creating a new variable to store the new board configuration
        B_list_copy = copy(B[1])                               #creating a copy of the piece list of the input board 
        current_piece = piece_at(self._pos_X, self._pos_Y, B)  #storing the piece in a variable

        if self.can_reach(pos_X, pos_Y, B) == True and is_piece_at(pos_X, pos_Y, B)==True:    #checking whether the piece at the given location can be captured by the current piece

            captured_piece = piece_at(pos_X, pos_Y, B)    #finding the captured piece
            B_list_copy.remove(captured_piece)            
            B_list_copy.remove(current_piece)
            New_Bishop_pos = Bishop(pos_X, pos_Y, self._side_)   #creating a new instance of the resulting move after deleting the previous instances
            B_list_copy.append(New_Bishop_pos)                   #adding the new instance to the board
            New_Board = (B[0], B_list_copy)                      #constructing the new board of the resulting move
            if is_check(self._side_, New_Board) == True:         #checking whether the move has resulted in a check condition for the same side
                return False
            else:
                return True

        if self.can_reach(pos_X, pos_Y, B)==True and is_piece_at(pos_X, pos_Y, B)==False:
            
            B_list_copy.remove(current_piece)
            New_Bishop_pos = Bishop(pos_X, pos_Y, self._side_)
            B_list_copy.append(New_Bishop_pos)
            New_Board = (B[0], B_list_copy)
            if is_check(self._side_, New_Board) == True:
                return False
            else:
                return True

        return False

    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        New_pieces = copy(B[1])   #making a copy of the current pieces in the board
        New_piece_pos = Piece     #creating a Piece variable to store the new instance

        if self.can_move_to(pos_X, pos_Y, B) == True:

            New_pieces.remove(piece_at(self._pos_X, self._pos_Y,B))  
            New_piece_pos = Bishop(pos_X, pos_Y, self._side_)

            if is_piece_at(pos_X, pos_Y, B) == True:

                New_pieces.remove(piece_at(pos_X, pos_Y,B))  
                New_pieces.append(New_piece_pos)
                return (B[0], New_pieces)

            else:

                New_pieces.append(New_piece_pos)
                return (B[0], New_pieces)    
                
        else:
            return B


class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_) #calling the constructor of the parent class

    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule2] and [Rule3]'''
        
        piece_check = bool
        piece = Piece

        if (abs(self._pos_X - pos_X) == 1 or abs(self._pos_X - pos_X) == 0) and (abs(self._pos_Y - pos_Y) == 1 or abs(self._pos_Y - pos_Y) == 0):

            piece_check = is_piece_at(pos_X, pos_Y,B)
            piece = piece_at(pos_X,pos_Y,B)
            
            if piece_check == True and piece._side_ == self._side_:
                return False

            elif piece_check == True and piece._side_ != self._side_:
                return True

            else:
                return True
        
        else: 
            return False    

    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        
        captured_piece = Piece
        current_piece = Piece
        New_Board = tuple[int, list[Piece]]
        B_list_copy = copy(B[1])
        current_piece = piece_at(self._pos_X, self._pos_Y, B)

        if self.can_reach(pos_X, pos_Y, B) == True and is_piece_at(pos_X, pos_Y, B) == True:

            captured_piece = piece_at(pos_X, pos_Y, B)    
            B_list_copy.remove(captured_piece)
            B_list_copy.remove(current_piece)
            New_King_pos = King(pos_X, pos_Y, self._side_)
            B_list_copy.append(New_King_pos)
            New_Board = (B[0], B_list_copy)
            if is_check(self._side_, New_Board) == True:
                return False
            else:
                return True

        if self.can_reach(pos_X, pos_Y, B)==True and is_piece_at(pos_X, pos_Y, B)==False:
            
            B_list_copy.remove(current_piece)
            New_King_pos = King(pos_X, pos_Y, self._side_)
            B_list_copy.append(New_King_pos)
            New_Board = (B[0], B_list_copy)
            if is_check(self._side_, New_Board) == True:
                return False
            else:
                return True

        return False

    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        New_pieces = copy(B[1])
        New_piece_pos = Piece

        if self.can_move_to(pos_X, pos_Y, B) == True:

            New_pieces.remove(piece_at(self._pos_X, self._pos_Y,B))
            New_piece_pos = King(pos_X, pos_Y, self._side_)

            if is_piece_at(pos_X, pos_Y, B) == True:

                New_pieces.remove(piece_at(pos_X, pos_Y,B))  
                New_pieces.append(New_piece_pos)
                return (B[0], New_pieces)

            else:

                New_pieces.append(New_piece_pos)
                return (B[0], New_pieces)    
                
        else:
            return B

def board_dim_check( x_pos: int, y_pos: int, B: Board):
    '''
    checks if the given position is within the board. If it exceeds the board dimensions the highest value will be assigned 
    and if it is lower than the least possible value (1) of the board, 1 will be assigned
    '''
    if x_pos>B[0]:
        x_pos = B[0]
    if x_pos<1:
        x_pos = 1
    if y_pos>B[0]:
        y_pos = B[0]
    if y_pos<1:
        y_pos = 1

    return x_pos, y_pos

def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''
    king_side = King
    for i in range(0, len(B[1])):
        if type(B[1][i])==King and B[1][i]._side_ == side:
            King_side = B[1][i]

    for i in range(0, len(B[1])):
        if B[1][i]._side_ != side and B[1][i].can_reach(King_side._pos_X, King_side._pos_Y, B) == True:
            return True
         
    return False


def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_move_to
    '''
    Check_king = Piece
    Check_piece = Piece
    King_moves = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]

    if is_check(side, B) == True:
        for piece in B[1]:
            if type(piece) == King and piece._side_ == side:
                Check_king = piece

        for piece1 in B[1]:
            if piece1._side_ != side and piece1.can_move_to(Check_king._pos_X, Check_king._pos_Y, B) == True:
                Check_piece = piece1

        for i in range (0,len(King_moves)):
            king_x = Check_king._pos_X + King_moves[i][0]
            king_y = Check_king._pos_Y + King_moves[i][1]
            king_new_x,king_new_y = board_dim_check(king_x,king_y, B)

            if Check_king.can_move_to(king_new_x,king_new_y, B) == True:
                return False

        king_x = Check_king._pos_X
        king_y = Check_king._pos_Y

        for k in range (1, abs(Check_king._pos_X - Check_piece._pos_X)+1):

            king_x, king_y = next_pos(Check_piece._pos_X, king_x, Check_piece._pos_Y, king_y)
        
            for piece2 in B[1]:

                king_new_x1,king_new_y1 = board_dim_check(king_x,king_y, B)
                if type(piece2) == Bishop and piece2._side_ == side and piece2.can_move_to(king_new_x1, king_new_y1, B) == True:
                    return False

        return True
    
    else:
        return False
        

def is_stalemate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is stalemate for side

    Hints: 
    - use is_check
    - use can_move_to 
    '''
    King_moves = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
    Bishop_moves = [(1,1),(1,-1),(-1,-1),(-1,1)]

    if is_check(side, B) == False:
        for piece in B[1]:
            if side == piece._side_ :
                if type(piece) == King:
                    for i in range (0,len(King_moves)):
                        x_k = piece._pos_X + King_moves[i][0]
                        y_k = piece._pos_Y + King_moves[i][1]

                        x_k1,y_k1 = board_dim_check(x_k,y_k, B) #checking if king move is within the board configuration

                        if piece.can_move_to(x_k1, y_k1, B) == True:
                            return False

                if type(piece) == Bishop:
                    for j in range (0,len(Bishop_moves)):
                        x_b = piece._pos_X + Bishop_moves[j][0]
                        y_b = piece._pos_Y + Bishop_moves[j][1]

                        x_b1,y_b1 = board_dim_check(x_b,y_b, B)

                        if piece.can_move_to(x_b1, y_b1, B) == True:
                            return False
    
                return True
    
    else:
        return False

def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    Read_b = open(filename, "r")
    Board_size = Read_b.readline().strip()
    White_pieces = Read_b.readline().strip().replace(" ", "").split(',')
    Black_pieces = Read_b.readline().strip().replace(" ", "").split(',')
    Board_pieces = White_pieces+Black_pieces

    w_king_count = 0
    b_king_count = 0
    for white in White_pieces:
        if white[0] == 'K':
            w_king_count+=1
    
    for black in Black_pieces:
        if black[0] == 'K':
            b_king_count+=1

    if w_king_count!=1 or b_king_count!=1: raise IOError #checking if there is only one king per side
    
    if not Board_size.isdigit() or int(Board_size)<3 or int(Board_size)>26: raise IOError

    piece1 = Piece
    New_piece_set =[]

    for piece in Board_pieces:

        if piece[0]!='B' and piece[0]!='K': raise IOError

        if not piece[2:].isdigit() or int(piece[2:])>int(Board_size) or int(piece[2:])<1: raise IOError

        if not piece[1].isalpha() or ord(piece[1])-96>int(Board_size): raise IOError

        if len(Board_pieces)!=len(set(Board_pieces)): raise IOError

        if piece[0] == 'B' and piece in White_pieces:
            piece1 = Bishop(ord(piece[1])-96,int(piece[2:]),True)

        if piece[0] == 'B' and piece in Black_pieces:
            piece1 = Bishop(ord(piece[1])-96,int(piece[2:]),False)
    
        if piece[0] == 'K' and piece in White_pieces:
            piece1 = King(ord(piece[1])-96,int(piece[2:]),True)

        if piece[0] == 'K' and piece in Black_pieces:
            piece1 = King(ord(piece[1])-96,int(piece[2:]),False)

        New_piece_set.append(piece1)
    
    Read_b.close()
    return (int(Board_size),New_piece_set)

def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''
    save_file = open(filename,'w')
    line1 = str(B[0])
    line2 = ''
    line3 = ''

    for pieces in B[1]:         
        x = pieces._pos_X  
        x_str=chr(x+96)

        if type(pieces)== Bishop and pieces._side_ == True:
            line2+='B'+x_str+str(pieces._pos_Y)+','
        
        if type(pieces)== King and pieces._side_ == True:
            line2+='K'+x_str+str(pieces._pos_Y)+','

        if type(pieces)== Bishop and pieces._side_ == False:
            line3+='B'+x_str+str(pieces._pos_Y)+','
        
        if type(pieces)== King and pieces._side_ == False:
            line3+='K'+x_str+str(pieces._pos_Y)+','
        
    save_file.write(line1+'\n')  
    save_file.write(line2.rstrip(',')+'\n')            
    save_file.write(line3.rstrip(','))  
    save_file.close()          
          

def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''

    x_pos = 0 
    y_pos = 0
    P = Piece
    while True:
        P = random.choice(B[1])                      #using the choice method of random library to choose a piece from the randomly
        if P._side_ == False:
            x_pos = random.randint(1,B[0])           #using randint method of random library to generate a random integer for the given range
            y_pos = random.randint(1,B[0])           #using randint method of random library to generate a random integer for the given range
            if P.can_move_to(x_pos,y_pos,B) == True: #checking whether the chosen piece can move to the given location and if the move is possible, breaking out of the loop
                break

    return (P, x_pos, y_pos)

def conf2unicode(B: Board) -> str: 
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''
    output_string = ''
    unicode_char = {'white_king':'\u2654','white_bishop':'\u2657','black_king':'\u265A','black_bishop':'\u265D','space':'\u2001'}

    for i in range (B[0],0,-1):
        for j in range (1,B[0]+1):    #using a nested for loop to generate a string which contains the unicodes of pieces from top to bottom of the board

            if is_piece_at(j,i,B) == True:
                if piece_at(j,i,B)._side_ == True and type(piece_at(j,i,B)) == King:
                    output_string+=unicode_char['white_king']
                    
                if piece_at(j,i,B)._side_ == True and type(piece_at(j,i,B)) == Bishop:
                    output_string+=unicode_char['white_bishop']
                    
                if piece_at(j,i,B)._side_ == False and type(piece_at(j,i,B)) == King:
                    output_string+=unicode_char['black_king']
                    
                if piece_at(j,i,B)._side_ == False and type(piece_at(j,i,B)) == Bishop:
                    output_string+=unicode_char['black_bishop']
                    
            else:
                output_string+=unicode_char['space']   #if there isn't piece at the given location, a space will be added to the string

        output_string+='\n'    #moving to the next line of the board
    
    return output_string.rstrip('\n')

def main() -> None:
    '''
    runs the play
    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''
    filename = ''
    initial_board = ''

    while True:
        try:
            filename = input("File name for initial configuration: ")
            if filename == 'QUIT':
                exit()
            initial_board = read_board(filename)    
            
        except IOError:
            print("This is not a valid file. File name for initial configuration: ")

        else: 
            print('The initial configuration is:')
            print(conf2unicode(initial_board))
            break

    current_piece = ''
    current_board = initial_board
    new_board = ''
    board_loc2 = ''

    while True:
        try:
            user_input = input('Next move of White:')
            assert (len(user_input)>=4 and len(user_input)<=6) == True
            if user_input =='QUIT':
                save_file = input('File name to store the configuration: ')
                save_board(save_file, current_board)
                print('The game configuration saved.')
                exit()

            elif user_input[2].isalpha() == True:
                assert (user_input[0].isalpha() and user_input[1].isdigit() and user_input[2].isalpha() and user_input[3:].isdigit()) == True
                board_loc1 = location2index(user_input[0:2])
                assert is_piece_at(board_loc1[0],board_loc1[1],current_board) == True
                current_piece = piece_at(board_loc1[0],board_loc1[1],current_board)
                board_loc2 = location2index(user_input[2:])

            else:
                assert (user_input[0].isalpha() and user_input[1:3].isdigit() and user_input[3].isalpha() and user_input[4:].isdigit()) == True
                board_loc1 = location2index(user_input[0:3])
                assert is_piece_at(board_loc1[0],board_loc1[1],current_board) == True
                current_piece = piece_at(board_loc1[0],board_loc1[1:3],current_board)
                board_loc2 = location2index(user_input[4:])

            assert current_piece._side_ == True    
            assert current_piece.can_move_to(board_loc2[0],board_loc2[1],current_board) == True
            assert (board_loc2[0]<=current_board[0] and board_loc2[1]<=current_board[0] and board_loc2[0]>=1 and board_loc2[1]>=1) == True
            new_board = current_piece.move_to(board_loc2[0],board_loc2[1],current_board)
            current_board = new_board
            print("The configuration after White's move is:")
            print(conf2unicode(current_board))

            if is_checkmate(not current_piece._side_, current_board) == True:
                print('Game over. White wins.')
                exit()

            if is_stalemate(not current_piece._side_, current_board) == True:
                print('Game over. Stalemate.')
                exit()

            black_move = find_black_move(current_board)
            new_board_after_bmove = black_move[0].move_to(black_move[1], black_move[2], current_board)
            current_board = new_board_after_bmove
            print(f"Next move of Black is {chr(black_move[0]._pos_X+96)}{black_move[0]._pos_Y}{chr(black_move[1]+96)}{black_move[2]}. The configuration after Black's move is:")
            print(conf2unicode(current_board))
            
            if is_checkmate(not black_move[0]._side_, current_board) == True:
                print('Game over. Black wins.')
                exit()

            if is_stalemate(not black_move[0]._side_, current_board) == True:
                print('Game over. Stalemate.')
                exit()

        except AssertionError:
            print('This is not a valid move. ', end = '')

if __name__ == '__main__': #keep this in
   main()