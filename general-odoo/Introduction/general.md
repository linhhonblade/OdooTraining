# General Settings

## Multi-company

- Data such as Products, Contacts, and Equipment can be shared or set to be shown for a specific company only.
  - A blank field: the record is shared within all companies.
  - Adding a company: the record is visible to users logged in to that specific company.

- If a user has multiple companies activated on his database, and he is editing a record, the editing happens on the record’s related company.
  - Example: if editing a sale order issued under JS Store US while working on the JS Store Belgium environment, the changes are applied under JS Store US (the company from which the sale order was issued).

- When creating a record, the company taken into account is:
  - The current company (the one active) or,
  - No company is set (on products and contacts’ forms for example) or,
  - The company set is the one linked to the document (the same as if a record is being edited).

- Inter-company Transactions
  - **Synchronize invoice/bills**: an invoice posted on JS Store Belgium, for JS Store US, automatically creates a vendor bill on the JS Store US, from the JS Store Belgium.
  - **Synchronize sales/purchase order**: when a sale order for JS Store US is confirmed on JS Store Belgium, a purchase order on JS Store Belgium is automatically created (and confirmed if the Automatic Validation feature was enabled).

## Discussion

## Gamifications
- Badges are granted when a challenge is finished. This is either at the end of a running period (eg: end of the month for a monthly challenge), at the end date of a challenge (if no periodicity is set), or when the challenge is manually closed.

## IAP
- To be notified when it’s time to recharge my credits, I’ll go to my IAP Portal through Settings app ‣ Odoo IAP ‣ View my Services, unfold a service and mark the Receive threshold warning option.
- Different services are available depending on the hosting type of your Database:
  - Odoo Online (SAAS): only the IAP services provided by Odoo can be used (i.e. the SMS, Snailmail, Reveal and Partner Autocomplete features);
  - Odoo.sh and Odoo Enterprise (on-premise): both the services provided by Odoo and by third-party apps can be used.

## CRM
- The team & leads assignation will assign the unassigned leads once a day.
- If you track a webpage, the pages that your partner visited will be seen under the chatter of the contact form or the button
- The feature will not repeat multiple viewings of the same pages in the chatter.
- Lead Enrichment:
  - If you run out of credits, the only information that will be populated when clicking on the suggested company will be the website link and the logo.
  - If you are on Odoo Online (SAAS) and you have the Enterprise version, you benefit from free trial credits to test the feature.

## Portal Access:
- A portal access is given to a user who has the necessity to have access to Odoo instance, to view certain documents or information in the system.

- For Example, a long term client who needs to view online quotations.

- A portal user has only read/view access. He or she will not be able to edit any document in the system.

## Subscriptions

- The To renew tag is automatically ticked when a payment fails.
- Types of reports:
  - Monthly Recurring Revenue (MRR): monthly revenue earned with subscription-based products or services.
  - Annual Run rate (ANN): estimate the coming year’s performance. However, this estimation does not take variations and growth into account.
![Different between MRR and ARR](../img/01_general/difference-between-MRR-and-ARR.png)
  - Non-Recurring Revenue (NRR): revenue earned for everything else than subscription-based products or services.
  - Customer Retention: Practices to engage existing customers to continue buying products or services from your business.
  - Churn Rate:
    - Logo Churn: subscription cancellation rate.
    - Revenue Churn: monthly recurring revenue loss rate.
  - Customer Lifetime Value (CLV): Indicates how much revenue can be expected for a customer during his/her entire contract.

- Reports:
  - Subscription Analysis Report
    - By default, Odoo uses the Monthly Recurring Revenue. (in Report)
  - Retention Analysis Report
  - Revenue KPIs Report
  - Sales

# Dates

## Sales

- **sale.order**
  - date_order: default today, Order Date/Quotation Date, creation date of draft/sent orders, confirmation date of confirmed orders
  - create_date: Creation Date, Date on which sales order is created
  - validity_date: Expiration, default validity date get from param self.env.company.quotation_validity_days (enable sale.use_quotation_validity_days in settings of sales)
  - signed_on: date of the signature
  - commitment_date: Delivery Date, This is the delivery date promised to the customer. If set, the delivery order with be scheduled based on this date rather than product lead times. If the commitment_date is sooner than the expected date, there is a warning: Requested date is too soon, you maybe unable to honor the delivery.
  - expected_date: delivery date you can promise to the customer, computed from the minimum lead time of the order lines, = min (line._expected_date() for line in sale.order.lines)
  - Trong SO, expected_date ko được store nhưng khi expected date thay đổi thì update giá trị của expected date vào commitment date

