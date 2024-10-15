#!/usr/bin/env python3
"""Module containing an asynchronous generator function."""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yield a random float between 0 and 10, 10 times, with a 1-second delay.

    Yields:
        A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
