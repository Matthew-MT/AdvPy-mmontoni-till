import sys, unittest

### https://open.kattis.com/problems/trainpassengers

def algorithm(capacity: int, stations: list):
    holding: int = 0
    left: int
    joined: int
    waited: int
    for station in stations:
        parsed = station.split(" ")
        left = int(parsed[0])
        joined = int(parsed[1])
        waited = int(parsed[2])

        if left < 0 or joined < 0 or waited < 0: return "impossible"

        holding -= left
        if holding < 0: return "impossible"
        holding += joined
        if holding > capacity or (waited > 0 and holding + waited <= capacity): return "impossible"
    
    if holding != 0 or waited != 0: return "impossible"
    return "possible"

def test():
    #unittest.TestCase("runTest").assertEqual(algorithm(["4", "2", "2", "1", "3", "1"]), 2)
    #unittest.TestCase("runTest").assertEqual(algorithm(["3", "3", "2", "1", "2", "5", "2"]), 3)
    #unittest.TestCase("runTest").assertEqual(algorithm(["5", "1", "4", "3", "1", "2", "2", "5"]), 4)
    print("All test cases passed.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        lines: list = []
        for line in sys.stdin: lines.append(line)
        res: str = algorithm(int(lines[0].split(" ")[0]), lines[1::])
        print(res)