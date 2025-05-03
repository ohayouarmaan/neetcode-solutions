def productExceptSelf(nums: list[int]) -> list[int]:
    simple_multiplication = 1
    simple_multiplication_without_zero = 1
    if max(nums) == min(nums) == 0:
        simple_multiplication_without_zero = 0
        simple_multiplication = 0

    zero_count = 0
    for n in nums:
        if n != 0:
            simple_multiplication *= n
            simple_multiplication_without_zero *= n
        else:
            zero_count += 1
            if zero_count >=2:
                simple_multiplication_without_zero = 0
                simple_multiplication = 0
            simple_multiplication *= n

    result = []
    for x in nums:
        if x == 0:
            result.append(simple_multiplication_without_zero)
        else:
            result.append(simple_multiplication // x)

    return result


test_cases = [
    {
        "input": [
            [1,2,4,6]
        ],
        "output": [48,24,12,8]
    },
    {
        "input": [
            [-1,0,1,2,3]
        ],
        "output": [0,-6,0,0,0]
    },
    {
        "input": [
            [-1,0]
        ],
        "output": [0, -1]
    },
    {
        "input": [
            [0,0]
        ],
        "output": [0, 0]
    },
    {
        "input": [
            [0,8,0]
        ],
        "output": [0, 0, 0]
    },
]

for case in test_cases:
    x = productExceptSelf(*case['input'])
    if x == case['output']:
        print("TEST PASS")
        print("________________________\n")
    else:
        print("YOUR OUTPUT: ", x, "\nACTUAL OUTPUT", case["output"], "\n________________________\n")
