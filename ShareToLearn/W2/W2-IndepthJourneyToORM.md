---
theme: "Singapore"
colortheme: "seahorse"
title: An In-depth Journey into Odoo's ORM
author: 'Pham Thi Ngoc Mai'
institute: 'Onnet - AHT'
date: September 3rd, 2021
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

## Implementation requirements

- Be correct
- Be secure:
  - access rights
  - against external attacks, sql injections
- Be effient:
  - scalable algorithm
  - few and efficient SQL queries: the cost in term of time of every SQL query is huge compared to the cost of simple computation in python code

## Key data structures

- Registry
- Record cache
- Fields to write
- Fields to compute
- Field triggers

# Registry

## What?

A place where every model name is associated to a python class

```python
class Registry(Mapping):
    """ Model registry for a particular database.

    The registry is essentially a mapping between 
        model names and model classes.
    There is one registry instance per database.

    """
    ...
```

##

::: columns
:::: {.column width=40%}
```python
# Model definitions
class Foo0(models.Mode):
    _name = 'foo'
    ...
class Foo1(models.Model):
    _inherit = 'foo'
    ...
class Foo2(models.Model):
    _inherit = 'foo'
    ...
```
::::
:::: {.column width=60%}
```python
# Model classes
class foo(Foo2, Foo1, Foo0, Base):
    _name = 'foo'
    ...
```
::::
:::

##

- Goal: map **model_name** to **model_class**
- **model_class** should reflect model definitions
- **browse()** returns an instance of **model_class**
- holds metadata

## Why?

- Determine fields by introspection
- Add custom fields
- Add `_inherits` fields
- Setup fields (parameters, depends, ...)

## Challenges:

- Getting the **model classes** right
- **Performance**  of setup

# Record cache

## What ?

- Goal: **augmented** database cache
- Stores **field values**
- Accessible on **environment**