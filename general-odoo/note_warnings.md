# Notes and Warnings

## The benefits of upgrading Odoo
- Improved performance, stability, and ease of use
- Save employee's time
- Cross Apps Integration
- Smart Warnings
- ORM Improvements: better performance and smoother development

## Sales
- On each quotation template, you can also specify discounts if the option is activated in the Sales settings.
- Templates facilitate the confirmation process by allowing customers to sign electronically or to pay online. You can activate these two options directly in the quotation template itself.
- Every quotation will now have this setting. Of course you can always change it and make it specific for each quotation.
- Be careful that delivery orders are only generated for storable products and if the Inventory app is already installed.
- If you select a customer with defined invoice and delivery addresses, Odoo will automatically use them to fill in the fields. Now, if you want to change it instantly, it is possible to do so directly from the quotation or the sales order.
- Default Terms and Conditions: Please note that this feature is activated via the settings of the Invoicing App and not via the settings of the Sales App. Moreover, you don’t need to install the invoicing application since it is done automatically with the installation of the sales application.
- Create and edit email templates to set a default attachment for all quotation emails that you will send in the future.
- To customize your email templates, activate the developer mode and go to Settings ‣ Technical ‣ Email ‣ Templates.
- If you decide to choose the Invoice what is delivered rule, you will not be able to activate the feature called Automatic invoice, which automatically generates invoices when the online payment is confirmed.
- Once the quotation is confirmed and that the status went from Quotation sent to Sales order, you are able to see your delivered and invoiced quantities directly from your sales order (it is true for both rules)
- When you request your first down payment, a new product called Down payment will be created. This product will be registered as a service product with an invoicing policy of ordered quantities. As a reminder, you can edit this product and modify it at any time. Please note that if you choose delivered quantities as invoicing policy, you will not be able to create an invoice.
- Be careful that if you do a down payment with a product using delivered quantities as invoicing policy, you won’t be able to deduct all the down payments when it comes to invoicing your customer. Indeed, you have to deliver a product before creating the final invoice. If nothing has been delivered, you create a credit note that cancels the draft invoice created after the down payment. To do so, you have to install the Inventory App to confirm the delivery. Otherwise, you can enter the delivered quantity manually on the sales order.
- A pro-forma invoice is an abridged or estimated invoice in advance of a delivery of goods.
- You should also activate the analytic accounts feature to link expenses to the sales order
- Fiscal Positions take the Default Tax into account. Therefore, if a Fiscal Position is applied to an invoice, Odoo applies the related tax instead of the Default Taxes, as mapped in the Fiscal Position.
- Databases with multiple companies: the Default Taxes values are company-specific.
- A few Fiscal Positions are already preconfigured on your database, as part of your Fiscal Localization Package.
- The mapping only works with active taxes. Therefore, make sure they are active by going to Accounting ‣ Configuration ‣ Taxes.
- Taxes on eCommerce orders are automatically updated once the visitor has logged in or filled out their billing details.
- The Fiscal Positions’ sequence - the order in which they are arranged - defines which Fiscal Position to apply if the conditions are met in multiple Fiscal Positions.

- For example, if the first Fiscal Position targets country A, and the second Fiscal Position targets a Country Group that also comprises country A, only the first Fiscal Position will be applied to customers from country A.
- Make sure that the tax sequence is correct, as the order in which they are may impact the taxes’ amounts computation, especially if one of the taxes affects the base of the subsequent ones.
- It is not possible to delete taxes that have already been used. Instead, you can deactivate them to prevent future use.
- Invoices: By default, the Line Subtotals displayed on your invoices are Tax-Excluded. To display Tax-Included Line Subtotals, go to Accounting ‣ Configuration ‣ Settings ‣ Customer Invoices, and select Tax-Included in the Line Subtotals Tax Display field, then click on Save.
- eCommerce: By default, the prices displayed on your eCommerce website are Tax-Excluded. To display Tax-Included prices, go to Website ‣ Configuration ‣ Settings ‣ Pricing, and select Tax-Included in the Product Prices field, then click on Save.
- The order in which you add the taxes on a product line has no effect on how amounts are computed. If you add taxes directly on a product line, only the tax sequence determines the order in which they are applied.
- Make sure you have default prices set in the pricelist outside of the deals period. Otherwise you might have issues once the period over.
- The prices order does not matter. The system is smart and applies first prices that match the order date and/or the minimal quantities.
-     Once again the system is smart. If a rule is set for a particular item and another one for its category, Odoo will take the rule of the item.
- Make sure at least one pricelist item covers all your products.
- The default pricelist can be replaced when creating a sales order.

## Purchases
- If you use the Order Date or Confirmation Date filters, the Comparison feature appears next to Filters. It enables you to compare the period you filtered with the previous one.
- 3-way matching is intended to work with the bill control policy set to On received quantities.
- If the quantity Odoo has to reorder doesn’t match the minimum quantity specified, Odoo selects the next vendor on your list. If you don’t have another vendor on your list, the reordering rule won’t work. For that purpose, you can add the same vendor multiple times with different prices for different quantities.
- You can access and create reordering rules from Inventory ‣ Configuration ‣ Reordering Rules and from Inventory ‣ Operations ‣ Replenishment. By default, the replenishment view presents a summary of all the products that you might need to purchase to fulfill your sales orders. From there, you can ask Odoo with a single click to order a product once or automate all orders for that product, future orders included.
- If you selected multiple routes for the same product under its Inventory tab, make sure to select your Preferred Route on your reordering rule by clicking on the optional columns drop-down menu, adding the Preferred Route column, and selecting the right route.
- If you use a Rounding Precision inferior to 0.01, a warning message might appear stating that it is higher than the Decimal Accuracy and that it might cause inconsistencies. If you wish to use a Rounding Precision lower than 0.01, first activate the Developer Mode, then go to Settings ‣ Technical ‣ Database Structure ‣ Decimal Accuracy, select Product Unit of Measure and edit Digits accordingly. For example, if you want to use a rounding precision of 0.00001, set Digits to 5.

## Invoicing and Accounting

- It is not possible to modify the Fiscal Localization of a company once a Journal Entry has been posted.
- Use the aging report to determine which customers are overdue and begin your collection efforts.
- The Profit and Loss statement displays your revenue and expense details. Ultimately, this gives you a clear image of your Net Profit and Loss.
- The balance sheet summarizes your company’s liabilities, assets and equity at a specific moment in time.
- On the bottom left corner, Odoo shows a summary table of all taxes on the vendor bill. In several countries, different methods are accepted to round the totals (round per line, or round globally). The default rounding method in Odoo is to round the final prices per line (as you may have different taxes per product. E.g. Alcohol and cigarettes). However if your vendor has a different tax amount on their bill, you can change the amount in the bottom left table to adjust and match.
- Issuing a credit note is the only legal way to cancel, refund or modify a validated invoice. Don’t forget to register the payment afterward if you need to send money back to your customer.

## Subscriptions

- When the quotation is confirmed by your customers, the products are added to the initial subscription. Quotation prices are, then, prorated to the remaining time of the current invoicing period.
