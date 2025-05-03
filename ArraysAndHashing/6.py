from collections import deque
def encode(strs: list[str]) -> str:
    output_string = ""
    for i in strs:
        output_string += str(len(i))
        output_string += " "
        output_string += i
    return output_string

def decode(s: str) -> list[str]:
    chars = deque([x for x in s])
    result = []
    nums = [ str(x) for x in range(0, 10) ]
    while len(chars):
        new_num = ""
        x = chars.popleft()
        while x in nums:
            new_num += x
            x = chars.popleft()
        
        number_of_element = int(new_num)
        new_string = ""
        for _ in range(0, number_of_element):
            new_string += chars.popleft()

        result.append(new_string)

    return result


test_cases = [
    {
        "input": [
            ["neet","code","love","you!", "!"]
        ],
        "output": ["neet","code","love","you!", "!"]
    },
]

for case in test_cases:
    x = encode(*case['input'])
    if decode(x) == case['output']:
        print("TEST PASS")
    else:
        print("YOUR OUTPUT: ", decode(x), "\nACTUAL OUTPUT", case["output"], "\n________________________\n")
