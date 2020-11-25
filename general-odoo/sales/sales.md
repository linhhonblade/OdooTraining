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

- If you decide to choose the Invoice what is delivered rule, you will not be able to activate the feature called Automatic invoice, which automatically generates invoices when the online payment is confirmed.
- When you request your first down payment, a new product called Down payment will be created. This product will be registered as a service product with an invoicing policy of ordered quantities. As a reminder, you can edit this product and modify it at any time. Please note that if you choose delivered quantities as invoicing policy, you will not be able to create an invoice.
- Be careful that if you do a down payment with a product using delivered quantities as invoicing policy, you won’t be able to deduct all the down payments when it comes to invoicing your customer. Indeed, you have to deliver a product before creating the final invoice. If nothing has been delivered, you create a credit note that cancels the draft invoice created after the down payment. To do so, you have to install the Inventory App to confirm the delivery. Otherwise, you can enter the delivered quantity manually on the sales order.

Note

- A single sale price per product : doesn’t let you adapt prices, it use default product price ;
- Different prices per customer segment : you will set several prices per products ;
- Advanced pricing based on formula : will let you apply discounts, margins and roundings.
- Make sure you have default prices set in the pricelist outside of the deals period. Otherwise you might have issues once the period over.
- Make sure you have default prices set in the pricelist outside of the deals period. Otherwise you might have issues once the period over.

Note

- Once again the system is smart. If a rule is set for a particular item and another one for its category Odoo will take the rule of the item.
- Make sure at least one pricelist item covers all your products.

## Fiscal Position (tax and account mapping)

Fiscal Positions allow you to create sets of rules to automatically adapt the taxes and the accounts used for a transaction.

They can be applied in various ways:
- automatically applied, based on some rules
- manually applied on a transaction
- assigned to a partner

> A few Fiscal Positions are already preconfigured on your database, as part of your Fiscal Localization Package.

### Tax and Account Mapping
- The mapping of taxes and accounts is based on the default taxes and accounts defined in the products’ forms.
- In the record of fiscal position:
  - To map to another tax or account, fill out the right column (Tax to Apply/Account to Use Instead).
  - To remove a tax, rather than replacing it with another, leave the field Tax to Apply empty.
  - To replace a tax with multiple other taxes, add multiple lines with the same Tax on Product.

> The mapping only works with active taxes. Therefore, make sure they are active by going to Accounting ‣ Configuration ‣ Taxes.

### Automatic application
To do so, open the Fiscal Position you want to modify and click on Detect Automatically. You can configure a few conditions:
- VAT Required
- Country group / country

> Taxes on eCommerce orders are automatically updated once the visitor has logged in or filled out their billing details.

> The Fiscal Positions’ sequence - the order in which they are arranged - defines which Fiscal Position to apply if the conditions are met in multiple Fiscal Positions.

For example, if the first Fiscal Position targets country A, and the second Fiscal Position targets a Country Group that also comprises country A, only the first Fiscal Position will be applied to customers from country A.

### Manual Application

- Assign fiscal position to a partner: open the partner’s contact form, go to the Sales & Purchase tab, edit the Fiscal Position field

- Choose Fiscal Positions manually on Sales Orders, Invoices, and Bills

## Sell in foreign currencies
- Check Allow multi currencies in Invoicing/Accounting ‣ Settings.
- Create one pricelist per currency. A new Currency field shows up in pricelist setup form.

### Automatic conversion from public price
### Set your own prices
