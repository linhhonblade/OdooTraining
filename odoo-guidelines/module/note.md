# Terminology

## ORM

A key component of Odoo is the ORM layer. This layer avoids having to write most SQL by hand and provides extensibility and security services.

Business objects are declared as Python classes extending `Model`

**Model Fields** are defined as attributes on the model class.

simple fields: `Boolean`, `Date`, `Char`

relational fields: linking records (same or different models)

doo creates a few fields in all models, they called **reversed fields**. They are managed by the system and shouldn’t be written to

## Data files

Each `<record>` element creates or updates a database record.

Data files have to be declared in the manifest file to be loaded.

## Actions and Menus

They are regular records in database, usually declared through data files

Actions can be triggered in 3 ways:
- clicking on menu item (linked to specific action)
- clicking on buttons in views (if connected to actions)
- as contextual actions on object

<mark>The action must be declared before its corresponding menu in the XML file.</mark>

<mark>Data files are executed sequentially, the action’s id must be present in the database before the menu can be created.</mark>

## Basic views

Views define the way the records of a model are displayed.

Views can either be requested generically via their type (the view with the correct type and the lowest priority will be used) or specifically via their id

### Generic view declaration

A view is declared as a record of the model `ir.ui.view`

<mark>The view’s content is XML.</mark>

<mark>The arch field must thus be declared as type="xml" to be parsed correctly.</mark>

### Tree view

Tree views, also called list views, display records in a tabular form.

Their root element is `<tree>`

### Form view

Forms are used to create and edit single records.

Their root element is `<form>`

Form views can also use plain HTML for more flexible layouts.

## Relational Field

Relational fields link records, either of the same model (hierarchies) or between different models.

- `Many2one`: a simple link to another object
- `One2many`: behaves as a container of records, accessing it results in a (possibly empty) set of records

<mark>Because a `One2many` is a virtual relationship, there must be a `Many2one` field in the `other_model`, and its name must be `related_field`</mark>

## Inheritance

### Model inheritance

2 inheritance mechanisms:
- traditional mechanism:
  - allows a module to modify the behavior of a model defined in another module
  - `_inherit` and `_name`
- delegated mechanism
  - allows to link every record of a model to a record in a parent model, and provides transparent access to the fields of the parent record.
  - `_inherit` only
  - > If there are new fields, restart odoo psql server and upgrade the module from apps list

### View inheritance

An extension view references its parent using the inherit_id field, and instead of a single view its arch field is composed of any number of xpath elements selecting and altering the content of their parent view

> If cannot see the new model u created, change to superuser

## Computed fields and default values

The ORM expects the developer to specify those dependencies on the compute method with the decorator `depends()`

`default=X`

## Onchange

The “onchange” mechanism provides a way for the client interface to update a form whenever the user has filled in a value in a field, without saving anything to the database.

For computed fields, valued onchange behavior is built-in

## Model constraints

### Python constraints

A Python constraint is defined as a method decorated with `constrains()`, and invoked on a recordset.

Raise exceptions

### SQL constraints

SQL constraints are defined through the model attribute `_sql_constraints`
