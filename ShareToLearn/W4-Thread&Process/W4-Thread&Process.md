---
theme: "Singapore"
colortheme: "seahorse"
title: Multithreading and Multiprocessing in Python
author: 'Pham Thi Ngoc Mai'
institute: 'Onnet - AHT'
date: September 30th, 2021
toc: false
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
# Introduction

# Thread & Process

## What is Process?

### Process

::: columns
:::: column

- **Process** is a program in execution state
- Process Control Block (PCB) is the brain of process

::::
:::: column

![Process Components](images/process_components.jpg){width=60%}

::::
:::

## What is Thread?

### Thread

- a single flow of execution
- belongs to a process
- can be considered as a lightweight process

## Single-threaded process

- Default
- Only one thread per process

## Multi-threaded process

::: columns
:::: column

- More than one thread per process
- Share memory allocation (heap, global data) among threads
- Different stack

::::
:::: column

![Multi-threaded process](images/ThreadDiagram.jpg){width=60%}

::::

## Why

## CPU-bound and I/O-bound processes

- A program is **CPU bound** if it would go faster if the CPU were faster
- A program is **I/O bound** if it would go faster if the **I/O subsystem** (disk, networking) was faster

# Multithreading and Multiprocessing

## Multithreading

## Multiprocessing

# GIL

## What?

## Why Python GIL?

## Pros and Cons

# In Odoo


