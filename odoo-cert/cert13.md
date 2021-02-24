# Odoo Certification Test 13

## Inventory

### In a normal situation, a 'customer location' has a positive stock value or a negative stock value?
- [x] posivtive
- [ ] negative
- [ ] should tend to zero
- [ ] idk
*vendor location and virtual location/inventory adjustment: negative*

### Where do you define the cost of a product that has variants?
- [x] At product variant level
- [ ] At product level
- [ ] At attribute level

### Does manually updating the Qty On Hand of a product generate the same stock moves as validating an Inventory Adjustment for the same product, location and qty
- [x] Yes

### What stock moves will be generated when you make an inventory adjustment increasing a product on hand qty from 0 to 5 units

- [ ] A move from an internal location to an inventory location
- [x] A move from an inventory location to an internal location
- [ ] A move between two internal locations
> Should be inventory loss location ?

### What is the purpose of location's type being set to view?
- [x] It's a location for creating the structure of the stock locations

### Is it possible to make a conversion btw two units of measure from different categories?
- [x] No

### Validating an Inventory Adjustment into the Inventory app will create:
- [x] One stock move per adjustment line with an updated qty

### When you manually update the Qty On Hand of a product via the "Update Qty" button on the product form view, does it generate a stock move?
- [x] Yes

### If the costing method of a product is set to "Average Price", will the unit cost of the product change when you deliver some to your clients?
- [x] No

### You currently have 20 chairs in stock which are configured to be purchased when a client place an order. If you were to sell 50 chairs to customer, how many units will be set on the automatically generated RFQ?
- [ ] 20 units
- [ ] 30 units
- [x] None of the above (should be 50 units)

## MRP

### How do you configure your BOM to produce several products at once (A + B = C + D)
- [x] You can define by product on BOM

### When are forecasted qty updated for components used in a manufacturing order?
- [x] At confirmation of manufacturing order
> **Forecasted Quantity**: The quantity of products you can sell for a specific warehouse or location. It is defined as the Quantity on Hand - Future Delivery Orders + Future incoming shipments + Future manufactured units.

### What document(s) will be generated when you confirm a sales order with a product that has a BoM type set as Kit

- [x] A delivery order with the components of the kit

### Once a manufaturing order is validated, can you produce more than initially expected?
- [x] Yes

### Can you define a routing without working center?
- [x] Yes, however no WO will be generated

### Can you define a quality control point on incoming shipments ?
- [x] Yes

### How is the Mean Time to Repair (MTTR) calculated?
- [x] Total downtime in days / number of breakdowns

### When is a stock move registered in a repair order?
- [x] When finishing a Repair Order

### With the subcontracting feature, how do you specify that a product is subcontracted
- [x] Via subcontractor field in BOM

### What is the indirect demand forecast for the tabletop?
- The demand coming from the need of table top as a component

## CRM

### You want to add new contact to a company. The company alrd has an address, and you want to set a different one for its new contact. What do you do?
- [x] From the company, add a new contact of type "Other address" and edit its address

### How many quot/sale orders can you generate from one opp

### When retrieving your CRM pipeline what do the colored dots represent?
- [x] These are tags defined in the opp

### Which of the following fields is used by Odoo when detecting the duplicate leads?
- [x] email

### Archiving an opp is the same as marking it as "Lost"?
- [x] True

### The probability field indicates:
- [x] To probability to sign a deal with this prospect

### A meeting type is used to:
- [x] Create a meeting in the user calendar

### The expected revenue:
- [x] Can be set manually at any point

### Can you manually link an existing SO to an existing Opp?
- [x] No, it's too late for that once both documents exist

### Duplicating an opportunity
- [x] Will create an exact copy of the opp but bring it back to the first stage of the pipeline

## eCommerce

### If during checkout you would like to show your customers additional products they may like. What feature would you use?
- [x] Accessory products

### On your eCommerce you can define the Promotion Program:
- [x] Base on Customers and/or Products

### If upon checkout on your eCommerce you want to show your customer additional products they may be interested in. Which feature would you use?
- [x] Optional products

### When does Odoo generate a quot from eCommerce module
- [x] When product is added to cart

## Introduction

### When printing a quote, how will Odoo determine which languages to use?
- [x] The language of the customer

### Which of the following views are you not able to perform a multi level group-by?
- [x] Kanban

### In a multi-company environment, how do you define whether or not a customer record is visible for all companies
- [x] You should leave 'company' field empty

### If you were in any list view, how you display 1000 records at once?

## Human Resource

### Is it possible to configure a leave to have no limit in term of the number of dates you can take?
- [x] No

### Where can you set an employee's work schedule?
- [x] On the contract (not employee form)

### When is an expense is marked as Paid

### Where is employee hourly cost defined for time-sheet tracking
- [x] Employee form

