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

| Feature               | Threading                                 | Process                                    |
| --------------------- | ----------------------------------------- | ------------------------------------------ |
| **Memory Usage**      | Threads share memory space                | Each process has its own memory space      |
| **Concurrency Model** | Shared memory, light-weight tasks         | Heavy-weight, independent tasks            |
| **Communication**     | Easier (shared memory)                    | Requires inter-process communication (IPC) |
| **Creation Cost**     | Low (lightweight)                         | High (more resources per process)          |
| **Context Switching** | Fast (lighter weight)                     | Slower (heavier processes)                 |
| **Suitability**       | I/O-bound tasks, cooperative multitasking | CPU-bound tasks, isolation needed          |
| **Parallelism**       | Not possible in CPython (due to GIL)      | True parallelism (multiple cores)          |



# Concurrency vs Parallelism

| Feature                     | Concurrency                                                  | Parallelism                           |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------- |
| **Definition**              | Multiple tasks progress concurrently, but not simultaneously | Multiple tasks run at the same time   |
| **Execution**               | Tasks are interleaved, may or may not run simultaneously     | Tasks run on different CPUs/cores     |
| **Context Switching**       | The system switches between tasks based on availability      | Tasks are executed simultaneously     |
| **Ideal Use Case**          | I/O-bound tasks, like network operations                     | CPU-bound tasks, like processing data |
| **Requires Multiple Cores** | No, can be done on a single-core CPU                         | Yes, to fully utilize parallelism     |
| **Main Focus**              | Managing multiple tasks at once                              | Completing multiple tasks at once     |


**In short**:

**Concurrency** is about dealing with lots of things at once.

**Parallelism** is about doing lots of things at once.

# I/O bound vs CPU bound

| Feature                     | I/O-Bound Task               | CPU-Bound Task                         |
| --------------------------- | ---------------------------- | -------------------------------------- |
| **Bottleneck**              | Waiting for external I/O     | Heavy computations or processing       |
| **Examples**                | File read/write, network I/O | Image processing, scientific computing |
| **Resource Usage**          | Blocks on I/O devices        | Consumes CPU cycles                    |
| **Execution Style**         | Lots of idle time            | Continuous processing                  |
| **Best Concurrency Tool**   | `asyncio`, `threading`       | `multiprocessing`, native C            |
| **GIL Friendly?**           | Yes (can release GIL on I/O) | No (GIL becomes bottleneck)            |
| **Performance (I/O tasks)** | Excellent with `asyncio`     | Poor with asyncio                      |
| **Performance (CPU tasks)** | Poor with `asyncio`          | Excellent with multiprocessing         |
| **Parallelism Benefit**     | Low benefit (not CPU bound)  | High benefit (multi-core processing)   |
| **Optimization Strategy**   | Use async to overlap I/O     | Use multiprocessing for parallel tasks |


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

| Feature                     | Threading                   | Asyncio                         |
| --------------------------- | --------------------------- | ------------------------------- |
| **Concurrency Model**       | Preemptive (OS-controlled)  | Cooperative (event loop)        |
| **Parallelism**             | Limited by GIL (1 thread)   | No parallelism (single thread)  |
| **Thread Count**            | One thread per task         | One thread, many coroutines     |
| **Task Switching**          | OS switches threads         | Code yields via `await`         |
| **Blocking Behavior**       | Blocking by default         | Non-blocking (requires `await`) |
| **Suitable For**            | I/O-bound & some CPU-bound  | I/O-bound only                  |
| **Performance (I/O tasks)** | Good, but more overhead     | Excellent, lightweight          |
| **Performance (CPU tasks)** | Poor unless GIL is released | Bad, will block entire loop     |
| **Complexity**              | Easier to write initially   | Requires async mindset          |
| **Debugging**               | Hard (race conditions)      | Easier (fewer sync bugs)        |
| **Library Support**         | Broad, legacy compatible    | Growing, but not universal      |
| **Example Module**          | `threading`                 | `asyncio`                       |



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

# How Odoo achieves Concurrency?

## FastAPI

- FastAPI allows you to define asynchronous endpoints using Python's async def syntax.
- **await** vs `backgroundtask`

