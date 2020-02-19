def willYou(young, beautiful, loved):
    return loved and any(not v for v in [young, beautiful]) or not loved and young and beautiful

def willYou(young, beautiful, loved):
    return loved != (young and beautiful)