- **sale.order.line**
  - _expected_date(): = order_date + customer_lead
  - customer_lead: Customer Lead Time, number of days between the order confirmation and the shipping of the products to the customer

- **stock.picking**
  - scheduled_date: default now, Scheduled Date, Scheduled date for the first part of the shipment to be processed. Setting manually a value here would set it as expected date for all the stock moves. Cannot change on a done or cancelled transfer (Nếu ko set bất kỳ security lead time thì default = expected_date của SO)
  - date_deadline: Deadline, Date promise to the customer on the top level document (SO, PO), nếu có purchase security lead time thì date_deadline += purhcase security lead time
  - date: Creation Date, usually the time of the order, default sale.order.date_order
  - date_done: Date of Transfer, date at which the transfer has been processed or cancelled.

- **stock.move**
  - create_date: Creation Date
  - date: Date Scheduled, Scheduled date until move is done, then the date of actual move processing
  - date_deadline: Date promised to the customer on the top level document (SO/PO)

- **purchase.order**
  - date_order: Order Deadline, default now, Depict the date within which the Quotation should be confirmed and converted into a purchase order
  - date_approve: Confirmation Date
  - date_planned: Receipt Date, Delivery date promised by vendor. This date is used to determine expected arrival of products, default = min (date_planned of purchase.order.line)

- **purchase.order.line**
  - date_planned: Delivery Date, Delivery date expected from vendor. This date respectively defaults to vendor pricelist lead time then today's date (today + vendor lead time)

## Times

- Customer Lead Time: expected_date = order_date + min(customer lead time of products)
- Security Lead Time for Purchase: Margin of error for vendor lead times. When the system generates Purchase Orders for reordering products, they will be scheduled that many days earlier to cope with unexpected vendor delay.
- Security Lead Time for Sales: Margin of error for dates promised to customers. Products will be scheduled for delivery that many days earlier than the actual promised date, to cope with unexpected delays in the supply chain

expected delivery date = order date + customer lead time (min)

scheduled delivery date =


# Stock

- stock.picking:
  - move_line_ids: stock.move.line
  - move_lines: stock.move


- Sale Order:
  - expected_date = order date + customer lead time

- Delivery Order:
  - scheduled_date = expected date (on SO) - sales security lead time
  -


| Time                             | Where to set                              | Description                                                                                                                                                                                                                                     |
| -------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer Lead Time               | Product > Inventory tab                   | The time needed for your product to go from your warehouse to the customer place.                                                                                                                                                               |
| Security Lead Time for Sales     | Inventory Settings                        | Margin of error for dates promised to customers. Products will be scheduled for delivery that many days earlier than the actual promised date, to cope with unexpected delays in the supply chain                                               |
| Security Lead Time for Purchase  | Inventory Settings                        | Margin of error for vendor lead times. When the system generates Purchase Orders for reordering products, they will be scheduled that many days earlier to cope with unexpected vendor delay.                                                   |
| Vendor Lead Time                 | Product > Purchase tab > Vendor Pricelist | Time needed for a product you purchased to be delivered.                                                                                                                                                                                        |
| Manufacturing Security Lead Time | Manufacturing Settings                    | additional time to mitigate the risk of a manufacturing delay. In case of a Replenish to Order, the Delivery Order scheduled date - Manufacturing Lead Time - Manufacturing Security Lead Time is the default Manufacturing Order planned date. |
| Manufacturing Lead Time          |                                           | this is the expected time it takes to manufacture a product. This lead time is independent of the quantity to produce and does not take the routing time into account.                                                                          |
| Days to Purchase                 |                                           | number of days the purchasing department takes to validate a PO. If another RFQ to the same vendor is already opened, Odoo adds the line to the RFQ instead of creating a new one. Then, the specific date is set on the line.                  |
