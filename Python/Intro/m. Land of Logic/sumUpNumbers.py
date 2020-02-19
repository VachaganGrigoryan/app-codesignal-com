def sumUpNumbers(inputString):
    n = re.findall("[0-9]+",inputString)
    return sum(map(lambda x: int(x), n))

def sumUpNumbers(inputString):
    return sum([int(v) for v in re.split('[^0-9]+', inputString) if v.isdigit()])
