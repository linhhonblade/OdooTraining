# Basics

- company data (from company template) will be added to business document
- add payment acquirer in configuration
- when invoice is validated, customer now has action to pay, (in preview mode)
- Depend on setting, you may cannot invoice the order because you havent deliver the products
- Some long T&C can be print on the back of the invoice or as a link to website (add in business template in setting)
- Payment Term:
  - Balance line is the last line in the list
  - Can add term and condition at the end of invoice template

# Online Invoice Payment

- For all payment acquirer, you get credential from the payment acquirer site
- Set up thanks / pending message
- can save card infor or let customer save or not
- Payment Flow:
  - Payment from Odoo
  - Redirection to the acquirer website

# Use of QR code for customers in Europe

- Activate SEPA QR Code (settings)
- Select use SEPA QR Code (in payment acquirer config): auto generate qr code if customer choose that payment method

# SEPA Direct Debit (SDD)

- enable in setting and add creditor identifier
- on the contact of customer, invoicing tab, have bank account set up
- Debtor account is that bank account in the contact
- Journal (required) (set up bank account too)
- once we validate the mandate, it moves from draft to active
- if close the mandate: all the invoices can still be paid with the mandate
- if invoke: cannot
- invoice will go from draft to paid directly (if mandate is active)

# Tax

- Define default tax in settings
  - If select included in price -> auto select affect base of subsequent tax
  - can change default tax in product template
  - tax description appears in other info tab of the invoice
# Fiscal Position

- Config country group in Contact app
- Specific country to apply fiscal position: the country field below country group
- add customer first in the invoice so that fiscal positon display properly (add product first, then fiscal position not display)

# Notes

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