| Feature            | **`await`**                                                                         | **`BackgroundTask`**                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Purpose**        | Wait for completion of an asynchronous task within the same request-response cycle. | Execute long-running tasks asynchronously in the background without blocking the HTTP response.         |
| **Use Case**       | I/O-bound tasks like API requests, database queries, file I/O.                      | Non-critical, time-consuming tasks like sending emails, processing data, logging.                       |
| **Blocking**       | Yes, the client waits until the task is complete before receiving the response.     | No, the client receives an immediate response, while the task continues running in the background.      |
| **When to Use**    | When you need the result of an operation before returning the response.             | When the task does not need to affect the immediate response to the client.                             |
| **Example**        | `data = await fetch_data()` — client waits for data.                                | `background_tasks.add_task(send_email, email)` — email is sent in the background.                       |
| **Response Time**  | The HTTP response is delayed until the task completes.                              | The HTTP response is sent immediately, even though the background task is still running.                |
| **Task Execution** | Task runs as part of the same request cycle.                                        | Task runs independently in the background, allowing the event loop to continue handling other requests. |
| **Suitable For**   | Tasks where the client needs the result (e.g., data fetching, computations).        | Tasks that are independent of the client’s immediate needs (e.g., logging, notifications).              |

# How Odoo achieves Parallelism?

## Odoo multi-worker mode

**Odoo’s multi-worker mode** is a production-grade deployment configuration that allows Odoo to handle multiple requests in **parallel** by using **multiple processes** (not just threads). This enables true concurrency and scalability, especially on multi-core servers, and is essential for running Odoo in production environments under high load.

- `workers = 0`: single-threaded
- `workers > 0`: Odoo forks multiple worker processes, each capable of handling requests concurrently. These workers are independent processes, not threads, so they bypass the GIL and utilize multiple CPU cores.

## Worker vs Process

| Feature                | **Odoo Worker**                                     | **Generic Process (OS-level)**                      |
| ---------------------- | --------------------------------------------------- | --------------------------------------------------- |
| **Definition**         | An Odoo-managed process handling HTTP or cron jobs  | An independent unit of execution managed by the OS  |
| **Controlled By**      | Odoo master process                                 | Operating System                                    |
| **Used For**           | Handling web requests, cron jobs, background tasks  | Any standalone task or application logic            |
| **Lifecycle**          | Spawned and monitored by Odoo                       | Created by `fork()`, `multiprocessing`, etc.        |
| **Parallel Execution** | Yes (true parallelism using multiple CPU cores)     | Yes                                                 |
| **Memory Space**       | Separate memory space (per worker)                  | Separate memory space                               |
| **Crash Handling**     | Respawned by Odoo master process                    | Not automatically respawned unless explicitly coded |
| **Concurrency Model**  | One worker = one process = one concurrent task      | One process can spawn threads or subprocesses       |
| **Communication**      | Indirect (via DB, cache, or IPC)                    | Inter-process communication (e.g., pipes, sockets)  |
| **Resource Planning**  | Tuned via Odoo config (`workers`, `limit_memory_*`) | Managed by system-level resource control            |
| **Deployment Context** | Web server / WSGI layer (e.g., behind Nginx)        | Any application context                             |


## How workers are created?

Odoo Master Process (PID 1000) 
├── HTTP Worker #1 (PID 1001) 
├── HTTP Worker #2 (PID 1002) 
├── HTTP Worker #3 (PID 1003) 
├── Cron Worker #1 (PID 1004) 
├── Cron Worker #2 (PID 1005) 
├── Queue Job Worker #1 (PID 1006) 
├── Queue Job Worker #2 (PID 1007) 
└── Add-ons (e.g., custom threads/processes)

- Odoo Master Process:
  - Launches and supervises all workers.
  - Manages lifecycle: starts, monitors, and restarts workers as needed.
- HTTP Workers:
  - Handle incoming web requests (REST API, UI, RPC).
  - Each runs in its own process (true parallelism).
- Cron Workers:
  - Run scheduled actions (ir.cron jobs).
  - Number controlled by max_cron_threads config.
- Queue Job Workers (from queue_job module):
  - Dedicated to running background job queue tasks.
  - Launched separately via a command like:
  - Not directly managed by Odoo’s main process (optional depending on setup), but shown here for logical hierarchy.

## Odoo Queue Job - JobRunner

| Responsibility               | Description                                                                 |
| ---------------------------- | --------------------------------------------------------------------------- |
| **Fetch ready jobs**         | Queries the database for jobs with state `pending`, `enqueued`, etc.        |
| **Lock job**                 | Locks the job row in the DB to prevent multiple workers from running it.    |
| **Run the job function**     | Executes the actual Python function associated with the job.                |
| **Error handling / retries** | Catches exceptions, logs failures, and schedules retries if configured.     |
| **Update job status**        | Sets status to `done`, `failed`, or `retry` after execution.                |
| **Channel coordination**     | Enforces **per-channel exclusivity** (i.e., one job per channel at a time). |

