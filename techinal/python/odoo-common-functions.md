# Common functions you will encounter when diving throught odoo source code

## ensure_one()

self.ensure_one is made to ensure that only one record is being passed on. It checks that the current record is a singleton (so just one record, not multiple records). If self would contain multiple records the system would throw up an error.

A general rule of thumb is to only use self.ensure_one when you are sure / want to be sure you only have one record, not multiple.

You can use @api.one, but since @api.one put returned value in a list and it is not always supported by the web client, therefore most of the developers uses@api.multi with self.ensureone().

Read more on [readthedocs](https://odoo-new-api-guide-line.readthedocs.io/en/latest/decorator.html) and Odoo ORM API

```python
def ensure_one(self):
  """ Verifies that the current recordset hold a single record.
      Raises an exception otherwise.
  """
  if len(self) == 1:
    return self
  raise ValueError("Expected singleton: %s" % self)
```
