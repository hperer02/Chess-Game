import pytest
from chess_puzzle import *

#Unit tests for location2index function

def test_location2index1():
    assert location2index("e2") == (5,2)

def test_location2index2():
    assert location2index("e20") == (5,20)

def test_location2index3():
    assert location2index("f1") == (6,1)

def test_location2index4():
    assert location2index("j15") == (10,15)

def test_location2index5():
    assert location2index("z26") == (26,26)

#Unit tests for index2location function

def test_index2location1():
    assert index2location(5,2) == "e2"

def test_index2location2():
    assert index2location(26,2) == "z2"

def test_index2location3():
    assert index2location(7,8) == "g8"

def test_index2location4():
    assert index2location(24,17) == "x17"

def test_index2location5():
    assert index2location(4,3) == "d3"

wb1 = Bishop(2,5,True)
wb2 = Bishop(4,4,True)
wb3 = Bishop(3,1,True)
wb4 = Bishop(5,5,True)
wb5 = Bishop(4,1,True)

wk1 = King(3,5,True)
wk1a = King(2,5,True)


bb1 = Bishop(3,3,False)
bb2 = Bishop(5,3,False)
bb3 = Bishop(1,2,False)

bk1 = King(2,3,False)

B1 = (5, [wb1, bb1, wb2, bb2, wb3, wk1, bk1])

#Unit tests for is_piece_at function

def test_is_piece_at1():
    assert is_piece_at(2,2, B1) == False

def test_is_piece_at2():
    assert is_piece_at(27,27, B1) == False

def test_is_piece_at3():
    assert is_piece_at(3,1, B1) == True

def test_is_piece_at4():
    assert is_piece_at(5,3, B1) == True

def test_is_piece_at5():
    assert is_piece_at(3,3, B1) == True

#Unit tests for piece_at function

def test_piece_at1():
    assert piece_at(3,3, B1) == bb1

def test_piece_at2():
    assert piece_at(3,1, B1) == wb3

def test_piece_at3():
    assert piece_at(2,3, B1) == bk1

def test_piece_at4():
    assert piece_at(2,5, B1) == wb1

def test_piece_at5():
    assert piece_at(3,5, B1) == wk1

def test_piece_at6():
    assert piece_at(4,4, B1) == wb2

def test_piece_at7():
    assert piece_at(5,3, B1) == bb2

#Unit tests for can_reach function

def test_can_reach1():
    assert wb2.can_reach(5,5, B1) == True

def test_can_reach2():
    assert bb1.can_reach(6,6, B1) == False

def test_can_reach3():
    assert wb3.can_reach(2,2, B1) == True

def test_can_reach4():
    assert wb3.can_reach(6,3, B1) == False

def test_can_reach5():
    assert wb1.can_reach(3,3, B1) == False

def test_can_reach6():
    assert wb2.can_reach(3,3, B1) == True

def test_can_reach7():
    assert wk1.can_reach(2,5, B1) == False

def test_can_reach8():
    assert wk1.can_reach(1,5, B1) == False

def test_can_reach9():
    assert wk1.can_reach(2,4, B1) == True

def test_can_reach10():
    assert wk1.can_reach(3,4, B1) == True
    
#Unit tests for can_move_to function

def test_can_move_to1():
    assert wb2.can_move_to(5,5, B1) == False

def test_can_move_to2():
    assert wb2.can_move_to(5,3, B1) == True

def test_can_move_to3():
    assert wb2.can_move_to(6,2, B1) == False

def test_can_move_to4():
    assert wb2.can_move_to(2,2, B1) == False

def test_can_move_to5():
    assert wb3.can_move_to(5,3, B1) == True

def test_can_move_to6():
    assert wb3.can_move_to(1,4, B1) == False

def test_can_move_to7():
    assert bb1.can_move_to(4,4, B1) == True

def test_can_move_to8():
    assert bb1.can_move_to(5,5, B1) == False

def test_can_move_to9():
    assert wk1.can_move_to(2,4, B1) == False

def test_can_move_to10():
    assert wk1.can_move_to(3,4, B1) == False

def test_can_move_to11():
    assert wk1.can_move_to(4,5, B1) == True

def test_can_move_to12():
    assert bk1.can_move_to(1,3, B1) == False

def test_can_move_to13():
    assert bk1.can_move_to(1,4, B1) == False

def test_can_move_to14():
    assert bk1.can_move_to(2,4, B1) == False

def test_can_move_to15():
    assert bk1.can_move_to(3,2, B1) == True

#Unit tests for move_to function

