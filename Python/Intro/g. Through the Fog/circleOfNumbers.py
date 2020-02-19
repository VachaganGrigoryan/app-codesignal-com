def circleOfNumbers(n, firstNumber):
    return firstNumber-n/2 if firstNumber >= n/2 else firstNumber+n/2

print(circleOfNumbers(int(input("Enter n : ")),int(input("Enter firstNumber : "))))