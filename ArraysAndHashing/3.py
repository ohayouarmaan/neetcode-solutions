def twoSum(nums: list[int], target: int) -> list[int]:
    required = {}
    for x in range(len(nums)):
        if nums[x] in required:
            required[nums[x]].append(x)
            return required[nums[x]]
        else:
            required[target - nums[x]] = [x]

    return [-1, -1]
    

test_cases = [
    {
        "input": [[3,4,5,6], 7],
        "output": [0, 1]
    },
    {
        "input": [[4,5,6], 10],
        "output": [0, 2]
    },
]

for case in test_cases:
    if twoSum(*case['input']) == case['output']:
        print("TEST PASS")
    else:
        print("YOUR OUTPUT: ", twoSum(*case['input']), "\nACTUAL OUTPUT", case["output"], "\n________________________\n")
