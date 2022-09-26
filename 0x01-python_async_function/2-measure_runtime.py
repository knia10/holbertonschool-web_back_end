#!/usr/bin/env python3
'''
Import wait_random from the previous python file that
you’ve written and write an async routine called
wait_n that takes in 2 int arguments (in this order):
n and max_delay. You will spawn wait_random n times with
the specified max_delay.

wait_n should return the list of all the delays
(float values). The list of the delays should be in
ascending order without using sort() because of concurrency.
'''

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    return the list of all the delays (float values).
    '''
    time_0 = time()
    run(wait_n(n, max_delay))
    time_1 = time()
    elapsed_time = time_1 - time_0
    return elapsed_time / n
