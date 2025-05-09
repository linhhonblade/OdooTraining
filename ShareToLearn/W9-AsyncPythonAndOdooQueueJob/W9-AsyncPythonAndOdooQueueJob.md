---
theme: "Singapore"
colortheme: "seahorse"
title: Asynchronous in Python and Odoo
author: 'Mailovemisa'
institute: 'A1 Consulting'
date: May 9th, 2025
toc: true
slide_level: 2
mainfont: "merriweather"
fontsize: 10pt
linkstyle: bold
urlcolor: red
lang: en-US
aspectratio: 169
header-include: |
    \metroset{progressbar=frametitle,sectionpage=progressbar}

# pandoc report.md -t beamer -o slide.pdf
---

# Thread and Process

+-------------------------+-------------------------------+-------------------------------+
| Feature                 | Process                       | Thread                        |
+-------------------------+-------------------------------+-------------------------------+
| Definition              | Independent executing unit    | Lightweight subprocess        |
|                         | with its own memory space     | sharing process memory        |
+-------------------------+-------------------------------+-------------------------------+
| Memory Usage            | High                          | Low                           |
+-------------------------+-------------------------------+-------------------------------+
| Isolation               | Fully isolated                | Share memory and resources    |
+-------------------------+-------------------------------+-------------------------------+
| Communication           | IPC (Inter-Process Comm.)     | Shared memory (fast)          |
+-------------------------+-------------------------------+-------------------------------+
| Creation Overhead       | Heavy                         | Light                         |
+-------------------------+-------------------------------+-------------------------------+
| Crash Impact            | Does not affect others        | Can crash the whole process   |
+-------------------------+-------------------------------+-------------------------------+
| Context Switching       | Slower (more overhead)        | Faster                        |
+-------------------------+-------------------------------+-------------------------------+
| Scheduling              | Handled by OS                 | Handled by OS or user space   |
+-------------------------+-------------------------------+-------------------------------+
| Use Case Example        | Web servers, services         | Concurrent tasks in a program |
+-------------------------+-------------------------------+-------------------------------+
| Scalability             | Less than threads (per cost)  | More scalable (per core)      |
+-------------------------+-------------------------------+-------------------------------+
| Lifetime                | Independent of others         | Tied to parent process        |
+-------------------------+-------------------------------+-------------------------------+


# Concurrency vs Parallelism

+------------------------+-----------------------------+------------------------------+
| Feature                | Concurrency                 | Parallelism                  |
+------------------------+-----------------------------+------------------------------+
| Definition             | Dealing with multiple       | Executing multiple tasks     |
|                        | tasks at once (interleaving)| simultaneously               |
+------------------------+-----------------------------+------------------------------+
| Task Execution         | Tasks progress independently| Tasks run at the same time   |
|                        | and may overlap             | literally in parallel        |
+------------------------+-----------------------------+------------------------------+
| Hardware Requirement   | Single or multi-core        | Requires multi-core CPU      |
+------------------------+-----------------------------+------------------------------+
| Context Switching      | Yes                         | Not necessarily              |
+------------------------+-----------------------------+------------------------------+
| Time Sharing           | Yes                         | No (tasks have dedicated cores)|
+------------------------+-----------------------------+------------------------------+
| Goal                   | Structure and responsiveness| Speed and efficiency          |
+------------------------+-----------------------------+------------------------------+
| Example (Human)        | One cook juggling dishes    | Multiple cooks doing dishes  |
+------------------------+-----------------------------+------------------------------+
| Example (Code)         | Async I/O, goroutines       | Vectorized computation       |
|                        | (e.g., Go, Python async)     | (e.g., SIMD, GPU threads)    |
+------------------------+-----------------------------+------------------------------+
| Determinism            | Harder to predict timing     | More predictable under load  |
+------------------------+-----------------------------+------------------------------+
| Main Focus             | Task management              | Execution throughput         |
+------------------------+-----------------------------+------------------------------+

**In short**:

**Concurrency** is about dealing with lots of things at once.

