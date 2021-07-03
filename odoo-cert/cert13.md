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

```
usage = fields.Selection([
   ('supplier', 'Vendor Location'),
   ('view', 'View'),
   ('internal', 'Internal Location'),
   ('customer', 'Customer Location'),
   ('inventory', 'Inventory Loss'),
   ('production', 'Production'),
   ('transit', 'Transit Location')], string='Location Type',
   default='internal', index=True, required=True,
   help="* Vendor Location: Virtual location representing the source location for products coming from your vendors"
        "\n* View: Virtual location used to create a hierarchical structures for your warehouse, aggregating its child locations ; can't directly contain products"
        "\n* Internal Location: Physical locations inside your own warehouses,"
        "\n* Customer Location: Virtual location representing the destination location for products sent to your customers"
        "\n* Inventory Loss: Virtual location serving as counterpart for inventory operations used to correct stock levels (Physical inventories)"
        "\n* Production: Virtual counterpart location for production operations: this location consumes the components and produces finished products"
        "\n* Transit Location: Counterpart location that should be used in inter-company or inter-warehouses operations")
```

### What is the purpose of location's type being set to view?
- [x] It's a location for creating the structure of the stock locations
- [ ] It's the only kind of location we can attach to warehouses
- [ ] It's the only kind of location we can use when creating starting inventories

### Is it possible to make a conversion btw two units of measure from different categories?
- [x] No

### Validating an Inventory Adjustment into the Inventory app will create:
- [x] One stock move per adjustment line with an updated qty
- [ ] One stock move for the whole inventory adjustment
- [ ] One stock move per product included the inventory
- [ ] One stock move per location used in the inventory
### When you manually update the Qty On Hand of a product via the "Update Qty" button on the product form view, does it generate a stock move?
- [x] Yes

### If the costing method of a product is set to "Average Price", will the unit cost of the product change when you deliver some to your clients?
- [x] No

### You currently have 20 chairs in stock which are configured to be purchased when a client place an order. If you were to sell 50 chairs to customer, how many units will be set on the automatically generated RFQ?
- [ ] 20 units
- [ ] 30 units
- [x] None of the above (should be 50 units)
![](odoo13cert/Screen%20Shot%202021-01-05%20at%2013.24.59.jpg)

## MRP

### How do you configure your BOM to produce several products at once (A + B = C + D)
- [x] You can define by product on BOM
- [ ] You can create a sub-bom (kits)
- [ ] You can define a byproduct on the routing()
### When are forecasted qty updated for components used in a manufacturing order?
- [x] At confirmation of manufacturing order
- [ ] At validation of finished product
- [ ] When manufacturing order is marked as Done
> **Forecasted Quantity**: The quantity of products you can sell for a specific warehouse or location. It is defined as the Quantity on Hand - Future Delivery Orders + Future incoming shipments + Future manufactured units.

### What document(s) will be generated when you confirm a sales order with a product that has a BoM type set as Kit

- [x] A delivery order with the components of the kit
- [ ] A manufacturing order to produce the kit and a delivery order
- [ ] A delivery order with the final prodcut (kits are used when purchasing)

### Once a manufaturing order is validated, can you produce more than initially expected?
- [x] Yes

### Can you define a routing without working center?
- [x] Yes, however no WO will be generated
- [ ] No, it is mandatory
- [ ] I don't know

### Can you define a quality control point on incoming shipments ?
- [x] Yes

> Just enable multi-steps routes and choose Input > Quality Control > Stock

> In Odoo13, no more routing in MO, the work order and work center is added directly in BoM, so that when choosing the BoM in MO, the data about work order and workcenter is populated also

### How is the Mean Time to Repair (MTTR) calculated?
- [x] Total downtime in days / number of breakdowns
- [ ] Total Up time in days / number of breakdowns
- [ ] Total time in days / number of breakdowns

### When is a stock move registered in a repair order?
- [x] When finishing a Repair Order
- [ ] At confirmation of repair order
- [ ] When starting a repair order

### With the subcontracting feature, how do you specify that a product is subcontracted
- [x] Via subcontracting selection in BOM Type
- [ ] Via a checkbox on the product template form
- [ ] Via a route on the sale order line

### What is the indirect demand forecast for the tabletop?
- [x] The demand coming from the need of table top as a component
- [ ] The demand for the product coming from the website
- [ ] The demand coming from non yet validated quotations

