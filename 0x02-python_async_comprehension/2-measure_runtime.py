#!/usr/bin/env python3
"""A Python module to measure the execution time of asynchronous tasks."""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Execute async_comprehension 4 times in parallel and measure the total runtime.

    Returns:
        float: Total execution time in seconds.
    """
    start_time = time.perf_counter()  # Record start time
    tasks = [async_comprehension() for _ in range(4)]  # Create 4 tasks
    await asyncio.gather(*tasks)  # Run tasks concurrently
    end_time = time.perf_counter()  # Record end time

    return end_time - start_time  # Calculate total runtime
