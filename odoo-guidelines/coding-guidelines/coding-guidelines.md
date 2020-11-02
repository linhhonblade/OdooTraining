---
theme: metropolis
title: Odoo General and Demo

author: 'Pham Thi Ngoc Mai'
institute: 'AHT'
date: August 12th, 2018
toc: true
slide_level: 2
mainfont: 'TimesNewRoman'
header-includes: |
  \metroset{progressbar=frametitle,sectionpage=progressbar}
  \usepackage[linesnumbered, ruled]{algorithm2e}
  \usepackage{subfig}
  \usepackage{mathptmx}
  \usepackage{multicol}

# pandoc coding-guidelines.md -t beamer -o slide.pdf
---

# Module Structure

# File Naming

## General Rules

> File name should only contains [a-z0-9_] (lowercase alphanumerics and _)

User correct file permissions:
- folder 755
- file 644

## Models

```
addons/plant_nursery/
|-- models/
|   |-- plant_nursery.py (first main model)
|   |-- plant_order.py (another main model)
|   |-- res_partner.py (inherited Odoo model)
```

## Security

```
addons/plant_nursery/
|-- security/
|   |-- ir.model.access.csv
|   |-- plant_nursery_groups.xml
|   |-- plant_nursery_security.xml
|   |-- plant_order_security.xml
```

## Views

```
addons/plant_nursery/
|-- views/
|   | -- assets.xml (import of JS / CSS)
|   | -- plant_nursery_menus.xml (optional definition of main menus)
|   | -- plant_nursery_views.xml (backend views)
|   | -- plant_nursery_templates.xml (portal templates)
|   | -- plant_order_views.xml
|   | -- plant_order_templates.xml
|   | -- res_partner_views.xml
```

## Data

```
addons/plant_nursery/
|-- data/
|   |-- plant_nursery_data.xml
|   |-- plant_nursery_demo.xml
|   |-- mail_data.xml
```

## Controllers

```
addons/plant_nursery/
|-- controllers/
|   |-- plant_nursery.py
|   |-- portal.py (inheriting portal/controllers/portal.py)
|   |-- main.py (deprecated, replaced by plant_nursery.py)
```

## Static

```
addons/plant_nursery/
|-- static/
|   |-- img/
|   |   |-- my_little_kitten.png
|   |   |-- troll.jpg
|   |-- lib/
|   |   |-- external_lib/
|   |-- src/
|   |   |-- js/
|   |   |   |-- widget_a.js
|   |   |   |-- widget_b.js
|   |   |-- scss/
|   |   |   |-- widget_a.scss
|   |   |   |-- widget_b.scss
|   |   |-- xml/
|   |   |   |-- widget_a.xml
|   |   |   |-- widget_a.xml
```

## Wizards

```
addons/plant_nursery/
|-- wizard/
|   |-- plant_order_make.py
|   |-- plant_order_make_views.xml
```

## Statistics Reports

```
addons/plant_nursery/
|-- report/
|   |-- plant_order_report.py
|   |-- plant_order_report_views.xml
```

## Printable Reports

```
addons/plant_nursery/
|-- report/
|   |-- plant_order_reports.xml (report actions, paperformat, ...)
|   |-- plant_order_templates.xml (xml report templates)
```

## Full structure

