# Website

- change picture quality (make website loadfaster)
- list view improved
![List View Odoo 13](crm1.png)
![List View Odoo 14](crm2.png)
- expected recuring revenue in CRM opp
![Expected Recuring Revenue](crm3.png)

# Inventory

- Replenishment
  - safety stock minimum
  - maximum
  - lead time to procure the different products, base on this lead time, we check the future forecast of this stock and if it's below the safety stock, then we will reorder to get up to the maximum
  - small icon beside quantity:
    - forecasted stock
    - available (red icon when available < qty order)

![inventory](inventory1.png)
![](inventroy2.png)
![](Screenshot%20from%202021-01-28%2016-36-00.png)
![](Screenshot%20from%202021-01-28%2016-41-50.png)

  - If your product is not available (because all the on-hand products are reserved), change the priority of the delivery order -> your product is reserved
  - Forecasted = On hand - confirmed orders (after sum of lead time vendor lead time + purchase security lead time + days to purchase)
  - Forecasted + Pending = onhand - confirmed orders + incoming products - unconfirm orders (quotations)

# Barcode

- wave picking
- batch picking
- cluster picking

# Timesheet

- Shortcut for switching project and log work
- use hot key to add 15m to a specific project

# Expenses

- record expenses by snapping a picture (Odoo App)

# Manufacturing

- Create MO without BoM (you define work orders directly in MO form)

![](MO1.png)
![](MO2.png)

# Purchase

- Better list view

![](purchase1.png)
![](purchase2.png)

- show on-time delivery rate of vendor on RFQ

![](purchase3.png)
