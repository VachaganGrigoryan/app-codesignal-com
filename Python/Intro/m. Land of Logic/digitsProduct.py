def digitsProduct(product):
    if product < 10:
        return product if product > 0 else 10
    strDig = ""
    for i in range(9,1,-1):
        while not product%i:
            strDig = chr(ord('0')+i) + strDig
            product /= i
    return -1 if product != 1 else int(strDig)