**Parallelism** is about doing lots of things at once.

# I/O bound vs CPU bound



# Python GIL

## What is Python GIL?

**Global Interpreter Lock** is a mutex in **CPython** (the reference Python implementation). It allows only one thread to execute Python bytecode at a time, even on multi-core systems

## Why GIL?

1. C extension is not thread-safe
2. Garbage Collection and Reference Counting

## How Python achieve Concurrency with GIL?

0. Don't use CPython :D or wait new Python version (maybe)

1. `threading`

-  allows the creation of multiple threads.
-  only one thread executes Python code at a time.
-  Good for I/O-bound tasks

2. `asyncio` (3.4+)

- single-threaded, event loop-based concurrency.
- `async`, `await`


```python
async def my_coroutine():
    await asyncio.sleep(1)
    return "done"
```
- Python sử  dụng **async def** để định nghĩa một hàm là hàm bất đồng bộ (một coroutine) và từ khóa await để tạm dừng và chờ kết quả từ các task vụ (python coroutines).
- Coroutine hiểu một cách đơn giản các hàm có thể tạm dừng và tiếp tục thực thi tại các điểm khác nhau
- **Await** được sử dụng để chờ một coroutine hoàn thành mà không chặn luồng chính.

3. Which to choose?

+---------------------------+-----------------------------+-----------------------------+
| Feature                   | threading                   | asyncio                     |
+---------------------------+-----------------------------+-----------------------------+
| Concurrency Model         | Preemptive (OS-controlled)  | Cooperative (event loop)    |
+---------------------------+-----------------------------+-----------------------------+
| Parallelism               | Limited by GIL (1 thread runs)| No parallelism (single thread) |
+---------------------------+-----------------------------+-----------------------------+
| Thread Count              | One thread per task         | One thread, many coroutines |
+---------------------------+-----------------------------+-----------------------------+
| Task Switching            | OS switches threads         | Code yields via `await`     |
+---------------------------+-----------------------------+-----------------------------+
| Blocking Behavior         | Blocking by default         | Non-blocking (requires `await`)|
+---------------------------+-----------------------------+-----------------------------+
| Suitable For              | I/O-bound & some CPU-bound  | I/O-bound only              |
+---------------------------+-----------------------------+-----------------------------+
| Performance (I/O tasks)   | Good, but with more overhead| Excellent, lightweight      |
+---------------------------+-----------------------------+-----------------------------+
| Performance (CPU tasks)   | Poor unless GIL is released | Bad, will block entire loop |
+---------------------------+-----------------------------+-----------------------------+
| Complexity                | Easier to write initially   | Requires async mindset      |
+---------------------------+-----------------------------+-----------------------------+
| Debugging                 | Hard (race conditions)      | Easier (fewer sync bugs)    |
+---------------------------+-----------------------------+-----------------------------+
| Library Support           | Broad, legacy compatible    | Growing, but not universal  |
+---------------------------+-----------------------------+-----------------------------+
| Example Module            | `threading`                 | `asyncio`                   |
+---------------------------+-----------------------------+-----------------------------+


# How to achive Parallelism in Python?

Threads in CPython can only run in parallel if they're waiting on I/O (e.g. file, network) or running non-Python native code (e.g. NumPy in C, image libraries, etc.).

0. Don't use CPython
1. `multiprocessing` + multi core:
- `multiprocessing` spawns separate processes with:
  - Its own memory space
  - Its own Python Interpreter
  - Its own GIL
&rarr; `multiprocessing` **enable** parallelism **if** hardware support it.
- multiprocessing on single-core &rarr; all processes will still be executed sequentially (context switching at OS level) &rarr; no performance benefit
  - Increase Overhead
  - More Memory Usage
  - No Parallelism

&rarr; **true parallelism only when you have multiple cores**

# How Odoo achives Concurrency?

## FastAPI

- FastAPI allows you to define asynchronous endpoints using Python's async def syntax.

## Worker vs Process

## Odoo process

# Odoo Queue Job