## CRM

### You want to add new contact to a company. The company alrd has an address, and you want to set a different one for its new contact. What do you do?
- [x] From the company, add a new contact of type "Other address" and edit its address
- [ ] From the company, add a new contact of type "Contact" and, after creation, edit its address
- [ ] Create the contact separately, set its address, then link it to the company

### How many quot/sale orders can you generate from one opp

### When reviewing your CRM pipeline what do the colored dots represent?
- [x] These are tags defined in the opp
- [ ] These are the products selected in the opportunity

### Which of the following fields is used by Odoo when detecting the duplicate leads?
- [x] email
- [ ] contact name
- [ ] opportunity name

### Archiving an opp is the same as marking it as "Lost"?
- [x] True

### The probability field indicates:
- [x] To probability to sign a deal with this prospect
- [ ] The probability of the opportunity to go to the next pipeline stage
- [ ] The probabilityto get an answer to the offer sent

### A meeting type is used to:
- [x] Create a meeting in the user calendar
- [ ] Automatically schedule the follow-up task
- [ ] Generate a link towards an online conference

### The expected revenue:
- [x] Can be set manually at any point
- [ ] Is computed based on the Untaxed Amount of the Sales orders linked to that opportunity
- [ ] Can only be set when creating the opportunity

### Can you manually link an existing SO to an existing Opp?
- [x] No, it's too late for that once both documents exist
- [ ] Yes through the "Link documents" button
- [ ] Yes, in debug mode on the Sale order

### Duplicating an opportunity
- [x] Will create an exact copy of the opp but bring it back to the first stage of the pipeline
- [ ] Will create an exact copy of the opportunity
- [ ] Will create a copy of this opportunity but set it as a lead

## eCommerce

### If during checkout you would like to show your customers additional products they may like. What feature would you use?
- [x] Accessory products
- [ ] Alternative products
- [ ] Optional products

> Alternative Products: Suggest alternatives to your customers (upsell strategy) Those products show up on the product page
> Accessories Products: Accessories show up when the customer reviews the cart before payment (cross-sell strategy)
> Optional Products: are suggested when the customer hits `Add to Cart` button (cross-sell strategy)

### On your eCommerce you can define the Promotion Program:
- [x] Base on Customers and/or Products
- [ ] Based only on Customers
- [ ] Based only on Products
- [ ] Based only for visitors

### If upon checkout on your eCommerce you want to show your customer additional products they may be interested in. Which feature would you use?
- [x] Optional products
- [ ] Alternative Prodcuts
- [ ] Accessory products

### When does Odoo generate a quot from eCommerce module
- [x] When product is added to cart
- [ ] When clicking "Process Checkout" in the shopping cart
- [ ] When payment is validated

## Introduction

### When printing a quote, how will Odoo determine which languages to use?
- [x] The language of the customer
- [ ] The language in the current user's preferences
- [ ] The language of the user's company

### Which of the following views are you not able to perform a multi level group-by?
- [x] Kanban
- [ ] List
- [ ] Graph
### In a multi-company environment, how do you define whether or not a customer record is visible for all companies
- [x] You should leave 'company' field empty
- [ ] This is not possible, every customer belongs to one company
- [ ] Check the box "Accessible to Everyone"

### If you were in any list view, how you display 1000 records at once?
- [ ] All records are always displayed
- [ ] By clicking on the page indicator, and entering 1-1000
- [ ] It is not possible, Odoo only displays 80 records per page

## Human Resource

### Is it possible to configure a leave to have no limit in term of the number of dates you can take?
- [x] Yes

![](Screenshot%20from%202021-03-26%2009-06-55.png)

### Where can you set an employee's work schedule?
- [x] On the contract (not employee form)
- [ ] On the employee form
- [ ] Both of the answers above

> On employee form, `Working Hours` field is `resourse.calendar.id`
> On the contract of employee there is also `Work Schedule` field which also relates to `resource.calendar.id`

### When is an expense is marked as Paid
- [ ] When the employee has paid for the expense but has not been reimbursed yet
- [x] When the employee has paid for the expense and has been reimbursed by the company
- [ ] As soon as the expense has been approved by the company

### Where is employee hourly cost defined for time-sheet tracking
- [x] Employee form
- [ ] On the sale order line linked to the task
- [ ] On the employee contract

## Timesheets

