# About Odoo Certification

## The main focus

- Sales
- CRM
- eCommerce

- Accounting/Invoicing

- Inventory
- Purchase
- Manufacturing

- Employees
- Timesheets
- Projects
- Expenses

> The answers often in e-learning
> Focus on Odoo Enterprise
> Follow  the business logic

## Learn Odoo Principles

- Fields: type, store or not
- Models:
- Functions

> Configuration, Master Data, Transactional Data



# Odoo Functional Certification Sample Test

## Introduction

### 1. What will this filter do?

![](IntroV12-Q3.jpg)

- [ ] Filter opportunities that are either in France or Belgium
- [x] Returns an empty list, as no opportunity is both in France and Belgium
- [ ] It will group opportunities by country
- [ ] Idk

### 2. Can you display 1000 records at once in list view?

- [ ] All records are alway displayed, nothing to do
- [x] Yes but you need to click on the page indicator, and enter 1-1000
- [ ] No, Odoo only display 80 records per page
- [ ] Idk

## CRM

### 1. How many quotations and orders can you generate from one opportunity?

- [ ] Serveral quotations, but only one order
- [x] Serveral quotations, serveral orders
- [ ] Only one quotation or order active at the same time
- [ ] Idk

### 2. In general, which is more likely to win?

- [ ] Lead
- [x] Opportunity
- [ ] Idk

### 3. What happens when you click on the little "+" button?

![](crm.png)

- [ ] It creates a stage that will come after this one
- [ ] You will be able to configure the stage
- [x] It creates an opportunity in this stage
- [ ] Idk

## Inventory

### 1. How many strock moves happen when you validate an inventory adjustment?
  - [ ] One stock move for the whole inventory adjustment
  - [x] One stock move per adjustment line with an updated quantity
  - [ ] One stock move per product included the inventory
  - [ ] One stock move per location used in the inventory
  - [ ] Idk

### 2. Where can you define costing method
  - [ ] On the product
  - [x] On the product category
  - [ ] On the company (all products have the same costing method)

### 3. I have 40 units of "Chair" in stock, with a product cost $50 per unit, 20 units belonging to myself and 20 units belonging to Azure Interior (owner), what is my inventory value for the chairs?

- [ ] 1000$
- [x] 2000$
- [ ] 1500$
- [ ] Idk

## MRP

### 1. How would you set up a Bill of Material to produce several finished products (A+B=C+D)?

- [x] Define "byproducts" on the bill of material
- [ ] It is not possible to have two different finished products
- [ ] Use sub-bom (kits)
- [ ] Idk

### 2. Can I continue manufacturing operation without having to validate a quality check if one is requested?

- [ ] Yes
- [x] No
- [ ] Idk

### 3. Is it possible to create a routing operation without work center?

- [ ] Yes
- [ ] No
- [ ] Idk

## eCommerce

### 1. Where is the pricelist of the first time visitors defined for an eCommerce website?

- [ ] It's on the settings of the website
- [ ] There is no pricelist used in eCommerce, it uses product prices
- [x] The pricelist linked to the public user
- [ ] Idk

### 2. What happens when product is added to the cart?

- [x] Odoo generates a quotation
- [ ] Odoo generates an opportunity
- [ ] Nothing
- [ ] Idk

## Human Resources

### 1. When is an expense marked as "Paid"?

![](HRV12-Q7.jpg)

- [ ] When the employee has paid for the expense, but has not been reimbursed yet
- [x] When the employee has paid for the expense and has been reimbursed by the company
- [ ] As soon as the expense has been approved by the company
- [ ] Idk

### 2. How would you allocate one leave per day (PTO) per month work?

- [x] Create a new leave type with allocation mode "Fixed by HR"
- [ ] Create a new allocation and configuring its "accrual" option
- [ ] Configuring a work schedule on the employee
- [ ] It's not possible to do that
- [ ] Idk

## Timesheets

### 1. What does this do

![](TimesheetsV12-Q3(1).png)
![](TimesheetsV12-Q3(2).jpg)

- [ ] Task is created in a new project and I can manually set delivered quantity to invoice on the sale order
- [ ] Task is created in a new project and I can invoice the ordered quantity of the sale order at any time
- [x] A new project is created and I can manually set delivered quantity to invoice on the sale order
- [ ] Idk

### 2. Can you timesheet your hours with the timesheet app offline?

- [x] Yes
- [ ] No
- [ ] Idk

## Project

### 1. How would you ask a rating to your customers when a task gets done?

- [ ] Set a client as follower of the task
- [ ] It's not possible
- [x] Set an email template on the "Done" state
- [ ] Idk

### 2. Can a task belong to multiple projects?

- [ ] Yes
- [x] No
- [ ] Idk

### 3. Does task need to be associated with a project ?

- [x] Yes
- [ ] No
- [ ] Idk

## Accounting

