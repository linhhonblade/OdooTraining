# Website

- change picture quality (make website loadfaster)

![](website_13_14.png)
![](img_srch_13_14.png)

web page load faster 3.42 times

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

- New appearance for forecasted report
![](fore_cast_13_14.png)
![inventory](inventory1.png)
![](inventroy2.png)

- Easier to manage replenishment with Replenishment action
![](replenishment_graph_14.png)


![](Screenshot%20from%202021-01-28%2016-36-00.png)
![](Screenshot%20from%202021-01-28%2016-41-50.png)

  - If your product is not available (because all the on-hand products are reserved), change the priority of the delivery order -> your product is reserved
  - Forecasted = On hand - confirmed orders (after sum of lead time vendor lead time + purchase security lead time + days to purchase)
  - Forecasted + Pending = onhand - confirmed orders + incoming products - unconfirm orders (quotations)

# Barcode

![](barcode_13_14.png)
![](batch_transfer_barcode.png)

- Wave Picking (set routes for product/product categories) and Batch Picking (Batch Transfer) (13 + 14)
![](batch_picking_14.png)
![](batch_picking_14_2.png)

- New Picking Strategies: Cluster Picking
![](cluster_picking_14.png)

# Timesheet

- Shortcut for switching project and log work
![](timesheet_13_14.png)

- use hot key to add 15m to a specific project
![](timesheet_hotkey_14.png)

# Expenses

- record expenses by snapping a picture (Odoo App)
- more in Accounting

# Manufacturing

- Create MO without BoM (you define work orders directly in MO form)

![](MO1.png)
![](MO2.png)

- Change priority to get components reserved
![](MO_not_avail_component_14.png)
![](MO_forecasted_rpt_14.png)
![](MO_change_prio_14.png)
![](MO_forecasted_rpt_af_prio_change_14.png)

- Create Operation: Work Center is mandatory
- Miscellaneous:

# Purchase

- Better list view

![](purchase1.png)
![](purchase2.png)

- show on-time delivery rate of vendor on RFQ

![](purchase3.png)

- Ask confirmation checkbox: send and email to the vendor to make sure they can confirm delivery on the date specified in purchase order.
- When the vendor receive email, they can confirm or update the delivery date (line by line) on the purchase order

![](purchase4.png)
![](purchase5.png)

# Business Intelligence Reporting Engine

- It works on the all applications of any module
- With the new javascript framework of odoo, building report is 40 times faster then v13

![](business_intelligence.png)
![](business_intelligence2.png)
![](business_intelligence3.png)




# Data Cleaning

- Help you clean the data automatically (so that reporting is more efficient)
- Merge duplicate contact (choose the priority when merging) (can do the same for any models)
- Configure the rule for deduplication
  - manually: you configure the rule, system recommend you, you decide to merge or not
  - automatically: system do all (with a threshold) based on your rule

# CRM

- Opp with recurring revenue (view report with MRR)

# Microsoft Integration

- add contact to Odoo from Outlook
- sync calendar with Microsoft calendar

# Appraisal

- quick schedule appraisal and ask for feedback
- create survey for feedback template

# Survey

- get attendee answers in real-time

# Accounting

## Vendor bills

![Bills List View Odoo 13](bill_list_13.png)
![Bills List View Odoo 14](bill_list_14.png)

## Expense

- AI digital analyze can update the product, price, date and even the acounting information for the receipt
- Behind the scene, we categorize all expenses in diff categories (food, restaurants, parking, travel..). User can link category to the products. You can link the expense acount to the product
- New Disallowed Expenses Report: Disallowed expenses are those expenses that cannot be deducted in the fiscal result but can be deducted in your bookkeeping result

![Disallowed Expense Categories](disallowed_categ_14.png)
![Setup Disallowed Expenses for an account](COA_disallow_14.png)
![Disallowed Expenses Report: you will see all the disallowed expenses categories with all the expenses accounts linked to it](disallowed_report_14.png)
![](general_ledger_disallowed_14.png)
## Reporting

- Odoo Spreadsheet
- Not only in Accounting but everywhere else

## Currency

- New Report when enabling Multi-currencies: Unrealized currency gains/losses
![](currency_rpt_14.png)

- Post the entry for adjustment of currency gain/loss automatically (or manually) - other info tab
- Adjustment entry will be automatically posted at the correct accounting date
![](adj_entry_currency_14.png)
![](currencty_entry_14.png)
![](currency_rpt_with%20adj_entry_14.png)

## Taxes

- Larger range of tax return possibilities
![](tax_return_period_14.png)

## Payment Refractoring

- The balance sheet will be updated at every moment and synchronized with bank statement
  - Every Bank Journal will have specific Suspense Account: the moment you synchronize bank statements / import bank transactions, they re immediately posted
  - the bank account then will be updated in BL sheet

