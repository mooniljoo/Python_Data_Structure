def fibo_dp(num: int) -> int:
    '''
    Returns the Fibonacci number of the nth with memoization
    '''
    cache = [0 for index in range(num + 1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num + 1):
        cache[index] = cache[index - 1] + cache[index - 2]
    return cache[num]
