import sys, unittest

### https://open.kattis.com/problems/tornbygge

def algorithm(numList: list):
    num: int = 0
    last: int = 0
    for item in numList:
        item = int(item)
        if item > last:
            num += 1
        last = item
    return num

def test():
    unittest.TestCase("runTest").assertEqual(algorithm(["4", "2", "2", "1", "3", "1"]), 2)
    unittest.TestCase("runTest").assertEqual(algorithm(["3", "3", "2", "1", "2", "5", "2"]), 3)
    unittest.TestCase("runTest").assertEqual(algorithm(["5", "1", "4", "3", "1", "2", "2", "5"]), 4)
    print("All test cases passed.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        lines: list = []
        for line in sys.stdin: lines.append(line)
        num: int = algorithm(lines[1].split(" "))
        print(num)