![Suspense Account for Bank Journal](bank_account_14_1.png)

- Add transfer accounts and track payments

![Outstanding Receipts in Bank Journal](bank_account_14_2.png)

- Any payment register (for invoice or bills) will be automatically posted to transfer accounts
![auto reconciled to the transfer account](bl_sheet_14.png)

- The journal entries for bank statement is automatically posted with the counterpart is the suspense account

![Bank Statement](bank_stmt_14.png)
![Journal Entries (automatically posted)](posted_journal_entries_14.png)
![Journal Entry with counterpart Suspense Account](bnk1_14.png)

- After reconciliation of the bank statement, the right account will be updated in the journal entries

![Bank statement after being reconciled](bank_stmt_reconciled_14.png)
![The updated journal entry after reconciliation of bank statement](entry_updated_af_reconcile.png)

## Implement Accounting

- Invoicing, Inventory, eCommerce,... are integrated with Accounting (event when u r not installing it on your server). They also create accounting entries
- But when you want to start with the official Accounting application, you just want to import the opening balance
- If u dont do anything, the opening balance tgt with all accounting transactions will make double entries.
- Now, Odoo will take care of all those prev entries. Just set the date of the go-live of Odoo Accounting, Odoo will archived all neccessary entries
- All invoices still there but in a new stage: invoicing app legacy (only the accounting entries behind are archived)
- I would like to start Accounting on the 1st Oct, and a fresh start

![](switch_threshold.png)

- All Invoices and Bills before the date will be cancelled

![](cancelled_inv.png)

- Report refreshed

![](balance_sheet.png)

## Misc

- New Auditor role (Read-only access right)
- Preview accounting entries b4 posting them
-

# Documents

- Already have some spreadsheet templates for you, can create your own template

![](document1.png)

- One template can use several pivot tables so you can bring different pivot tables in the same report
- The template is dynamic (can filter, add fomular, data updated when you change a field)

- AI & Documents management
  - 95.88% recognition rate &rarr; less time on manually input work
  - Capture: subtotal, currency, dates (due, invoice), tax amount, invoice ref, bank account, supplier (find in database for the name, address, website, create right on the fly if not exist)
  - Not only bill, but also expense (scan receipts)
  - send bill directly to Accounting

- manage documents for each workspace (can create as many workspace as you want): Finance, HR, Internal,..
- workspace can be hierarchy
- easy to send a file to Documents App by using email alias

![Documents App Odoo 14](action_document_14.png)

- split document easily
- The AI take responsible for providing the correct expense account for vendor bill (by remember the combination of the label, supplier)
![Split Documents](split_document_14.png)

## Document Settings

![](document_settings_13_14.png)
-> When u send&print an invoice or any document, the file will be sent to Documents too (to the workspace u set in settings)
- To access Actions in Documents, activate dev mode


# HR and Payroll


# Events

- for ticket option in settings (Sell tickets with sales order): need ecommerce
![](event_setting_13.png)
![](event_setting_14.png)
![](events_13.png)
![](events_14.png)

- Event field is mandatory in Track form
- Other information about speaker (email, phone, bio) will be populated after choosing the speaker (speaker field is not mandatory)
- When save a track, it is in proposal stage
- Track proposal on website (allow website visitor) register for a talk proposal for an event

- The email template will update the time until your event based on the day you open the remind email

## Point of Sales

- Available on POS is checked by default if u create product inside POS app, but wont if in others

- Cash control: in Odoo14, set openning balance whenever u start new session (not at the shop setting anymore like Odoo13)
![](cash_control_13.png)
![](cash_control_14.png)
### Settings

- Is a Bar/Restaurant
- Authorized Employees: Use employee credentials to log in to the PoS session and switch cashier
- Manage Orders: Reprint receipt, refund and exchange orders
- Product Configurator: Select product attributes
- Restrict Product Categories: Pick which product categories are available
- Large Scrollbars: Improve navigation for imprecise industrial touchscreens
- IoT Box: Connect devices using an IoT Box
- Direct Devices: Connect devices to your PoS directly without an IoT Box
- Global Discount: Allow global discounts on orders
- Manual Discount: Allow discount per line
- Price Control: Restrict price modification to managers
- Payment Methods: Payment methods are available
- Advanced Cash Control: Control cash box at opening and closing (w authorized difference maximum)
- Header & Footer: Add a custom message to header and footer
- Automatic Receipt Printing: Print receipts automatically once the payment is registered
- Invoicing: Print invoices on customer request
- Operation Type: Operation type used to record product pickings
Products will be taken from the default source location of this operation type
- Journal Entries: Configuration for journal entries of PoS orders
- Sales Team: Sales are reported to the following sales team
