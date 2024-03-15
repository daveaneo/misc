import math

def maxMinSteps(n, mode):
    # Define step sizes based on the mode
    if mode == 'log10':
        step_sizes = [10**i for i in range(int(math.log10(n)) + 1)]
    elif mode == 'log2':
        step_sizes = [2**i for i in range(int(math.log2(n)) + 1)]
    elif mode == 'fibonacci':
        step_sizes = [1, 1]
        while step_sizes[-1] + step_sizes[-2] <= n:
            step_sizes.append(step_sizes[-1] + step_sizes[-2])
    else:
        raise ValueError("Invalid mode. Choose from 'log10', 'log2', or 'fibonacci'.")

    # Initialize an array to store the minimum steps needed to reach each stair
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 steps needed to reach the 0th stair

    # Calculate the minimum steps needed to reach each stair
    for i in range(1, n + 1):
        for step in step_sizes:
            if i - step >= 0:
                dp[i] = min(dp[i], dp[i - step] + 1)

    max_steps = max(dp[1:])  # Exclude the 0th stair
    avg_steps = sum(dp[1:]) / n  # Exclude the 0th stair
    return {"max": max_steps, "average": avg_steps}

# Test cases
# print(maxMinSteps(8, 'log10'))  # log10 -> answer should be 8 (step 8)
# print(maxMinSteps(9, 'log10'))  # log10 -> answer should be 9 (step 9)
# print(maxMinSteps(10, 'log10'))  # log10 -> answer should be 9 (step 9)
# print(maxMinSteps(100, 'log10'))  # log10  -> answer should be 18 (step 99)
# print(maxMinSteps(8, 'log2'))  # log2 -> answer should be 4 (step 8)
# print(maxMinSteps(9, 'log2'))  # log2 -> answer should be 5 (step 9)

modes = ["fibonacci", "log10", "log2"]

TOTAL_STAIRS = 4444
print(f'staircase size: {TOTAL_STAIRS}')
for mode in modes:
    res = maxMinSteps(TOTAL_STAIRS, mode)  # log2 -> answer should be 5 (step 9)
    print(f'{mode}: {res["max"]} max, {res["average"]} average')
