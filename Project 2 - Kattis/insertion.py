import sys, unittest

### https://open.kattis.com/problems/insert

def nCk(n: int, k: int):
    if k > n / 2: k = n - k
    if k == 0: return 1
    elif k == 1: return n
    else:
        tmp: int = 1
        for i in range((n - k) + 1, n + 1): tmp *= i
        for i in range(2, k + 1): tmp /= i
        return int(tmp)

def algorithm(numList: list):
    if len(numList) <= 1: return 1
    root: int = numList[0]
    tmpL: list = []
    tmpR: list = []
    numList = numList[1::]
    for elem in numList:
        if elem < root: tmpL.append(elem)
        else: tmpR.append(elem)
    return nCk(len(numList), len(tmpR)) * algorithm(tmpL) * algorithm(tmpR)

def test():
    #unittest.TestCase("runTest").assertEqual(algorithm(2387542893749238174, 29017439048723), 2387571911188286897)
    #unittest.TestCase("runTest").assertEqual(algorithm(3048203948, 2340239485034957098), 2340239488083161046)
    #unittest.TestCase("runTest").assertEqual(algorithm(78908469548903485253982759825, 902858248793895727502394801293), 981766718342799212756377561118)
    print("All test cases passed.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        lines: list = []
        for line in sys.stdin: lines.append(line)
        lines = lines[1::2]
        for line in lines:
            numList: list = line.split(" ")
            for i in range(0, len(numList)):
                numList[i] = int(numList[i])
            res: int = int(algorithm(numList))
            print(res)