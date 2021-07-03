# Some special fields and variables

- `self._fields`: returns the fields which are available in that model to a dictionary type
- `model._fields[fieldname] will return the datatype of field as key and the field name with respective model as value
- example: `self._fields['price_unit']` in `sale.order.line` will return `Float: sale.order.line.price_unit`

## Hide fields from Odoo filter and groupby
```python
def fields_get(self, fields=None):
    res = super(ProjectTaskQa, self).fields_get()
    fields_to_hide = ['internal_name', 'external_name']
    for field in fields_to_hide:
        if res.get(field):
            res.get(field)['searchable'] = False #hide from filter
            res.get(field)['sortable'] = False #hide from group by
    return res
```

## Send inbox message and notification to specific user progamatically in Odoo13
```python
def button_validate(self):
    res = super(StockPicking, self).button_validate()
    #create condition only receipt document
    if self.picking_ytpe_id.code == 'incoming':
        #define purchase user by group
        purchase_group = self.env.ref('purchase.group_purchase_user')
        purchase_user = self.env['res.users].search([('groups_id', '=', purchase_group)])
        notification_ids = []
        for purchase in purchase_user:
            notification_ids.append((0,0,{
            'res_partner_id':purchase.partner_id.id,
            'notification_type':'inbox'}))
        self.message_post(body='This receipt has been validated!', message_type='notification', subtype='mail.mt_comment', author_id='self.env.user.partner_id.id', notification_ids=notification_ids)
    return res
```