```
addons/plant_nursery/
|-- __init__.py
|-- __manifest__.py
|-- controllers/
|   |-- __init__.py
|   |-- plant_nursery.py
|   |-- portal.py
|-- data/
|   |-- plant_nursery_data.xml
|   |-- plant_nursery_demo.xml
|   |-- mail_data.xml
|-- models/
|   |-- __init__.py
|   |-- plant_nursery.py
|   |-- plant_order.py
|   |-- res_partner.py
|-- report/
|   |-- __init__.py
|   |-- plant_order_report.py
|   |-- plant_order_report_views.xml
|   |-- plant_order_reports.xml (report actions, paperformat, ...)
|   |-- plant_order_templates.xml (xml report templates)
|-- security/
|   |-- ir.model.access.csv
|   |-- plant_nursery_groups.xml
|   |-- plant_nursery_security.xml
|   |-- plant_order_security.xml
|-- static/
|   |-- img/
|   |   |-- my_little_kitten.png
|   |   |-- troll.jpg
|   |-- lib/
|   |   |-- external_lib/
|   |-- src/
|   |   |-- js/
|   |   |   |-- widget_a.js
|   |   |   |-- widget_b.js
|   |   |-- scss/
|   |   |   |-- widget_a.scss
|   |   |   |-- widget_b.scss
|   |   |-- xml/
|   |   |   |-- widget_a.xml
|   |   |   |-- widget_a.xml
|-- views/
|   |-- assets.xml
|   |-- plant_nursery_menus.xml
|   |-- plant_nursery_views.xml
|   |-- plant_nursery_templates.xml
|   |-- plant_order_views.xml
|   |-- plant_order_templates.xml
|   |-- res_partner_views.xml
|-- wizard/
|   |--make_plant_order.py
|   |--make_plant_order_views.xml
```


# XML Files

## Format

- User `record` tag to declare a record in XML file
- Place `id` attribute before `model`
- For field declaration:
  - `name` attribute first
  - value either in `field` tag or in `eval` attribute
  - other attributes (widget, options,...) ordered by importance
- Try to group all records by model

## Format

```xml
<record id="view_id" model="ir.ui.view">
    <field name="name">view.name</field>
    <field name="model">object_name</field>
    <field name="priority" eval="16"/>
    <field name="arch" type="xml">
        <tree>
            <field name="my_field_1"/>
            <field name="my_field_2" string="My Label" widget="statusbar" statusbar_visible="draft,sent,progress,done" />
        </tree>
    </field>
</record>
```
## Format

