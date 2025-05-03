def groupAnagrams(strs: list[str]) -> list[list[str]]:
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

    result = []
    while len(strs) > 0:
        first_string = strs[0]
        new_strs = []
        anagrams = [first_string]
        for i in strs[1:]:
            if isAnagram(first_string, i):
                anagrams.append(i)
            else:
                new_strs.append(i)

        strs = new_strs
        result.append(anagrams)


    return result

test_cases = [
    {
        "input": [["act","pots","tops","cat","stop","hat"]],
        "output": [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    },
    {
        "input": [['x']],
        "output": [['x']]
    },
]

for case in test_cases:
    if groupAnagrams(*case['input']) == case['output']:
        print("TEST PASS")
    else:
        print("YOUR OUTPUT: ", groupAnagrams(*case['input']), "\nACTUAL OUTPUT", case["output"], "\n________________________\n")