### 1. How many journal item with be created for a customer invoice having 2 product lines and the same 15% tax on each line?
- [ ] 2 journal items
- [ ] 3 journal items
- [x] 4 journal items
- [ ] 5 journal items
- [ ] Idk

### 2. How is the total due by a customer computed?

- [ ] The sum of the unpaid invoices from this customer
- [x] The balance related to this customer in receivable accounts
- [ ] The sum of invoices minus the sum of payments of this customer
- [ ] Idk

### 3. Will Odoo allow to create an invoice (with a tax) in a closed tax period?

- [ ] Yes
- [x] No
- [ ] Idk

## Purchase

### 1.

- [ ] 1000$
- [ ] 500$
- [x] 980$
- [ ] Idk

### 2. Can you order more quantities than what's in the purchase agreement if you're using a "Blanket Order"?

- [x] Yes
- [ ] No
- [ ] Idk

### 3. Which vendor is selected by default on a request for quotation?

- [x] The first valid supplier in the list
- [ ] The one with the smallest delivery lead time
- [ ] The one with the smallest price
- [ ] Idk

## Sales

### 1. What does this product configuration imply?

![](SalesV12-Q15(1).jpg)
![](SalesV12-Q8.jpg)

- [ ] The product will be ordered from a vendor everytime a sales or manufacturing order is validated
- [x] If a re-ordering rule is set up, the product will be ordered from a vendor when the rule is triggered
- [ ] The product will be manufactured everytime a sales or manufacturing order is validated
- [ ] Idk

### 2. What do you need to set on your product to be used in a sales order?

- [ ] Nothing, all your products can be sold
- [ ] You can only find products that are available in stock
- [x] You need to set "Can be sold" on the product
- [ ] Idk

### 3. Can I prevent a product from being sold?

- [ ] Yes


# Quiz

## Introduction

### If I don't activate my new database through the email link, how long will it stay alive?

4h

### How many apps can I install during the free trial?

Up to 10

### What can I see in the upper right corner of my main dashboard

- [ ] My scheduled activities
- [ ] Discuss
- [ ] My profile
- [x] All of the above
- [ ] None of the above

### Where can i change the language of my profile?

- [ ] General Settings
- [x] Preferences
- [ ] In my account

### Why do some fields turn red when I try to save my changes?

- [x] Because some mandatory fields have not been completed
- [ ] Because some information is not in the correct language.
- [ ] Because you do not have the rights to edit that field

### Where can I schedule an activity?

- [ ] In the chatter
- [ ] In the Kanban view
- [ ] On the user profile
- [x] n the chatter & kanban view

### Can I set a priority on an activity?

- [ ] Yes
- [x] No
- [ ] Yes, but only if the activity is linked to a project
- [ ] Yes, but only if the activity has a "next activity" configured

### What do the number and the clock in the upper right mean?

- [ ] It is the time left for you to finish your activities.
- [x] It is the number of unfinished activities you have up until today.
- [ ] It is the number of activities you will have to do in the future.
- [ ] It is the number of activities you have assigned to your colleagues.

###  Can I create a private channel with multiple users on Discuss?

- [x] Yes
- [ ] No
- [ ] Only between people from the same group

### Who can I send a direct message to?

- [x] Anyone in the company
- [ ] Anyone in your department
- [ ] Only people you are friends with.

### Can I create canned responses?

- [ ] You cannot.
- [ ] By going to Discuss -> Configuration -> Canned Responses
- [x] By going to Live Chat -> Configuration -> Canned Responses

### How can you see who's in a specific channel?

- [ ] By going to Discuss, selecting the channel, and clicking on the gear under the Members tab.
- [ ] By writing /who in the channel chat.
- [x] Both answers

### What can I set my contacts as?

- [ ] Individual
- [ ] Company
- [x] Either

### Where can I import my contacts?

- [x] In the Contacts app, by clicking on "Import".
- [ ] By going to Configuration -> Import.
- [ ] You cannot import your contacts.

### Can I specify the contact fields I want to export?
- [x] Yes
- [ ] No

## Purchase

### Is it possible to directly create a Purchase Order?

- [ ] Yes, from the Purchase Order menu.
- [x] No, it will create a request for quotation whatever you do.

### What should I do if I receive my products from the same vendor in two separate deliveries?

- [ ] Odoo does not take split deliveries into account
- [x] You should create a backorder on the first reception
- [ ] You should click on the "no backorder" button after the reception of the first delivery

### When will the warning message be triggered on my Request for Quotation?

- [ ] When you click on confirm order
- [ ] When you click on send by email
- [x] When you set a vendor or add a product

### Which feature should I use if I want an approval process on my Purchase Orders?

- [ ] The 3-way matching feature
- [x] The purchase order approval feature
- [ ] The purchase manager approval feature
- [ ] The warning feature

### Where can I configure a warning message?

- [ ] On the product form
- [ ] On the vendor form
- [ ] Directly in the internal notes of my RFQ
- [x] On the product form and on the vendor form
- [ ] All of the above
