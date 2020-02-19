import math

def swapAdjacentBits(n):
    return int(''.join([bin(n)[2:][::-1][i:i+2:] if len(bin(n)[2:][::-1][i:i+2:]) == 2 else bin(n)[2:][::-1][i:i+2:]+'0'  for i in range(0,math.ceil(len(bin(n)[2:])),2)][::-1]),2)

print(swapAdjacentBits(int(input("Enter number : "))))