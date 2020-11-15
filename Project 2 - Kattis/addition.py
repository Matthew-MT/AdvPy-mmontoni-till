import sys, unittest

### https://open.kattis.com/problems/simpleaddition

def algorithm(a: int, b: int):
    return a + b

def test():
    unittest.TestCase("runTest").assertEqual(algorithm(2387542893749238174, 29017439048723), 2387571911188286897)
    unittest.TestCase("runTest").assertEqual(algorithm(3048203948, 2340239485034957098), 2340239488083161046)
    unittest.TestCase("runTest").assertEqual(algorithm(78908469548903485253982759825, 902858248793895727502394801293), 981766718342799212756377561118)
    print("All test cases passed.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        lines: list = []
        for line in sys.stdin: lines.append(line)
        res: int = algorithm(int(lines[0]), int(lines[1]))
        print(res)