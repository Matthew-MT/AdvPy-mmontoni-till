import sys, unittest

### https://open.kattis.com/problems/recount

def algorithm(names: str):
    count: dict = {}
    for name in names:
        if not count.get(name): count.update({name: names.count(name)})
    sortedCount = list(count.items())
    sortedCount.sort(reverse = True, key = (lambda a: a[1]))
    if (sortedCount[0][1] == sortedCount[1][1]): return "Runoff!"
    else: return sortedCount[0][0][:-1:]

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
        lines = lines[:-1:]
        res: str = algorithm(lines)
        print(res)