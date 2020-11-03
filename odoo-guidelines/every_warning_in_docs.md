# Warning

## ORM API

### Model

- if multiple fields with the same name are defined in the `_inherits`-ed models, the inherited field will correspond to the last one (in the inherits list order).
- you cannot define a field and a method with the same name, the last one will silently overwrite the former ones.
- Strings representing dates and datetimes can be compared between each other, however the result may not be the expected result, as a datetime string will always be greater than a date string, therefore this practice is heavily discouraged.
- While it is possible to use the same compute method for multiple fields, it is not recommended to do the same for the inverse method.
- `_log_access` must be enabled on `TransientModel`
- Contrary to what the name implies, it is currently possible for recordsets to contain duplicates. This may change in the future (14.0)
- `@constrains` only supports simple field names, dotted names (fields of relational fields e.g. partner_id.customer) are not supported and will be ignored.
- `@constrains` will be triggered only if the declared fields in the decorated method are included in the create or write call. It implies that fields not present in a view will not trigger a call during a record creation. A override of create is necessary to make sure a constraint will always be triggered (e.g. to test the absence of value).
- Executing raw SQL bypasses the ORM, and by consequent, Odoo security rules. Please make sure your queries are sanitized when using user input and prefer using ORM utilities if you don’t really need to use SQL queries
- when using delegation inheritance, methods are not inherited, only fields
- `_inherits` is more or less implemented, avoid it if you can;
- chained `_inherits` is essentially not implemented, we cannot guarantee anything on the final behavior.
- The Activity view is only available when the mail module is installed, and for the models that inherit from the `mail.activity.mixin`.



- To create a model without any table, inherit from `AbstractModel`
- To parse date/datetimes coming from external sources:
```python
fields.Date.to_date(self._context.get('date form'))
```
- Datetime fields are stored as timestamp without timezone columns in the database and are stored in the UTC timezone. This is by design, as it makes the Odoo database independent from the timezone of the hosting server system. Timezone conversion is managed entirely by the client side.
- If you consider introducing new exceptions, check out the odoo.addons.test_exceptions module.

# Q&A

## Differences between ir and res in base module

- ir = information repository
- res = resource

A resource matches something in the 'real world' that you store in OpenERP - to represent information about partners, or products or accounting transactions.

The Information Repository is used to store data needed by OpenERP to know how to work as an application - to define menus, windows, views, wizards, database tables, etc.

When we specify any files inside this demo field in the manifest- the data is only installed if the ‘Load Demo Data’ option is enabled at the time of database creation, otherwise, the demo data will not be loaded.