### What happens when a sale order is validated including a product with the following configuration?
![](odoo13cert/Screen%20Shot%202021-01-05%20at%2013.44.13.jpg)
- [x] Task is created in a new project and I can invoice the ordered quantity of the sale order at any time
- [ ] Task is created in a new project and I can invoice timesheeted (delivered) quantity
- [ ] Task is created in a new project and I can invoice the quantity of the sale order only when delivered quantity equals ordered quanity

### When looking at the Project Overview how is the "Fixed" calculation generated?
- [x] These are timesheeted hours linked to a sale order where the product invoice policy is set to "Order quantities"
- [ ] These are sold hours coming from a sale order that still need to be timesheeted before beeing invoiced
- [ ] These are the actual timesheeted hours that can't be invoiced from the sale order

> Billed on Timesheets: Includes the time logged into tasks for which you invoicee based on timesheets on tasks.
> Billed at Fixed price: Includes the time logged into tasks for which you invoice based on ordered quantities or on milestones
> Non Billable Tasks: Includes the time logged into a task which is not linked to any Sales Order.
> Invoiced: Revenues linked to Timesheet already invoiced
> To invoice: Revenues linked to Timesheets not yet invoiced
> Timesheet costs: This cost is based on the `Timesheet cost` set in the HR Settings of your employees
> Other costs: Any cost linked to the Analystic Account of the Project

### The timesheet app does not work offline
- [x] False
### What do Timesheet entries that in grey represent?
- [x] Timesheets validated by the manager
- [ ] Timesheets already invoiced
- [ ] Timesheets not yet validated by the manager
> We can validate timesheets by batch now

## Project