## Timesheets

### What happens when a sale order is validated including a product with the following configuration?
![](odoo13cert/Screen%20Shot%202021-01-05%20at%2013.44.13.jpg)
- [x] Task is created in a new project and I can invoice the ordered quantity of the sale order at any time

### When looking at the Project Overview how is the "Fixed" calculation generated?
- [x] These are timesheeted hours linked to a sale order where the product invoice policy is set to "Order quantities"

### The timesheet app does not work offline

### What do Timesheet entries that in grey represent?
- [x] Timesheets validated by the manager

## Project

### What is the trigger for an automatic kanban status change
- [x] A customer reply to a feedback request on that specific kanban stage

### Can task stages be shared accross multiple different porjects?
- [x] No

### How do you restrict the visibility of tasks that are linked to a project?
- [x] Set up privacy level on project

### It is possible to define different kanaban stages for different project?
- [x] True

### Which of the following statements is true? If your project is billed at the project rate:
- [x] The time and material spent on all of this project's tasks will be billed at the same rate to the same customer

### What kind of costs are taken into account in the Project Overview?
- [ ] The timesheet costs of your employees
- [ ] Any cost linked to the analytic account of the project
- [ ] Expense costs linked to the project's sales order
- [x] All of the above

### Which statement is true? If your project is billed at employee rate
- [x] The time spent by each employee on this project will be billed to the same customer at a different rate

### When can you create a Sales Order from a project
- [x] When a sales order item is set on the project

## Accounting

### How can you prevent someone from modifying and/or creating journal entries?
- [x] Set a lock date

### What kind of action can you define when using the payment follow-ups levels?
- [ ] Send email
- [ ] Print letter
- [ ] Send SMS
- [ ] Only email and letter are possible
- [x] All are possible

### What happens if an account is managed in a different currency than the company's currency?
- [x] Odoo stores the foreign currency amounts then store the converted amounts as the debit/credit in the company currency

### What happens if a currency is not set on an account?
- [x] The account can only be used for transactions in the main company currency

### What does it mean when you see a blue line item on the bank reconciliation screen?
- [x] It shows a registered payment

### Can Odoo automatically update currency exchange rates?
- [x] Yes

### Which of the following formats are you not able to use in order to import bank statements into Odoo
- [x] XBRL
- [ ] CODA
- [ ] CSV
- [ ] CAMT

### What will the result of the next depreciation calculation be?
- [x] A (800/5 = 160)

### How is the total due by a customer computed?
- [x] The balance related to that customer in receivable account

### You cannot change a posted journal entries sequence but can you change its reference?
- [x] Yes, you can always change the reference of any journal entry

## Purchase

### When you set your "Control Policy" to "On received Quantities", will receiving an incoming shipment update the amount to be invoiced?
- [x] Yes

### You configure a product to calculate its cost on a "Average Cost" basis and you currently have 8 units of it in stock with a cost of $100/unit. If you were to purchase and reveive 2 more units at a price of $10/unit, what will your new cost be?
- [x] 82

### Where do you define the vendor delivery lead time?
- [x] On the product

### If you have a product with several vendors assigned to it, which one will be used when automatically generated an RFQ?
- [x] The first supplier in the list

### If you configure a product to calculate its cost on a "Standard Price" basis and you currently have 8 units of it in stock with a cost of $100/unit. If you were to purchase and receeive 2 more units at a price of $10/unit, what will new cost be?
- [x] $100

### Where do you define a product's costing method?
- [x] Product category

### When you generate a request for quoation on an agreement type set to "Use quantitites of agreement" which of the following is true:
- [x] The qty in the RFQ can still be changed

### If a product's costing method is set to "Average Cost" will the cost of the product form change when you receive some units?
- [x] Yes

### What does it mean if the forecasted qty of a stockable product is less than the qty on hand?
- [x] There are prolly more outgoing products planned than incoming products

### In "Automatic Invoice" mode when is the invoice generated?
- [x] When the online payment is confirmed by the payment acquirer

### What will be the scheduled delivery date if I confirm a sales order on Sep 1st for a product that has a customer lead time 5 days and 2 sales safety days? Note that there is enough stock to deliver
- [x] Sep 4th

### What does this product configuration imply?
![Route Buy + Make To Order]()
- [x] The product will be ordered from a vendor every time a sales or manufacturing order is validated

### What does this product configuration imply?
![Route Buy]()
- [x] If a reordering rule is set up, the product will be ordered from a vendor when the rule is triggered

### Which of the following is true when you select "Display margin on quotation and sales order" under sales configuration?
- [x] Changing the cost price on the order line will compute a new unit price according to the calculation in the pricelist

### If you would like to group specific sales order lines together to generate subtotals what feature would you use?
- [x] Sections
