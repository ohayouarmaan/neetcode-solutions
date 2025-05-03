def isAnagram(s: str, t: str) -> bool:
    frequencies = {}
    for x in s:
        if x in frequencies:
            frequencies[x] += 1
        else:
            frequencies[x] = 1

    for y in t:
        if y in frequencies:
            frequencies[y] -= 1
            if(frequencies[y] == 0):
                del frequencies[y]
        else:
            return False


    if frequencies == {}:
        return True
    else:
        return False

test_cases = [
    {
        "input": ["racecar", "carrace"],
        "output": True
    },
    {
        "input": ["jar", "jam"],
        "output": False
    },
]

for case in test_cases:
    if isAnagram(*case['input']) == case['output']:
        print("TEST PASS")
    else:
        print("YOUR OUTPUT: ", isAnagram(*case['input']), "\nACTUAL OUTPUT", case["output"], "\n________________________\n")
