# Sales

## Basic

- Odoo will search an external database and come up with a list of results related to what u type in customer field
- If u select one, odoo automatically creates a new contact on your own system with the data fetched from external data
- Enable Product Configurator in Sales Settings to Select product attributes and optional products from the sales order
- Add optional product from Product Template, Sales tab
- Can change unit price manually in Quotation
- Can type equation to unit price
- Make Quot looks nicer and easier to digest by adding a section or note
- If customer confirm the quot Sign & Pay, quot changes into SO, or we can confirm ourself manually
- Once Quot move to SO, a Delivery order is automatically generated if the product needs to be delivered

## Product Variants

- Enable in Sales Settings
- You will not be able to modify Variants Creation mode once the Attribute is created
- Variants Creation Mode:
  - Instantly: all possible variants are created as soon as the attribute and its values are added to a product
  - Dynamically: each variant is created only when its corresponding attributes and values are added to sales order
  - Never: variants are never created for the attribute
- Can add HTML color code for color attribute
- One Attribute can have multiple values
- For some variants with extra price: specify `Value Price Extra`
- If this attribute value is not compatible with other values: specify in `Exclude for`

## Online Quotations

- Quotation Template: Create standardized offers with defaut products
- When you click Sign & Pay from the quot u received by email, it will redirect u to the website page that you design for the quotation template
- Customer will be able to add optional products to their quot
- If customer Sign and Pay and select payment method (wiretransfer) there is log note in the chatter says that quot is waiting for wire transfer
- Use deadline in Quot template to stimulate customer to act

## Delivery Prices

- Activate Shipping Costs
- Two default provider: Fixed price and Based on rules
- Destination Availability
- The price of the delivery cost will be orange if we are using the price which is not following the rule we set up
- The sequence in pricing tab of Shipping method (Based on rule) does matter
- The firs one of the list will be the first to apply

## Delivery Lead Time (Customer Lead Time)

- When you confirm order, the delivery date will be computed and show in other info tab
- Add additional security lead time for sales in Inventory app (applied to all products) (the scheduled date of the WH/OUT will be earlier)

## Dropshipping

- Activate dropshipping in Purchase Settings
- Make sure dropship is selected in Inventory tab of product template and add a vendor to Purchase tab
- If you have multiple vendors, the first in the list will be selected for dropshipping
- When u confirm SO, DO not automatically generated but PO instead
- Go to the Purchase app and confirm that PO and receive product, then we see `Operation Type` Dropship, validate the DS
- Then the delivery order is created (and in done state) on the SO

## Pricelists - Multiple

- Activate in Sale Settings

### Multiple prices per product

- Specify Pricelists in Sales & Purchase tab in Contact or Quotation

### Advanced price rules (discount, formula)

- If change pricelist in SO, you have to remove and add product again in order to reset the price
- Can add Country group and eCommerce promo code to Configuration tab of Pricelists
- Selectable: Allow end user to select this pricelist

## Others

- Deliver and invoice to different address: enable Customer Addresses in sales setting
- If you select a customer with defined invoice and delivery addresses, Odoo will automatically use them to fill in the fields. Now, if you want to change it instantly, it is possible to do so directly from the quotation or the sales order.
- enter billing and shipping addresses under the Contacts & Addresses tab of Customer form

- To track & invoice expenses, you will need the expenses app
- You should also activate the analytic accounts feature to link expenses to the sales order