More at [Odoo Guidelines - XML Files](https://www.odoo.com/documentation/master/reference/guidelines.html#xml-files)

# Python

## PEP8

> Odoo source code tries to respect Python standard, but some of them can be ignored.

- E501: line too long
- E301: expected 1 blank line, found 0
- E302: expected 2 blank lines, found 1

## Import

The imports are ordered as:

- External libraries
- Import of `odoo`
- Import from odoo modules (rarely, and only if neccessary)

## Import

```python
# 1 : imports of python lib
import base64
import re
import time
from datetime import datetime
# 2 : imports of odoo
import odoo
from odoo import api, fields, models, _ # alphabetically ordered
from odoo.tools.safe_eval import safe_eval as eval
# 3 : imports from odoo addons
from odoo.addons.website.models.website import slug
from odoo.addons.web.controllers.main import login_redirect
```
## Idiomatics of Programming (Python)

Read more at [Odoo Coding Guidelines](https://www.odoo.com/documentation/master/reference/guidelines.html#idiomatics-of-programming-python)

## Idiomatics of Programming (Python)

- Each python file should have `# -*- coding: utf-8 -*-` as first line
- readability over conciseness
- Don't use `.clone()`

## Idiomatics of Programming (Python)
```python
# bad
new_dict = my_dict.clone()
new_list = old_list.clone()
# good
new_dict = dict(my_dict)
new_list = list(old_list)
```
## Idiomatics of Programming (Python)

Python dictionary : creation and update

```python
# -- creation empty dict
my_dict = {}
my_dict2 = dict()

# -- creation with values
# bad
my_dict = {}
my_dict['foo'] = 3
my_dict['bar'] = 4
# good
my_dict = {'foo': 3, 'bar': 4}

# -- update dict
# bad
my_dict['foo'] = 3
my_dict['bar'] = 4
my_dict['baz'] = 5
# good
my_dict.update(foo=3, bar=4, baz=5)
my_dict = dict(my_dict, **my_dict2)
```

## Idiomatics of Programming (Python)

Useless variable

```python
# pointless
schema = kw['schema']
params = {'schema': schema}
# simpler
params = {'schema': kw['schema']}
```

## Idiomatics of Programming (Python)

Multiple return points are OK, when they’re simpler

```python
# a bit complex and with a redundant temp variable
def axes(self, axis):
        axes = []
        if type(axis) == type([]):
                axes.extend(axis)
        else:
                axes.append(axis)
        return axes

 # clearer
def axes(self, axis):
        if type(axis) == type([]):
                return list(axis) # clone the axis
        else:
                return [axis] # single-element list
```
## Idiomatics of Programming (Python)

> You should at least have a basic understanding of all the [Python builtins](https://docs.python.org/3/library/functions.html)

## Idiomatics of Programming (Python)

Learn list comprehensions

```python
# not very good
cube = []
for i in res:
        cube.append((i['id'],i['name']))
# better
cube = [(i['id'], i['name']) for i in res]
```
## Idiomatics of Programming (Python)

Collections are booleans too

```python
bool([]) is False
bool([1]) is True
bool([False]) is True
```
## Idiomatics of Programming (Python)

Iterate on iterables

```python
# creates a temporary list and looks bar
for key in my_dict.keys():
        "do something..."
# better
for key in my_dict:
        "do something..."
# accessing the key,value pair
for key, value in my_dict.items():
        "do something..."
```
## Idiomatics of Programming (Python)

Use dict.setdefault

```python
# longer.. harder to read
values = {}
for element in iterable:
    if element not in values:
        values[element] = []
    values[element].append(other_value)

# better.. use dict.setdefault method
values = {}
for element in iterable:
    values.setdefault(element, []).append(other_value)
```

## Idiomatics of Programming (Python)

As a good developer, document your code (docstring on methods, simple comments for tricky part of code)






## Programming in Odoo

- Avoid to create generators and decorators: only use the one provided by Odoo API
- Use filtered, mapped, sorted to ease code reading and performance

## Programming in Odoo

- Make your method work in batch

```python
def my_method(self)
    for record in self:
        record.do_cool_stuff()
```

## Programming in Odoo

Do not perform a search or a search_count in a loop. It is recommended to use read_group method, to compute all value in only one request.

```python
def _compute_equipment_count(self):
""" Count the number of equipment per category """
    equipment_data = self.env['hr.equipment'].read_group([('category_id', 'in', self.ids)], ['category_id'], ['category_id'])
    mapped_data = dict([(m['category_id'][0], m['category_id_count']) for m in equipment_data])
    for category in self:
        category.equipment_count = mapped_data.get(category.id, 0)
```

## Programming in Odoo

Propagate the context

```python
records.with_context(new_context).do_stuff() # all the context is replaced
records.with_context(**additionnal_context).do_other_stuff() # additionnal_context values override native context ones
```

## Programming in Odoo

[Single-responsibility Principle](https://en.wikipedia.org/wiki/Single-responsibility_principle)

[Cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity)

## Programming in Odoo

[Never commit the transaction](https://www.odoo.com/documentation/master/reference/guidelines.html#never-commit-the-transaction)

Consequences:
- inconsistent business data, usually data loss
- workflow desynchronization, documents stuck permanently
- tests that can’t be rolled back cleanly, and will starpolluting the database, and triggering error (this is trueven if no error occurs during the transaction)

## Programming in Odoo

[Use translation method correctly](https://www.odoo.com/documentation/master/reference/guidelines.html#use-translation-method-correctly)

> Odoo uses a GetText-like method named “underscore” _( ) to indicate that a static string used in the code needs to be translated at runtime using the language of the context.

## Programming in Odoo

In general in Odoo, when manipulating strings, prefer `%` over `.format()` (when only one variable to replace in a string), and prefer `%(varname)` instead of position (when multiple variables have to be replaced).

This makes the translation easier for the community translators.

## Symbols and Conventions

When defining report model (SQL views e.i.) : use `<related_base_model>.report.<action>`, based on the Transient convention.

## Symbols and Conventions

Odoo Python Class : use camelcase (Object-oriented style).

```python
class AccountInvoice(models.Model):
    ...
```
## Symbols and Conventions

Model name (using dot notation, prefix by the module name)
- When defining an Odoo Model : use singular form of the name
- When defining an Odoo Transient (wizard) : use `<related_base_model>.<action>` Avoid the wizard word. For instance : account.invoice.make, project.task.delegate.batch, …


## Symbols and Conventions

Variable name :
- use camelcase for model variable
- use underscore lowercase notation for common variable.
- suffix your variable name with _id or _ids if it contains a record id or list of id. Don’t use partner_id to contain a record of res.partner

```python
Partner = self.env['res.partner']
partners = Partner.browse(ids)
partner_id = partners[0].id
```

## Symbols and Conventions

- `One2Many` and `Many2Many` fields should always have `_ids` as suffix (example: sale_order_line_ids)
- `Many2One` fields should have `_id` as suffix (example : partner_id, user_id, …)

## Method Conventions

- Compute Field : the compute method pattern is `_compute_<field_name>`
- Search method : the search method pattern is `_search_<field_name>`
- Default method : the default method pattern is `_default_<field_name>`
- Onchange method : the onchange method pattern is `_onchange_<field_name>`
- Constraint method : the constraint method pattern is `_check_<constraint_name>`
- Action method : an object action method is prefix with `action_`. Since it uses only one record, add `self.ensure_one()` at the beginning of the method.

## Attribute Order in a Model

- private attribute (`_name`, `_description`, `_inherit`, ...)
- default method and `_default_get`
- field declaration
- Compute, inverse and search methods in the same order as field declaration
- Selection method (methods used to return computed values for selection fields)
- Constrains methods (`@api.constrains`) and onchange methods (`@api.onchange`)
- CRUD methods (ORM overrides)
- Action methods
- And finally, other business methods.****

# Javascript and CSS

## Static files organization

- static: all static files in general
  - static/lib: this is the place where js libs should be located, in a sub folder. So, for example, all files from the jquery library are in addons/web/static/lib/jquery
  - static/src: the generic static source code folder
    - static/src/css: all css files
    - static/src/fonts
    - static/src/img
    - static/src/js
      - static/src/js/tours: end user tour files (tutorials, not tests)
    - static/src/scss: scss files
    - static/src/xml: all qweb templates that will be rendered in JS
  - static/tests: this is where we put all test related files.
    - static/tests/tours: this is where we put all tour test files (not tutorials).

## Javascript coding guidelines

- `use strict;` is recommended for all javascript files
- Use a linter (jshint, …)
- Never add minified Javascript Libraries
- Use camelcase for class declaration

[More](https://github.com/odoo/odoo/wiki/Javascript-coding-guidelines)

## CSS coding guidelines

- Prefix all your classes with `o_<module_name>` where `module_name` is the technical name of the module (‘sale’, ‘im_chat’, …) or the main route reserved by the module (for website module mainly, i.e. : ‘o_forum’ for `website_forum` module). The only exception for this rule is the webclient: it simply uses `o_` prefix.
- Avoid using id tag
- Use Bootstrap native classes
- Use underscore lowercase notation to name class

# Git

## Configure your git

- Be sure to define both the user.email and user.name in your local git config

```shell
git config --global <var> <value>
```

## Commit message structure

Commit message has four parts:
- tag
- module
- short description (<50 chars)
- full description

## Tag name

- [FIX]
- [REF]
- [ADD]
- [REM]
- [REV]
- [MOV]
- [REL]
- [IMP]
- [MERGE]
- [CLA]
- [l18N]

## Module name

- After tag comes the modified module name. Use the technical name
- If several modules are modified, list them or use various
- Unless really required or easier avoid modifying code across several modules in the same commit.

## Commit message header

Commit message header should make a valid sentence once concatenated with

`if applied, this commit will <header>`.

## Commit message full description

Specify the part of the code impacted by your changes (module name, lib, transversal object, …)

- WHY you are modifying code

## Commit message full description

>  If you are working on a task that lacks purpose and specifications please consider making them clear before continuing.

## Commit message full description

> Use the long description to explain the why not the what, the what can be seen in the diff

##
\centering
Thank you for listening!

## Refs

[Odoo Guidelines](https://www.odoo.com/documentation/13.0/reference/guidelines.html)

Học lại
- OOAD
- ADB
