# Basics

- auto create journal entries for each of accounting transactions: customer invoices, POS order, expenses, inventory move, etc
- report income / expense at the time transactions occur (i.e., accrual basis), or when payment is made or received (i.e., cash basis)
- Users can access several companies but always work in one company at a time.
- Every transaction is recorded in the default currency of the company
- Odoo stores both the value in the currency of the company and the value in the currency of the transaction. Odoo can generate currencies gains and losses after the reconciliation of the journal items.
- Odoo also have modules to comply with IFRS rules.
- By default, Odoo uses a single account for all account receivable entries and one for all accounts payable entries.
- Odoo also remembers how you’ve treated other bank statement lines and provides suggested general ledger transactions
- Odoo’s report engine allows you to customize your own report based on your own formulae.
- Calculate the tax you owe your tax authority by Tax Report
- support both periodic (manual) and perpetual (automated) inventory valuations
- calculates your current year earnings in real time so no year-end journal or rollover is required. This is calculated by reporting the profit and loss balance to your balance sheet report automatically.
- costing method:
  - standard price
  - average price
  - lifo
  - fifo (not accepted by IFRS)
- Every financial document of the company (e.g. an invoice, a bank statement, a pay slip, a capital increase contract) is recorded as a journal entry, impacting several accounts
- Reconciliation is performed automatically by the system when:
  - the payment is registered directly on the invoice
  - the links between the payments and the invoices are detected at the bank matching process
- Check handling
  - Two journal entries and a reconciliation
  - One journal entry and a bank reconciliation

# Settings

- Odoo Accounting automatically installs the appropriate Fiscal Localization Package for your company, according to the country selected at the creation of the database.
- Accounting onboarding banner:
  - Company Data
  - Bank Account
  - Accounting Periods
  - Chart of Accounts
- You can add as many bank accounts as needed
- you can add accounts to your Chart of Accounts and indicate their initial opening balances
- To access all the settings of an account, click on the double arrow button at the end of the line.
- Invoicing onboarding banner:
  - Company Data
  - Invoice Layout (Settings ‣ General Settings, under the Business Documents section)
  - Payment Method
  - Invoice Sample
- Add your bank account number and a link to your General Terms & Condition in the footer. This way, your contacts can find the full content of your GT&C online without having to print them on the invoices you issue.
- Configuring a Payment Acquirer with this tool also activates the Invoice Online Payment option automatically. With this, users can directly pay online, from their Customer Portal.

# Chart of Account

- The country you select at the creation of your database (or additional company on your database) determines which Fiscal Localization Package is installed by default.
- It is not possible to modify the Fiscal Localization of a company once a Journal Entry has been posted.
- Some accounts, such as accounts made to record the transactions of a payment method, can be used for the reconciliation of journal entries.
- It is not possible to delete an account once a transaction has been recorded on it. You can make them unusable by using the Deprecated feature.

# Customer Invoice

- When you have validated an invoice, Odoo gives it a unique number from a defined, and modifiable, sequence.
- Accounting entries corresponding to this invoice are automatically generated when you validate the invoice.
- an invoice is considered to be paid when the associated accounting entry has been reconciled with the payment entries
- can manually enter your bank statements
- or from several other predefined formats according to your accounting localisation.

## Payment Follow up

- the due amount display on the button `Due` on Contact template. If u click, it redirect u to send remind email. click on the dot on the left of Contact name to specify: good/normal/bad debtor
- Enable Follow up level in setting and manage the level there
- If you want to send reminder before the overdue date, set negatvie days value
- In Follow up reports, it diplays total due and overdue amount for each customer, can choose some customer and click process follow up (in action gear)
- A pdf generated containig the overdue invoice
- The action (send, print follow up email, schedule activity) then created in chatter

## Reconciliation

