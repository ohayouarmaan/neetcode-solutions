def longestConsecutive(nums: list[int]) -> int:
    hash_set = set()
    max_len = -1
    for i in range(len(nums)):
        if (nums[i] - 1) in hash_set:
            curr = nums[i] - 1
            length = 0
            while curr in hash_set:
                curr = curr - 1
                length += 1

            if length > max_len:
                max_len = length
        hash_set.add(nums[i])

    return max_len + 1

test_cases = [
    {
        "input": [
            [2,20,4,10,3,4,5]
        ],
        "output": 4
    },
    {
        "input": [
            [-1,0,1,2,3]
        ],
        "output": 5
    },
    {
        "input": [
            [-1,0]
        ],
        "output": 2
    },
    {
        "input": [
            [0,0]
        ],
        "output": 0
    }
]

for case in test_cases:
    x = longestConsecutive(*case['input'])
    if x == case['output']:
        print("TEST PASS")
        print("________________________\n")
    else:
        print("YOUR OUTPUT: ", x, "\nACTUAL OUTPUT", case["output"], "\n________________________\n")
