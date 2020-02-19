def chessBoardCellColor(cell1, cell2):
    chek = lambda x: not (ord(x[0]) + int(x[1]))%2
    return chek(cell1) == chek(cell2)

print(chessBoardCellColor("A1","A2"))