### What is the trigger for an automatic kanban status change
- [x] A customer reply to a feedback request on that specific kanban stage
- [ ] The task deadline is exceeded
- [ ] Total timesheeted time on that task is higer then initially planned hour
> [This video](https://www.youtube.com/watch?v=emqjX65NGgQ) showed that when you add a timesheet to New Task, the task automatically changed to In Progress stage but where the setting?

### Can task stages be shared accross multiple different projects?
- [x] Yes

### How do you restrict the visibility of tasks that are linked to a project?
- [x] Set up privacy level on project
- [ ] It can only be done using filters
- [ ] Setup privacy level on tasks

### It is possible to define different kanaban stages for different project?
- [x] True

### Which of the following statements is true? If your project is billed at the project rate:
- [x] The time and material spent on all of this project's tasks will be billed at the same rate to the same customer
- [ ] The time and material spent on this project's tasks will be billed to different customers at different rates.
- [ ] The time spent by each employee on this project will be billed to the same customer at a different rate

> Billing based on the project rate: All timesheets are billed by the same rate
> Billing based on the employee rate: Timesheets are billed by the individual rate of the employee.
> project rate: allows you to invoice a whole project, for a specfic service, at a specific rate, at once.
> employee rate: lets you invoice a project broken down into different services and different rates

### What kind of costs are taken into account in the Project Overview?
- [ ] The timesheet costs of your employees
- [ ] Any cost linked to the analytic account of the project
- [ ] Expense costs linked to the project's sales order
- [x] All of the above

### Which statement is true? If your project is billed at employee rate
- [x] The time spent by each employee on this project will be billed to the same customer at a different rate
- [ ] The time and material spent on all of this project's tasks will be billed at the same rate to the same customer
- [ ] The time and material spent on this project's tasks will be billed to different customers at different rates.

### When can you create a Sales Order from a project
- [x] When a Sales Order item is set on the project
- [ ] When a Sales Order is set on the project
- [ ] When a Sales Order is not set on the project

## Accounting

### How can you prevent someone from modifying and/or creating journal entries?
- [x] Set a lock date
- [ ] Close a period
- [ ] Post journal entries

### What kind of action can you define when using the payment follow-ups levels?
- [ ] Send email
- [ ] Print letter
- [ ] Send SMS
- [ ] Only email and letter are possible
- [x] All are possible

### What happens if an account is managed in a different currency than the company's currency?
- [x] Odoo stores the foreign currency amounts then store the converted amounts as the debit/credit in the company currency
- [ ] Odoo stores the debit/credit of all journal items in the account currency only
- [ ] Odoo converts amounts automatically and stores them in the company currency only

### What happens if a currency is not set on an account?
- [ ] The account can only be used for transactions in the main company currency (check again)
- [x] The account can be used for transaction in any currency
- [ ] It's not possible. A currency is required for each account
> On each account, you can set a currency. It will force all moves for this account to have the account currency.
> If you leave it empty, it means that it can handle all currencies that are Active.

> In order to register payments in other currencies, you have to remove the currency constraint on the journal.  If a currency is filled in, it means that you can register payments only in this currency.

> When creating or importing bank statements, the amount is in the company currency. But there are now two complementary fields, the amount that was actually paid and the currency in which it was paid.
### What does it mean when you see a blue line item on the bank reconciliation screen?
- [x] It shows a registered payment
- [ ] It means the payment is in another currency
- [ ] It's just an invoice
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
- [ ] The balance related to that customer in receivable account
- [ ] The sum of all unpaid invoices from this customer
- [x] The sum of invoices minus the sum of payments of this customer

### You cannot change a posted journal entries sequence but can you change its reference?
- [x] Yes, you can always change the reference of any journal entry
- [ ] No, you cannot modify anything in a posted journal entry
- [ ] You can only change the reference if the entry is not reconciled

## Purchase

### When you set your "Control Policy" to "On received Quantities", will receiving an incoming shipment update the amount to be invoiced?
- [x] Yes

### You configure a product to calculate its cost on a "Average Cost" basis and you currently have 8 units of it in stock with a cost of $100/unit. If you were to purchase and reveive 2 more units at a price of $10/unit, what will your new cost be?
- [x] 82

### Where do you define the vendor delivery lead time?
- [x] On the product
- [ ] On the vendor
- [ ] On the company

### If you have a product with several vendors assigned to it, which one will be used when automatically generated an RFQ?
- [x] The first supplier in the list
- [ ] The one with the smallest delivery lead time
- [ ] The one with smallest price

### If you configure a product to calculate its cost on a "Standard Price" basis and you currently have 8 units of it in stock with a cost of $100/unit. If you were to purchase and receeive 2 more units at a price of $10/unit, what will new cost be?
- [x] $100

### Where do you define a product's costing method?
- [x] Product category
- [ ] On the product
- [ ] On the company (all products have the same costing method)

### When you generate a request for quoation on an agreement type set to "Use quantitites of agreement" which of the following is true:
- [x] The qty in the RFQ can still be changed
- [ ] The qty is set to 0 by default
- [ ] The qty in the RFQ cannot be changed

### If a product's costing method is set to "Average Cost" will the cost of the product form change when you receive some units?
- [x] Yes

### What does it mean if the forecasted qty of a stockable product is less than the qty on hand?
- [x] There are prolly more outgoing products planned than incoming products
- [ ] Nothing as we don't know the complete history of each product
- [ ] New products are planned to arrive in stock

### In "Automatic Invoice" mode when is the invoice generated?
- [x] When the online payment is confirmed by the payment acquirer
- [ ] When the sales order is confirmed by the user

### What will be the scheduled delivery date if I confirm a sales order on Sep 1st for a product that has a customer lead time 5 days and 2 sales safety days? Note that there is enough stock to deliver
- [x] Sept 4th
- [ ] Sept 8th
- [ ] Sept 2nd

### What does this product configuration imply?
![Route Buy + Make To Order](odoo13cert/Screen%20Shot%202021-01-05%20at%2014.13.11.jpg)
![](odoo13cert/Screen%20Shot%202021-01-05%20at%2014.13.17.jpg)
- [x] The product will be ordered from a vendor every time a sales or manufacturing order is validated
- [ ] If there is a reordering rule set, the product will be manufactured once the rule is triggered
- [ ] The Product will be manufactured everytime a sales or manufacturing order is validated

### If you would like to group speccific sales order lines together to generate subtotals what feature would you use
- [ ] Product categories
- [ ] Sequence on quotation lines
- [x] Sections
### What does this product configuration imply?
![Route Buy](odoo13cert/Screen%20Shot%202021-01-05%20at%2014.13.53.jpg)
![](odoo13cert/Screen%20Shot%202021-01-05%20at%2014.14.03.jpg)
- [x] If a reordering rule is set up, the product will be ordered from a vendor when the rule is triggered
- [ ] The product will be oredered from a vendor everytime a sales or manufacturing order is validated
- [ ] The product will be manufactured everytime a sales or manufacturing order is validated

### Which of the following is true when you select "Display margin on quotation and sales order" under sales configuration?
- [ ] Changing the cost price on the order line will compute a new unit price according to the calculation in the pricelist
- [x] The order lines of the quoation will show both unit price and cost price from the product, as well as the margin by calculating the difference between the unit price and the cost price
- [ ] Margins are only display on the sales orders, not on quotations

# Odoo Certification Test 14

## ???
![](Screenshot%20from%202021-03-23%2014-46-41.png)
- [ ] 3 days from today
- [ ] 5 days from today
- [7] 7 days from today
> If today you schedule a call, the call will has deadline in 2 days. If you done the call right a way, the Reminder will be schedule and has deadline in 7 days
## When and where do you configure the "Lost Reasons" you want your Sales team to use?
- [ ] They are created when the application is installed and can never be modified
- [ ] They can only be set up once before creating any opportunity
- [x] They can be modified by a user with enough access rights at any time

## Archiving an opportunity is the same as marking it as "Lost"
- [x] True
- [ ] False
- [ ] Idk

## Which of the following fields can be used to automatically compute probability?
- [x] Source
- [ ] Job Position
- [ ] Priority
- [ ] Idk

## The Probability field indicates:
- [ ] The probability that the opportunity will move to the next stage in your pipeline
- [ ] The probability of getting a responose to the offer letter
- [x] The pobability of signing a deal with this prospect
- [ ] Idk

## What does converting an Opportunity mean

## You've customized a Building Block; Is it possible to re-use it?
- [x] Yes, you can save it and re-use it anywhere on your website
- [ ] No
- [ ] Yes, but with the HTML/CSS editor
- [ ] Idk

## When you install the Website app, you're ased to choose a Theme. Is it possible to change the theme later on?
- [x] Yes, go to the Option tab in Edit mode and choose "Switch Theme"
- [ ] No, this choice is definitive, and you'lll have to create another website
- [ ] Yes, switch to debug mode, then go to Website > Settings
- [ ] Idk

## Will Odoo automatically picks the best Color Combinations for each Building Block?
- [ ] No, you can customize the colors in the options tab
- [x] Yes, but you can customize the colors in the options tab
- [ ] Yes, and you have a limited selection of what you can change in the option tab

## Are keyboard shortcuts only available in the backend?
- [ ] It's not possible
- [x] No, they're also available in the frontend (e.g. "Esc" to hide the top bar)
- [ ] Idk

## Can you add a Google Map to locate your business on your website?
- [ ] Yes but you have to use HTML/CSS editor to do that
- [x] Yes, as long as you have your google credentials adding is simple
- [ ] Idk

## When editting a form, how are mandatory fields distinguished from non-mandatory fields?
- [ ] The input zone is yellow
- [ ] The label has a star
- [x] The line below the input zone is bold
- [ ] Idk

## When printing a quote, how does Odoo determine which language to use?
- [ ] Use the language defined on the current user's preferences
- [ ] Use the language defined on the customer record
- [ ] Use the language defined by the company of the user

## In which of the following views are you not able to perform a multi-level group
-  [x] The kanban view
-  [ ] The list view
-  [ ] The graph view
-  [ ] Idk

## In a multi-company environment, how do you define whether or not a customer record is visible for all companies
- [ ] This is not possible since every customer belongs to one company
- [x] Leave the "Company" field empty
- [ ] Check the box "Accessible to Everyone"
- [ ] Idk

## What does the small icon on the right side of the field below means (the translation icon)


# Search

- Redirect when a conference is over: redirect to the next recommend email
- utm
- apply surcharge in discount odoo (the order of surcharge, discount and rouding)
- company security lead time
- non-billable in project overview
- timesheet cost on product and employee
- when tax log (before fiscal year lock or after)
- costing method landed cost
- trigger for marketing automation (sms or email)
- click on the color bar on the top of the kanban column
- order of tax lock date: tax lock before year end
- scheduled activities (time of deadline)
- auto update kanban state: create activity in Marketing Automation with activity type is a server action
-

> Any new transaction which accounting date is prior to the Tax Lock Date has its tax values moved to the next open tax period. This is useful to make sure that no change can be made to a report once its period is closed.

> Therefore, we recommend locking your tax date before working on your Closing Journal Entry. This way, other users can’t modify or add transactions that would have an impact on the Closing Journal Entry, which helps you avoid some tax declaration errors.

# Odoo Experience Talks and Quizzes

## Payroll and Work Entries
### Is it possible to manage at the same time the payslips of two employees that are under different salary structures?
- [ ] No
- [ ] Yes, but you need to validate the generation of the payslips twice
- [x] Yes

### What happens if you have conflicts on the work entries of the month?
- [ ] Nothing, it is just an alert from Odoo but you can still generate your payslips
- [ ] There is an alert on the employee form
- [x] You can not generate payslips

### How can you integrate the time off of your employees with the work entries in the payroll application?
- [ ] You need to specify them on the contract of the employee
- [x] You don't have anything to do, the time off application is fully integrated with the payroll application
- [ ] You need to enter manually each time off in the payroll application

## Odoo14 Unveiling Keynote
### What is Odoo Spreadsheet?
- [x] A new feature of Odoo Documents to create spreadsheets

**Use can use hot key while doing survey now**

## Supply chain management for post-COVID

### Advanced analytics can improve supply forecast accuracy by...
- [ ] 10% to 40%
- [x] 20% to 60%
- [ ] 40% to 100%

### What can the supply chain industry learn after the pandemic?
- [ ] Gained insights into process improvements
- [ ] More sustainable and efficient operations
- [x] Both

### What is not automated even when using Odoo?
- [ ] The purchasing workflow
- [ ] RFQs sent based on stock levels
- [x] Coffee roasting

## Accounting Consolidation Made Easy

### Which accounting standards are available in Odoo?
- [ ] US GAAP
- [ ] IAS/IFRS
- [x] None
### Which consolidated reports can be built with Consolidation?
- [ ] Profit & Loss
- [ ] Balance Sheet
- [x] Both of them and much more
### Which exclusion method does not exist in Consolidation?
- [x] Partner
- [ ] Account
- [ ] Journal

## Budget and Forecast with Odoo Spreadsheet

### How often is the data updated in a spreadsheet?
- [ ] Once a day
- [ ] Every hour
- [x] Real time update

### Where are the spreadsheet files stored?
- [ ] In the chatter
- [x] In the Documents app
- [ ] In the Accounting app

### Where can you generate a spreadsheet from?
- [ ] From any view in Odoo
- [ ] From the pivot view
- [x] From the pivot view and the Documents app

## Customize Payroll Benefits

### How to compute the net salary?
- [ ] By configuring my advantages
- [x] I need the payroll application to create a rule and compute the details of the salary
- [ ] I don't know

### What is the goal of the confignrator?
- [ ] Compute a basic salary based on advantages and yearly budget
- [x] Compute a salary slip
- [ ] Define the yearly employee budget

### Which part(s) of the Salary Configurator can you customize yourself?
- [ ] Only the advantages
- [ ] You cannot customize anything
- [x] There are 3 possible customization: advantages, the summary of the salary package and personal info

## Odoo Digital Campaigns
### In Odoo, what are the 3 activity types you can use when launching an marketing automation campaign?
- [x] Email/SMS/Server Action
- [ ] Email/SMS/Social Post
- [ ] Email/SMS/LiveChat

### What functionality is commonly used to easily design amazing content?
- [x] Drag & Drop
- [ ] Look & Feel
- [ ] Push & Pull

### Which one of new features will give you insight on initial results?
- [ ] Custom preview text
- [x] 24h mail recap
- [ ] Mail header snippet

**New functionalities in Odoo14 Automation Marketing**
- 24 hours mail recap: The creator of the campaign will receive an email everyday just to show the overview of the data
- Custom preview text:
- Mail header snippet:

> POS now responsive, added product configurator, easier to config when you are in POS interface in Odoo14

## SMS Marketing

Features:

1. Easier to create/generate contact list
2. build your own SMS template
3. Easier to select/filter preferred target audiences
4. Scheduling future day
5. Use emoji
6. Include opt-out link
7. Dynamic placeholder generator (new in 14)
8. Users can now send an SMS on their own contact to test the service with their own phone (new in 14)

### What is new feature implemented on Odoo14 that was not in Odoo 13
- [x] Users can now send an SMS on their own contact to test the service with their own phone
- [ ] You can add dynamic placeholders to SMS messages.
- [ ] You can keep archives of SMS messages sent
- [ ] You can include a opt-out link to SMS messages

### What are the limits in characters for standard messages and unicode messages
- [x] 160 & 70
- [ ] 70 & 160
- [ ] 100 & 50
- [ ] 140 & 60

### What can you do with the SMS Marketing App
- [ ] Warn your most loyal customers about something special happening
- [ ] Send Holiday Sales Campaigns
- [ ] Event reminders
- [x] All of the Above

> The GSM-7 set is a set of characters that can be used in a standard SMS.

> So, to allow the end user's device to rebuild correctly the SMS, the limit is reduced to 153 characters and 67 characters.

## Odoo Purchase: Automate Supplier Follow-Ups Based on OTDs

### How is the on-time delivery ratio calculated?
- [x] As the quantity of units that a supplier has delivered on time divided by the total quantity of unit delvered by this supplier
- [ ] As the number of POs delivered on time by a supplier divided by the total number of PO delivered by this supplier
- [ ] It is not calculated but defined manually on the contact delivery

### How are reminders sent to suppliers to confirm a delivery on an expected date?
- [ ] Manually
- [ ] Automatically
- [x] Either manually or automatically

### What piece of information cannot be found on the RFQs list view?
- [ ] The RFQs dashboard and the purchase KPIs
- [x] The on-time delivery ratio
- [ ] The remaining days before that the deadline to turn the RFQ into a PO is met

## A No Brainer: the Bank Reconciliation Tool
Prior to v14, no journal entries were generated when you created a bank statement. However, it wasn't until you reconciled a bank statement line with the invoices/bills or manually wrote off your transaction into an income or expense account that a journal entry was generated

In v14, as soons as you generate the bank statement report and post it another change but more on that later, Odoo will generate an acconting entry or entry equal to the number of bank statement lines. Each entry will hit this bank suspense account (in journal) and also the bank account.

&rarr; You will have an up-to-date report both on your balance sheet as well as your accounting dashboard to see what your bank accounts looks like, assumes that you're using the integrated or synchronization to get regular update

### When does Odoo hit the Suspense account?
- [ ] When you register a payment on an invoice or vendor bill
- [ ] When you reconcile your book with your bank
- [x] When you post your bank statement

### Will Odoo let you move forward with reconciliation if your bank ending balance and computed balance don't match?
- [ ] Yes
- [x] No

### What is arguably the biggest new feature for v14 bank reonciliation?
- [ ] The suspense account
- [ ] The outstanding payment
- [x] Reconciling manual journal entries

## Scheduling Made Easy: Planning and Time Off
### In the Planning app, under Gantt and Calendar view, what colors are global holidays and employee time off displayed in?
- [ ] Red
- [x] Grey
- [ ] Yellow
### Can the employees that do not have an Odoo user have access to their shifts?
- [ ] No, they need a user for this
- [ ] Yes, they will have access through the portal but they won’t be able to request to take open shifts nor inform that they are unavailable for the shifts they have been assigned to.
- [x] Yes, they will have access through the portal and will be able to request to take open shifts and inform when they are unavailable for the shifts already assigned to them.
### What other paid apps must you have in order to be able to use Time Off?
- [ ] Payroll
- [ ] Planning
- [x] None

## CRM Workshop: Learn How to Manage your Pipeline

> Odoo probability lead scoring is based on your previous success rate and other criteria that you can add or remove freely
> In Odoo14, tags in Opportunity will sync to sales order
> In Odoo14, CRM now integrated with Rental App

### What is a lead in Odoo?
- [ ] A lead is a prospect with a confirmed sale
- [x] A lead is an optional step before an opportunity
- [ ] A lead is a prospect that has been verified as a real person with correct contact information

### The chatter is the best way to:
- [x] Keep track of interactions with prospects
- [ ] Track the health of a prospective opportunity
- [ ] Send automated outreach to the prospect

## What's new in Odoo14 Studio
> Mass editing in listview
> Sort by field (u choose)
> Avatar
> Approval
> Column now has invisible option
> Field type added in field name created in Studio
> New Model Configurator (Suggested features for your new model)

### The new Approval Rules option lets you:
- [ ] Link any app to the Approvals app
- [ ] Add a rating system to restrict younger viewers from
- [x] Require certain users to approve or deny any action like "Confirm" or "Validate"
### The new Model Configurator will allow user to:
- [ ] Let you use "variants" with anything else in the system, like accounts, sales, contacts, etc. just like the product configurator.
- [x] Quickly create new models or apps with a menu of possible field types and features you want it to generate.
- [ ] Build a 3D super model like a virtual Heidi Klum to promote your business on your website and in emails.

### The new Avatar feature can be used in order to:
- [x] Allow you to represent data such as many-to-one fields with a nice visual representation.
- [ ] Allow you to automatically calculate taxes based on region and commodity.
- [ ] Allow you to transform into a tall blue alien with big ears

## Odoo Documents Workshop: Digitize Your Business
> In Odoo14:

> Create Spreadsheet: Standard reports or create new one
> Drag and Drop to upload file

### What configuration function allows you to push or act on a document?
- [ ] Tags
- [ ] Shares & Emails
- [x] Actions

### What feature must be used to view the versioning of any documents?
- [x] Replace button
- [ ] Lock button
- [ ] Tags

## SEO Tips and Tricks to Promote Your Website

> Google wont prioritize websites without reponsive
> Can optimize SEO in every single page
> Disable the Index in Page Properties (Website frontend) will tell Google that dont display that page as search result
> Google Analytics, Google Console Search, robot.txt, sitemap

### Where do you activate the mobile friendly version of Odoo Website
- [ ] Go to Website Configuration, scroll down to the SEO section. Then activate the Mobile Friendly option.
- [ ] When selecting a theme for your website, make sure you select a theme that is mobile friendly.
- [x] oo Website is mobile friendly by default.

## Where can you optimize the title and description of any section of your website?
- [x] In your website, click the Promote menu.
- [ ] In the html code editor.
- [ ] In the Robots file.

### Which sections of your website can be optimized for SEO?
- [ ] The main website and the blog.
- [ ] The main website and the online store.
- [x] The whole website.

## What's New in Odoo14 Inventory
> Raise AWafrnet if the products you are going to delivery will expired in ifles days

> Inventory cannot work offline but barcode scanner can work offline (only if you have loaded the pickings in advanced). Then you can scan, the data will be loaded into cache, but to validate all those pickings, you have to connect Internet.

## Odoo eLearning: the Best Tool to Create Online Course
### How can a student earn points?
- [ ] Voting
- [ ] Commenting
- [ ] Finishing the course
- [x] All of the above

### How can you share extra documents with your students?
- [x] Adding links in the external link tab of the content
- [ ] Adding links in the external link tab of the course
- [ ] Adding the links in the descripition of the content

### How can you move a content to another course?
- [ ] It's not possible
- [ ] By duplicating the content
- [x] Changing the course in Content

## Barcode Scanner: Advanced Flows for Inventory Optimization
### What is an additional advantage of the batch picking when you are in the barcode module?
- [ ] You have nice colors on your screen
- [x] It groups products by location to optimize the picking flow
- [ ] It groups products by order

### If you receive an additional product from a vendor that wasn't in your PO, what would you do?
- [ ] Too bad, you absolutely have to create new PO in your back-end for this order
- [ ] You keep this product for your personal interest
- [x] You need to add a product during your picking operation

### Not said during the presentation, but, what do you have to pay attention to when using a USB scanner?
- [ ] Your scanner needs to use the same language keyboard as your computer
- [x] Language keyboard as your computer
- [ ] The battery is enough to last at least a day
> Just make sure when you buy it that the scanner is compatible with your keyboard layout or can be configured to be so (Odoo Docs)
> By default Odoo has 50 ms delay between each successive scan (It helps avoid accidental double scanning). If you want to suppress this delay, you can configure your scanner to insert a carriage return at the end of each barcode.

## An Efficient Manufacturing Process with the Work-Order Tablet View
### Smart devices can be used to:
- [ ] To perform control points in the manufacturing
- [ ] To pilot the work-center tablet view
- [x] Both

### Time per operation is:
- [ ] set manually
- [ ] computed and updated automatically
- [x] Both

## Inventory & MRP: The New Replenishment Mechanism
### What can't be changed in the new replenishment menu?
- [ ] The vendor to which we desire to send the RFQ
- [ ] The route from which a product would be procured
- [x] The expected delivery date at which a product should be delivered

### What does not appear by default in the new replenishment menu?
- [x] Automated reordering rules
- [ ] Manual reordering rules
- [ ] Products with a negative forecasted quantity

### What is not possible to do in one click with the new replenishment menu?
- [x] Change the default vendor for a product (i.e. change the vendor appearing at first place in the vendor pricelist)
- [ ] Switch a manual reordering rule into an automated reordering rule
- [ ] Hide for one day a product that should not be replenished today

