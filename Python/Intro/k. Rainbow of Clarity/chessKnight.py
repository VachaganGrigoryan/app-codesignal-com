def chessKnight(cell):
    count = 0
    if ('a' <= chr(ord(cell[0])+2) <= 'h') and (0 < int(cell[1])+1 < 9):
        count += 1
    if ('a' <= chr(ord(cell[0])-2) <= 'h') and (0 < int(cell[1])+1 < 9):
        count += 1
    if ('a' <= chr(ord(cell[0])+2) <= 'h') and (0 < int(cell[1])-1 < 9):
        count += 1
    if ('a' <= chr(ord(cell[0])-2) <= 'h') and (0 < int(cell[1])-1 < 9):
        count += 1
    if ('a' <= chr(ord(cell[0])+1) <= 'h') and (0 < int(cell[1])+2 < 9):
        count += 1
    if ('a' <= chr(ord(cell[0])+1) <= 'h') and (0 < int(cell[1])-2 < 9):
        count += 1
    if ('a' <= chr(ord(cell[0])-1) <= 'h') and (0 < int(cell[1])+2 < 9):
        count += 1
    if ('a' <= chr(ord(cell[0])-1) <= 'h') and (0 < int(cell[1])-2 < 9):
        count += 1
    return count

