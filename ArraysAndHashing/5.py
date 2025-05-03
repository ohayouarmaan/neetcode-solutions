def topKFrequent(nums: list[int], k: int) -> list[int]:
    bucket = [[] for _ in range(len(nums))]
    frequency_graph = {}
    for n in nums:
        if n in frequency_graph:
            frequency_graph[n] += 1
        else:
            frequency_graph[n] = 1
    
    for num, count in frequency_graph.items():
        bucket[count - 1].append(num)

    result = []
    for i in range(len(bucket) - 1, -1, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result

    return [-1]


test_cases = [
    {
        "input": [[1,2,2,3,3,3], 2],
        "output": [2,3] 
    },
    {
        "input": [[7,7], 1],
        "output": [7] 
    },
    {
        "input": [[1], 1],
        "output": [1] 
    },
]

for case in test_cases:
    if topKFrequent(*case['input']) == case['output']:
        print("TEST PASS")
    else:
        print("YOUR OUTPUT: ", topKFrequent(*case['input']), "\nACTUAL OUTPUT", case["output"], "\n________________________\n")
