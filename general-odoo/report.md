---
theme: metropolis
title: Odoo General and Demo

author: 'Pham Thi Ngoc Mai'
institute: 'AHT'
date: August 12th, 2018
toc: true
slide_level: 2
mainfont: 'TimesNewRoman'
header-includes: |
  \metroset{progressbar=frametitle,sectionpage=progressbar}
  \usepackage[linesnumbered, ruled]{algorithm2e}
  \usepackage{subfig}
  \usepackage{mathptmx}
  \usepackage{multicol}

# pandoc report.md -t beamer -o slide.pdf
---

# I. Introduction

## 1 - What is Odoo

> Odoo is a comprehensive open-source enterprise resource planning (ERP) software made up of an integrated suite of business modules

## 2 - Odoo Modules

- CRM
- Sales
- e-Commerce
- Accounting
- Inventory
- Manufacturing
- Employees

## 3 - Odoo ERP Implementation methodology:

1. Install basic Odoo.
2. Set up the load balancing if you need
3. Set up the database.
4. Install Odoo applications.
5. Install customized apps if any.
6. Configure the basic master like company info, user details, etc..
7. Configure user wise access levels.
8. And use.

# II. General Settings

## 1 - Users

[Settings/User](https://www.odoo.com/documentation/user[Introduction](#i-introduction)
[General Settings](#ii-general-settings)
[CRM](#iii-crm)
[Sales](#iv-sales)
[Odoo Studio](#v-odoo-studio)
[Planning](#vi-planning)
[Timesheets](#vii-timesheets)
[Approvals](#viii-approvals)
[Appointments](#ix-appointments)
[Accounting](#x-accounting)


## 2 - Companies

- Edit current company
- Manage company

![Settings/Company/New](create-company.png)

## 3 - Groups

- Groups defines rules to models within an application

![](groups.png){width=90%}
![](group-name.png){width=90%}

## 4 - Business documents:
- config layout: tagline, footer, logo, ...
- edit layout
- use custom layout

![](config-document.png){width=90%}

## 5 - Statistics

Digest email: subscribe/unsubscribe, edit, create

![](digest-email.png)

## 6 - Others

![](other.png){width=90%}

## 7 - Others

![](other1.png)



# III - CRM

## 1 - CRM settings

- Leads designates an individual who might become your customer, but currently isn't. Leads are usually converted to contacts, companies and deals (opportunities) or are 'junked'.

![](CRM-setting.png){width=90%}

## 2 - CRM workflow

- Acquire leads: by emails, website -> list of leads
- Convert leads into opportunity (manually | lead mining)
  - New
  - Qualified
  - Proposition
  - Won

## 3 - CRM Scenarios:

- Planning activity
- Generate leads/opportunities from emails/webpage
- Demo an opportunity lifecycle (+ send quotation, manage lost)

## 4 - CRM Config

- CRM Settings
- Sale team: leader, members, email...
- activity types
- pipeline: stages, tags, lost reasons (add, rm, edit),
- leads: change lead to opportunity, lead gen, lead mining, lead enrich, ... ( money)

# IV - Sales

## 1 - Sales workflow

- Create a quotation
- Send it to your customer
- Wait for confirmation
- Confirm the sales order
- Create an invoice.

## 2 - Sales Scenarios

- Create and send quotations
  - use quotation template: product, optional products, signature, paid, deadline, deliver and invoicing address, term & condition
  - deliver lead time, price

## 3 - Dropshipping

- Enable dropshipping (purchase settings, product)
- PO is automatically generated when creating quotations
- When PO is confirmed and received, SO with update the delivery info

## 3 - Dropshipping

![](sales/dropship-flow.png)


# V. Odoo Studio

## 1 - Module

> An Odoo Module can contain a number of elements, such as: business objects (models), object views, data files, web controllers, and static web data. An application is a collection of modules.

## 2 - Model

> Model usually represents a concept from the real world. Example: Odoo has models for Sales Orders, Users, Countries, etc.

## 3 - Field




\begin{columns}[T]
    \begin{column}{.5\textwidth}
     \begin{block}{}
\begin{itemize}
	\item scalar: number/text
	\item relational field: provide the option to link the data of one model with the data of another model.
\end{itemize}
    \end{block}
    \end{column}
    \begin{column}{.5\textwidth}
    \begin{block}{}
    \end{block}
    \end{column}
  \end{columns}

## 4 - View and Menu

- View: define how records are displayed
  - type view: form, list, kanban
- A Menu

# VI. Planning

## 1 - Time Shift Planning

View time shifts
![Time Shifts by Employees](week-plan.png)

## 2 - Create Time Shift

- Recurrent shift
- Plan time for task
- Save shift as template
- Duplicate plan from previous week

![](create-shift.png){width=90%}


## 3 - Publish and Send Week Plan

- Automate by set up Scheduled Action

![](my-planning.png)

# VII - Timesheets

## 1 - Timesheet Settings

![](timesheet-settings.png)

## 2 - Timesheet on a task

- Create timesheet
- Employee reminder

![](add-timesheet.png)

## 3 - Task Analysis (Project Module)

![](task-analysis.png){width=90%}

## 4 - Planning Analysis (Project Module)

![](planning-analysis.png)

## 5 - HR Analysis (Timesheets)

![](hr-analysis.png)

# VIII. Approvals

## 1 - Approval Types

![](approval-type.png)

## 2 - Create New Request

![](approval-newreq.png)

## 3 - Manage Requests

![](approve-approvla.png)

# IX. Appointments

## 1 - Create Online Appointments

- Define scheduling rules

![](create-appointment.png)

## 2 - Register An Appointment

\hspace*{-3in}
![](choose-appointments.png){width=50%}\ ![](view-appointmen.png){width=50%}

# X. Accounting

## 1 - Overview

![](accounting/flow.png)

## 1 - Overview
- Create Journal Entry
- Create Journal Item
- Follow-up payments, follow up level
![](accounting/followup03.png)
- Support internal transfer

## 1 - Customer Invoice to Payments

- Create invoice

![](accounting/create-cusinvoice.png){width=90%}

## 1 - Customer Invoice to Payments

- Create invoice (Offer cash discount)

![](accounting/cash-discount-invoice.png)

## 1 - Customer Invoice to Payments

- Create invoice (Offer cash discount)

![](accounting/payment-term.png)

## 1 - Customer Invoice to Payments

- Register a payment from a customer invoice (auto reconcile)
- Create a new payment (payment matching)

## 1 - Customer Invoice to Payments

![Customer invoice](accounting/sample-invoice.png){width=80%}

## 1 - Customer Invoice to Payments

![Customer invoice partially paid](accounting/invoice-paid-partially.png)

## 1 - Customer Invoice to Payments

- Auto-reconcile the invoice with corresponding payments

![Payment paid from invoice](accounting/payment-paid-from-invoice.png)

## 1 - Customer Invoice to Payments

- Payment that is created manually have to do Payment Matching (upper right button)

![Payment created manually](accounting/manual-payment.png)

## 1 - Customer Invoice to Payments

- Payment that is created manually have to do Payment Matching (upper right button)

![Payment Matching](accounting/payment-matching.png)

## 1 - Customer Invoice to Payments

![Reconcile Payment and Invoice](accounting/reconcile-payment-invoice.png)

## 1 - Customer Invoice to Payments

- Payment after reconciled with invoice will have link to the invoice

![Reconciled Payment](accounting/payment-after-reconcile.png)

## 1 - Customer Invoice to Payments

- Bank Journal keeps track of payment which are not linked to bank statements
- Create/Import bank satements to reconcile with the outstanding payments

![Bank Journal](accounting/bank-journal.png)

## 1 - Customer Invoice to Payments

- Bank Journal keeps track of payment which are not linked to bank statements
- Create/Import bank satements to reconcile with the outstanding payments

![Bank Journal Reconciliation Report](accounting/bank-reconciliation.png)


## 1 - Customer Invoice to Payments

![Bank Statement](accounting/bank-statement.png){width=90%}

## 1 - Customer Invoice to Payments

![Bank Journal when there are new bank statements not linked to a payment](accounting/bank-journal-to-reconcile.png)

## 1 - Customer Invoice to Payments

![Bank Journal Reconciliation Report](accounting/bank-reconciliation-when-have-bank-statement.png)

## 1 - Customer Invoice to Payments

![Reconciliation](accounting/reconcile-payment-bank-statement.png)

## 1 - Customer Invoice to Payments

![Reconciliation](accounting/reconcile-bank-stm-2.png)

## 2 - Vendor Bills to Payments

- Create/Upload Bills (different rouding methods)
- Batch Payment
  - Inbound batch type (customer batch payment)
  - Outbound batch type (vendor batch payment)

## 2 - Vendor Bills to Payments

Entries are posted when confirm the bills

![Vendor Bill](accounting/vendor-bill.png)

## 3 - Auto Reconciliation

- Reconciliation Model

![](accounting/reconcile-model.png)

## 4 - Handle Deferred Revenues

> Odoo Accounting handles deferred revenues by spreading them in multiple entries that are automatically created in draft mode and then posted periodically.

- Deferred revenue model: create Deferred Revenue entries faster.

![](accounting/deferred-model.png){width=90%}

## 4 - Handle Deferred Revenues

- Deferred revenue

![](accounting/deffered-rev.png)

## 5 - Credit Notes and Refund

![](accounting/credit-note-diagram.png)

## 5 - Credit Notes and Refund

![Credit Note](accounting/credit-note.png)

## 6 - Invoice Online Payment

![](accounting/payment-acquirers-activation.png)
![](accounting/online-payment-acquirers.png)

## 7 - Register Customer Payments by Checks

![Undeposited Fund](accounting/undeposited-funds.png)

## 7 - Register Customer Payments by Checks

![One Journal Entry](accounting/one-journal-entry.png)


## 7.1 - Undeposited Funds

![](accounting/register-payment-check.png)
![](accounting/journal-entry-check.png)
![](accounting/reconcile-check-bnkstm.png)

## 8 - Multicurrencies

- Live currency rate
- auto record exchange gain and loss

![](accounting/multicurrencies-setting.png){width=80%}
![](accounting/reconcile-multicurrencies.png){width=80%}

## 9 - Bank and Cash

- Cash register
- Synchronize PayPal
- Synchronize bank account

## 10 - Reconciliation Model

3 types:

- Write-off button
- Suggestion of counterpart values
- Match existing invoice/bills

## 10 - Reconciliation Model

![Write-off button](accounting/reconciliation_models_button.png)

## 10 - Reconciliation Model

![Suggest Counterpart Value](accounting/reconciliation_models_suggestion.png)

## 10 - Reconciliation Model

![Match existing invoices/bills](accounting/payment-matching.png)

## 10 - Reconciliation Model

![Configuration](accounting/reconciliation-model-config.png)


## 11 - Fiscality

## 11.1 - Taxes

- add/edit/active/deactive tax
- verify VAT number
- withholding tax (Retention tax group, negative value)

![](accounting/tax-def.png)

## 11.1 - Taxes

![Tax Settings](accounting/tax-config.png)

## 11.1 - Taxes

- add/edit/activate/deactivate tax

![Taxes list](accounting/tax-list.png)

## 11.1 - Taxes

- add/edit/activate/deactivate tax

![Taxes Configuration](accounting/tax-edit.png)

## 11.1 - Taxes

- add/edit/activate/deactivate tax

![Taxe Configuration](accounting/tax-edit2.png)

|                  |                                          |
| ---------------- | ---------------------------------------- |
| Tax Name         | Back end                                 |
| Label on Invoice | Taxes column on exported invoice         |
| Tax Group        | Above the Total line on exported invoice |
| Tax Grid         | Help generate Tax Report automatically   |

## 11.1 - Taxes

> Taxes and reports are usually already pre-configured: a Fiscal Localization Package is installed according to the country you select at the creation of your database.

## 11.1 - Taxes

> withholding tax is a government requirement for the payer of a customer invoice to withhold or deduct tax from the payment, and pay that tax to the government.

![Retention Tax Config](accounting/retention04.png)

## 11.1 - Taxes

![Retention Tax Config](accounting/retention02.png)

## 11.1 - Taxes

![Retention Tax in Invoice](accounting/retention03.png)

## 11.2 - Fiscal Position

> If a customer has a specific fiscal position, the default tax may be replaced by another

> Fiscal Positions allow you to create sets of rules to automatically adapt the taxes and the accounts used for a transaction.

## 11.2 - Fiscal Position

Can be applied in various ways:

- automatically applied, based on some rules

![Fiscal Position automatically applied for customers and vendors in Europe](accounting/tax-acc-mapping.png)

## 11.2 - Fiscal Position

- automatically applied, based on some rules
- manually applied on a transaction

![Choose Fiscal Position manually on Sale Orders, Invoices, Bills](accounting/fiscal-positions-transaction.png)

## 11.2 - Fiscal Position

- automatically applied, based on some rules
- manually applied on a transaction
- assigned to a partner, on its contact form

![](accounting/fiscal-positions-transaction.png)

## 11.2 - Fiscal Position

> TaxCloud calculates sales tax in real-time for every state, city, and special jurisdiction in the United States.

![Settings](accounting/taxcloud02.png)


## 11.3 - Tax Inlcude/Exclude

> Handle the very specific use case where you need to handle the two prices (tax excluded and included) on the product form within the same company.

## 11.3 - Tax Include/Exclude

- choose only one and stick to it: price without taxes or price with taxes included
- define which default tax related to the product
- let Odoo compute the other one automatically, based on the pricelist and fiscal position
- negotiate your contracts with customers accordingly

## 11.3 - Tax Include/Exclude

1. always store the default price TAX EXCLUDED on the product form, and apply a tax (price included on the product form)
2. create a pricelist with prices in TAX INCLUDED, for specific customers
3. create a fiscal position that switches the tax excluded to a tax included
4. assign both the pricelist and the fiscal position to customers who want to benefit to this pricelist and fiscal position

## 11.3 - Tax Include/Exclude

- your product default sale price is 8.26€ tax excluded
- but we want to sell it at 10€, tax included, in our shops or eCommerce website

## 11.3 - Tax Include/Exclude

![Config default tax exclude](accounting/price_B2C_B2B01.png)

## 11.3 - Tax Include/Exclude

![Create B2C pricelist](accounting/price_B2C_B2B02.png)

- activate pricelist in Sale Settings

## 11.3 - Tax Include/Exclude

Create B2C Fiscal Position

![B2C Fiscal Position](accounting/price_B2C_B2B03.png)

## 11.3 - Tax Include/Exclude

![B2B Quotation](accounting/price_B2C_B2B04.png)

## 11.3 - Tax Include/Exclude

![B2C Quotation](accounting/price_B2C_B2B05.png)

## 11.4 - Cash Basis Tax

![](accounting/cash-basis-setting.png)

## 11.4 - Cash Basis Tax

![](accounting/cash-basis-tax.png)

## 11.4 - Cash Basis Tax

![After validate invoice](accounting/when-validate-invoice.png)

## 11.4 - Cash Basis Tax

![Receive the payment](accounting/when-receive-payment.png)

## 11.4 - Cash Basis Tax

![Reconcile payment and invoice](accounting/after-reconcile-payment-invoice.png)

## 12 - Reports

- Customize Reports
- Convert pivot view to spreadsheet and access from Documents module
- export report to xlsx

![](accounting/reports-list.png){width=30%}


## 13 - Analytic Accounting

![](accounting/analytic-acc.png)
![](accounting/analytic-rpt.png)

## 13 - Analytic Accounting

![](accounting/analytic-tag.png)

- auto create an analytic account when creating a project

## 14 - Inventory Valuation

Costing methods:
- Standard Price
- Average Price
- FIFO
- LIFO

## 14 - Inventory Valuation

Costing methods:
![Standard Price](accounting/inventory-standard-price.png)

## 14 - Inventory Valuation

Costing methods:
![Average Price](accounting/inventory-average-price.png)

## 14 - Inventory Valuation

Costing methods:
![FIFO](accounting/inventory-fifo.png)

## 14 - Inventory Valuation

Costing methods:
![LIFO](accounting/inventory-lifo.png)

## 14 - Inventory Valuation

2 types:
- Periodic Inventory Evaluation
- Perpetual Inventory Evaluation

## 14 - Inventory Valuation

Periodic Inventory Evaluation:
> At the end of the month or year, the accountant post one journal entry representing the value of the physical inventory.
> At the end of the month/year, the company do a physical inventory (or just rely on the inventory in Odoo). They multiply the quantity of each product by its cost to know the inventory value of the company.

## 14 - Inventory Valuation

Perpetual Inventory Evaluation:
>goods reception and outgoing shipments are directly posted in the accounting. The inventory valuation is always up-to-date.



## 14 - Inventory Valuation

![](accounting/balance-sheet-asset.png)

## 15 - Asset Management

![](accounting/asset.png)

# XI. HR

## 1. Recruitment

![](hr/recruitment.png)

## 1. Recruitment

![](hr/contract-template.png)

## 2. Referral Recruitment

- referral links has tracker
- config:
  - levels
  - rewards
  - alert
  - onboarding

![](hr/referral-recruitment-dashboard.png)

## 2. Referral Recruitment

![](hr/alert.png)

## 3. Employee

![](hr/employee-info.png)

- Company working hour

## 4. Attendance

- Employee PIN/badge (kiosk mode)
- Time off application:
  - Time off type
  - Allocate day off for each type
  - Request a Time Off
  - Report

![](hr/time-off-workflow.png)

## 4. Attendance

![](hr/sick-time-off.png)

## 4. Attendance

![](hr/time-off-req.png)

## 4. Attendance

- An employee's leave can only be approved by a user in the HR Officer group (or higher)

![](hr/all-time-off.png)

## 5. Appraisal

- Request(from employee)/Create

![](hr/appraisal-settings.png)

## 5. Appraisal

- Request(from employee)/Create

![](hr/appraisal-req.png){width=90%}

## 5. Appraisal

- Goals

![](hr/goal.png)

## 6. Manage Skills and Resumes

- Skills Management (employee)

![](hr/resume-employee.png)

## 7. Expenses

![](hr/expense-flow.png)

## 7. Expenses


- Expense Products

![](hr/expense-product.png){width=80%}

## 7. Expenses

- Expense Report

![](hr/expense-report.png)

## 7. Expenses

- Auto create entry and reconcile

![](hr/expenses-entry.png)

## 8. Payroll

- Contract contains information about salary structure type, pay structures

![](hr/payslip-flow.png)

## 8. Payroll

- Payroll generate payslip depends on employee's contracts

![Employee Contract](hr/contract-template.png)

## 8. Payroll

![Salary Structure Type](hr/salary-structure-type.png)


## 8. Payroll

![Pay Structure](hr/regular-pay.png)

## 8. Payroll

![Salary Rule](hr/salary-rule.png)

## 8. Payroll

![Work Entry Types](hr/work-entry-type.png)

## 9. Payroll

- Resolve conflicts before generating payslips

![Work Entry](hr/work-entries.png)

## 9. Payroll

![Payslip](hr/payslip.png)

## 9. Payroll

![Generate entries from payslips](hr/payslip-journal-entries.png)

## 9. Payroll

Other features:
- report the expenses in payslip to reimburse employee directly in payslip
- structure types: definding payroll localization
- payroll structure: rule to compute the payslip
- structure + computation rules = salary rules

## 10. Fleet Management

![Manage vehicles](hr/vehicles.png)

## 10. Fleet Management

![Vehicles Contract](accounting/vehicle-contract.png)

## 10. Fleet Management

![Vehicle Service](hr/vehicle-service.png)






##
\centering
Thank you for listening!



## Refs

- [Odoo doc vietsub](https://bizapps.vn/page/huong-dan)
- [Odoo Book from OpenERP](https://doc.odoo.com/book)

## Contacts

![](hr/contacts.png)

<!-- drop ship
check invoice luu trong contact
approval thông qua nhiều người
mindmap
phần nào customize được -->


<!-- công cụ, bước pt module, ngôn ngữ,

lưu ý cần để pt trên odoo:
bước nào
deploy ntn, dùng gì,
deploy khác gì trên production và dev
unit test -->
