def hasDuplicate(nums: list[int]) -> bool:
    visited = set()
    should_return = False

    for i in range(len(nums)):
        if nums[i] in visited:
            should_return = True
            break
        else:
            visited.add(nums[i])

    return should_return


test_cases = [
    {
        "input": [1, 2, 3, 3],
        "output": True
    },
    {
        "input": [1, 2, 3, 4],
        "output": False
    },
]

for case in test_cases:
    if hasDuplicate(case['input']) == case['output']:
        print("TEST PASS")
    else:
        print("YOUR OUTPUT: ", hasDuplicate(case['input']), "\nACTUAL OUTPUT", case["output"], "\n________________________\n")
