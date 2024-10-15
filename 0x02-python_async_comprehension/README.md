# Python Async Comprehension Project

This project explores asynchronous programming in Python by implementing asynchronous generators and comprehensions. It covers how to write and use asynchronous code to improve efficiency by working with coroutines, and how to measure runtimes for parallel asynchronous tasks.

## Learning Objectives

By the end of this project, you will be able to:

- Write asynchronous generators.
- Use async comprehensions.
- Type-annotate generators and asynchronous functions.

---

## Requirements

- **Allowed editors:** `vi`, `vim`, `emacs`
- **Python version:** Python 3.7 on Ubuntu 18.04 LTS
- **Code style:** Must follow `pycodestyle` (version 2.5.x)
- **Documentation:** 
  - Each module, class, and function must have proper docstrings.
  - The first line of each file should be: `#!/usr/bin/env python3`
  - Every file must end with a new line.
- **Type annotations:** All functions and coroutines must be type-annotated.
- **Testing:** Use `wc` to check file lengths.
- **Parallel execution:** Tasks should demonstrate parallel async execution using `asyncio.gather`.

---

## Files in the Project

### 1. `0-async_generator.py`
- **Task:** Write a coroutine called `async_generator` that:
  - Loops 10 times.
  - Asynchronously waits 1 second on each loop.
  - Yields a random number between 0 and 10 (using the `random` module).

**Example Usage:**
```bash
$ ./0-main.py
[4.4, 6.9, 6.2, 4.5, 4.1, 9.9, 6.7, 9.8, 1.0, 1.3]