- Can get information of payment from invoice by clicking on little `i` button beside paid line
- The Invoice number should be used in payment communication
- reconcile payment and invoice in payment matching
- a payment is validated when it is reconciled with the invoice
- can annotate the payment in reconciliation report
- recording payments and recording it later with bank statements, it's useful when your statement aren't updated often for example you register payment with cheques and you still want to keep your entries reconciled on a regular basis
- It's not necessary to record payment first on odoo as you can choose to reconcile your journal entries directly with your bank statements If your bank statement is continuously updated (you link the bank with odoo)
- Bank reconciliation lines are not blue because you havent had a payment register, but you can continue to reconcile the bank statement with the invoice (journal entry)
- In Bank Account Template: choose Post at bank reconciliation = odoo post the entries in the journal only after the bank statement has been reconciled (extra layer of security)

# Vendor Bills Batch Payments

- Enable Checks in settings to Print checks to pay your vendor

# Batch Deposit Check

- Enable Batch Payment in settings

# Vendor Bills and Rounding method

- The tax computing from vendor bill we received may differ from the bill that odoo calculate
- can modify the tax line in the bill
- can add attachment (the real bill we received) to the bill in odoo
- To mark a contact as a vendor, go to contact template, sales & purchase tab, check `Is a vendor`
- If we upload a bill generated by another odoo database, it will read the xml file which is inside the pdf file and allow our databsae to fill all the fields

# Multi-currencies

- Remember to activate other currency (remember to remove the filter for active currencies)
- can activate automatic currency date also

# Reports and Financial Statements

- can compare to prev periods
- can choose btw cash basis or accrual basis
- can choose journal to view in cash flow statement
- aged receivable: how much customer still owe us and how old the debts are
- partner leder: combine bot receivable and payable account

# Analytic Accounts

- Analytic Items is like Journal Items but in Analytic Account
- To see the balance for the groups of analytical acocunts by checking the option Hierarchy and subtotal
- Can create profit and loss report for all entries linked to an analytic account by specifying the account in Analytic option
- When you create a project, odoo automatically create an analytic account for the project

# Closing fiscal period

- Checklists
  - All Invoices, Bills, Expenses are recorded and validated
  - Reconcile everything
  - Balance in Clearing and Suspense Accounts is zero
    - Clearing Account: allow us to record a transaction and hold it for later posting once we are sure which account it goes
    - Suspense Account: used when there is a problem or uncertainty and we still want to record the amount (e.g: customer sends an amount of money but we still have to investigate to be sure we apply it to the correct invoice)
- Deprecation
- Deferred Revenue
- Accrued and Expenses

- Advisor in Accounting is the only one who can manage the COA, Reconciliation, Tax Adjustment
- Set a lock date: the last date of the financial year we are closing
- Remember checking the date (As of End of Last Fiscal Year) in the reports
- Unallocated Earning should be zero
- Undistributed Profits/Losses Account: automatically created by Odoo to put Unallocated Year Earning, Only one condition is Type = Current Year Earnings
- There is lock date for non-adviser and advisor

# Inventory valuation

- Standard price: cost defined in the product from
- Average Cost: cost recomputed everytime there is quantity changes
- If chose Evaluation: Automated we have to specify Input Account, Output Account and Valuation Account
- Cannot modify the cost of product if we the average cost is applied
- Can view Stock Valuation Account in Balance Sheet

# Depreciation

- Computation method
  - Linear: Divide equally by the planned entry
  - Degressive: multiply the last residual value by a factor (the last residual value is used for the last depreciation entry)
  - Accelerated Degressive: like Degressive, but if the calculated value smaller than value computed according to linear method, use value of linear method
- Activate Asset Management
- Create Assets Model, required fields:
  - Fixed Asset Account: Create and validate and Choose the this Asset Model
  - Depreciation Account: Donot create asset
  - Expenses Account: type depreciation
  - Journal
  - Number of Depreciation

- Asset button appear on the bill
- Can modify depreciation: provide reason,

# Deferred Revenue

- Activate in settngs
- Create Deferred Revenue Model
- Mandatory Fields:
  - Revenue Account
  - Deferred Account: Create and validate and choose the Model
  - Journal
  - Number of Recognitions
- Product should be set with income account as the deferred account
- Product can be Consumable, Service, Storable