def test_move_to1():
    wb3a = Bishop(5,3,True)
    Actual_B = wb3.move_to(5,3, B1)
    Expected_B = (5, [wb3a, wb1, wk1, wb2, bk1, bb1]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

def test_move_to2(): #this move is not possible so the expected board shouldn't change
    wb2a = Bishop(5,5,True)
    Actual_B = wb2.move_to(5,5, B1)
    Expected_B = (5, [wb1, bb1, wb2, bb2, wb3, wk1, bk1]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

def test_move_to3():
    wb2b = Bishop(5,3,True)
    Actual_B = wb2.move_to(5,3, B1)
    Expected_B = (5, [wb3, wb1, wk1, wb2b, bk1, bb1]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

def test_move_to4(): #this move is not possible so the expected board shouldn't change
    wk2a = King(3,4,True)
    Actual_B = wk1.move_to(3,4, B1)
    Expected_B = (5, [wb3, wb1, wk1, wb2, bk1, bb1, bb2]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

def test_move_to5(): #this move is not possible so the expected board shouldn't change
    bk1a = King(1,3,False)
    Actual_B = bk1.move_to(1,3, B1)
    Expected_B = (5, [wb3, wb1, wk1, wb2, bk1, bb1, bb2]) 

    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

#Unit tests for is_check function

def test_is_check1():
    B2 = (5, [wb1, wk1, bk1, bb1, bb2, wb3])
    assert is_check(True, B2) == True

def test_is_check2():
    bk1_2 = King(1,3,False)
    B2_2 = (5, [wb1, wk1, bk1_2, wb2, bb1, bb2, wb3])
    assert is_check(False, B2_2) == True

def test_is_check3():
    bk1_3 = King(3,2,False)
    B2_3 = (5, [wb1, wk1, bk1_3, wb2, bb1, bb2, wb3])
    assert is_check(False, B2_3) == False

def test_is_check4():
    wb1_4 = Bishop(1,4,True)
    B2_4 = (5, [wb1_4, wk1, bk1, wb2, bb1, bb2, wb3])
    assert is_check(False, B2_4) == True

def test_is_check5():
    bk1_5 = King(1,2,False)
    B2_5 = (5, [wb1, wk1, bk1_5, wb2, bb1, bb2, wb3])
    assert is_check(False, B2_5) == False

#Unit tests for is_checkmate function

def test_is_checkmate1():
    B3 = (5, [wk1a, wb4, bk1, bb2, bb3, wb3, wb5])
    assert is_checkmate(False, B3) == True

def test_is_checkmate2():
    wb4a = Bishop(3,3,True)
    B3 = (5, [wk1a, wb4a, bk1, bb2, bb3, wb3, wb5])
    assert is_checkmate(False, B3) == False

def test_is_checkmate3():
    bb2a = Bishop(6,3,False)
    B3 = (5, [wk1a, wb4, bk1, bb2a, bb3, wb3, wb5])
    assert is_checkmate(False, B3) == False

def test_is_checkmate4():
    bb3a = Bishop(5,4,False)
    B3 = (5, [wk1a, wb4, bk1, bb2, bb3a, wb3, wb5])
    assert is_checkmate(False, B3) == False
    
def test_is_checkmate5():
    bb3b = Bishop(4,2,False)
    B3 = (5, [wk1a, wb4, bk1, bb2, bb3b, wb3, wb5])
    assert is_checkmate(False, B3) == False

def test_is_checkmate6():
    bk1a = King(3,2,False)
    B3 = (5, [wk1a, wb4, bk1a, bb2, bb3, wb3, wb5])
    assert is_checkmate(False, B3) == False

def test_is_checkmate7():
    bb2b = Bishop(6,2,False)
    B3 = (5, [wk1a, wb4, bk1, bb2b, bb3, wb3, wb5])
    assert is_checkmate(False, B3) == True

#Unit tests for is_stalemate function

def test_is_stalemate1():
    bk1_s = King(1,2,False)
    wb_s = Bishop(5,4,True)
    B4 = (5, [wk1a, wb4, bk1_s, wb3, wb_s, wb5])
    assert is_stalemate(False, B4) == True

def test_is_stalemate2():
    bk1_s = King(1,2,False)
    wb_s = Bishop(5,4,True)
    B4 = (5, [wk1a, wb4, bk1_s, wb3, wb_s])
    assert is_stalemate(False, B4) == False

def test_is_stalemate3():
    bk1_s = King(4,5,False)
    wb_s = Bishop(1,6,True)
    bb_s = Bishop(4,2,False)
    bb_ss = Bishop(3,2,False)
    B4 = (6, [wk1a, bb_s, bb_ss, bk1_s,wb_s, bb3, bb2])
    assert is_stalemate(True, B4) == True

def test_is_stalemate4():
    bk1_s = King(4,5,False)
    bb_s = Bishop(4,2,False)
    bb_ss = Bishop(3,2,False)
    B4 = (6, [wk1a, bb_s, bb_ss, bk1_s, bb3, bb2])
    assert is_stalemate(True, B4) == False

def test_is_stalemate5():
    bk1_s = King(4,5,False)
    wb_s = Bishop(1,6,True)
    bb_s = Bishop(4,2,False)
    B4 = (6, [wk1a, bb_s, bk1_s,wb_s, bb3, bb2])
    assert is_stalemate(True, B4) == False

#Unit tests for read_board function

def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece._pos_X == piece1._pos_X and piece._pos_Y == piece1._pos_Y and piece._side_ == piece1._side_ and type(piece) == type(piece1):
                found = True
        assert found

def test_read_board2(): #having a piece Bf3 which is outside of board limits 
    with pytest.raises(IOError) as exception:
        assert read_board("board_examp1.txt") == exception

def test_read_board3(): #testing with 2 kings for white
    with pytest.raises(IOError) as exception:
        assert read_board("board_examp2.txt") == exception

def test_read_board4(): #testing with 2 white Bishops in the same position
    with pytest.raises(IOError) as exception:
        assert read_board("board_examp3.txt") == exception

def test_read_board5(): #testing with a board_size greater than 26
    with pytest.raises(IOError) as exception:
        assert read_board("board_examp4.txt") == exception

#Unit tests for conf2unicode function

unicode_char = {'white_king':'\u2654','white_bishop':'\u2657','black_king':'\u265A','black_bishop':'\u265D','space':'\u2001'}

B5 = (8, [wb1, bb3, wb2, bb2, wb5, wk1, bk1])
B6 = (6, [wb3, bb1, wb2, bb2, wb4, wk1a, bk1])
B7 = (10,[wb4, bb1, wb2, bb3, wb5, wk1, bk1])
B8 = (7, [wb1, bb3, wb2, bb2, wb3, wk1a, bk1])

def result_conf2unicode(board_lines,row,col, B):
    '''this test function is used to check whether the correct 
    unicode value is in the string for the given board location'''
    found = False
    if is_piece_at(col,row,B) == True:
        piece = piece_at(col,row,B)
        if piece._side_ == True and type(piece) == King:
            if board_lines[piece._pos_Y-1][piece._pos_X-1] == unicode_char['white_king']:
                found = True

        elif piece._side_ == True and type(piece) == Bishop:
            if board_lines[piece._pos_Y-1][piece._pos_X-1] == unicode_char['white_bishop']:
                found = True

        elif piece._side_ == False and type(piece) == King:
            if board_lines[piece._pos_Y-1][piece._pos_X-1] == unicode_char['black_king']:
                found = True

        else:
            if board_lines[piece._pos_Y-1][piece._pos_X-1] == unicode_char['black_bishop']:
                found = True

    else:
        if board_lines[row-1][col-1] == unicode_char['space']:
                found = True
        
    return found

def test_conf2unicode1():

    Output_board = conf2unicode(B1)
    Output_board_lines = Output_board.split('\n')
    Output_board_lines.reverse()
    assert (B1[0] == len(Output_board_lines) and B1[0] == len(Output_board_lines[0])) == True

    for row in range (B1[0],0,-1):
        for col in range (1,B1[0]+1):
            assert result_conf2unicode(Output_board_lines,row,col,B1) == True

def test_conf2unicode2():

    Output_board = conf2unicode(B5)
    Output_board_lines = Output_board.split('\n')
    Output_board_lines.reverse()
    assert (B5[0] == len(Output_board_lines) and B5[0] == len(Output_board_lines[0])) == True

    for row in range (B5[0],0,-1):
        for col in range (1,B5[0]+1):
            assert result_conf2unicode(Output_board_lines,row,col,B5) == True

def test_conf2unicode3():

    Output_board = conf2unicode(B6)
    Output_board_lines = Output_board.split('\n')
    Output_board_lines.reverse()
    assert (B6[0] == len(Output_board_lines) and B6[0] == len(Output_board_lines[0])) == True

    for row in range (B6[0],0,-1):
        for col in range (1,B6[0]+1):
            assert result_conf2unicode(Output_board_lines,row,col,B6) == True

def test_conf2unicode4():

    Output_board = conf2unicode(B7)
    Output_board_lines = Output_board.split('\n')
    Output_board_lines.reverse()
    assert (B7[0] == len(Output_board_lines) and B7[0] == len(Output_board_lines[0])) == True

    for row in range (B7[0],0,-1):
        for col in range (1,B7[0]+1):
            assert result_conf2unicode(Output_board_lines,row,col,B7) == True

def test_conf2unicode5():

    Output_board = conf2unicode(B8)
    Output_board_lines = Output_board.split('\n')
    Output_board_lines.reverse()
    assert (B8[0] == len(Output_board_lines) and B8[0] == len(Output_board_lines[0])) == True

    for row in range (B8[0],0,-1):
        for col in range (1,B8[0]+1):
            assert result_conf2unicode(Output_board_lines,row,col,B8) == True